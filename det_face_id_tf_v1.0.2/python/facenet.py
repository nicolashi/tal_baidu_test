import sys
import os
import tensorflow as tf
import numpy as np
import pickle
import random
import cv2
import time

from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from sklearn.preprocessing import LabelEncoder

class facenet_encoder:
    def __init__(self,model_dir):
        self.sess = tf.Session()
        with self.sess.as_default():
            st = time.time()
            meta_file = self.get_meta(model_dir)
            restore_saver = tf.train.import_meta_graph(meta_file)
            restore_saver.restore(self.sess,tf.train.latest_checkpoint(model_dir))
            print "Loading model took {0} seconds".format(time.time()-st)

            self.images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            self.embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            self.phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

            self.image_size = self.images_placeholder.get_shape()[1]
            print "Input image size: {0}*{0}".format(self.image_size)
            self.embedding_size = self.embeddings.get_shape()[1]

    def generate_batch_embeddings(self,faces_list,batch_size=50):
        print "[FaceNet]Generating embeddings of images..."
        input_data = []
        input_labels = []
        for it in faces_list:
            for face in it['img']:
                face = cv2.resize(face,(self.image_size,self.image_size))
                face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
                #face = np.transpose(face, (2,1,0))
                img_mean = np.mean(face,axis=(0,1))
                img_std = np.std(face,axis=(0,1))
                num_elements = int(self.image_size*self.image_size)
                adjusted_stddev = np.maximum(img_std,1.0/np.sqrt(num_elements))
                face = (face - img_mean) / adjusted_stddev
                input_data.append(face)
                input_labels.append(it['id'])
        batch_size = 50
        num_data = len(input_data)
        num_batches = int(np.ceil(1.0 * num_data / batch_size))
        embeddings_array = np.zeros((num_data,self.embedding_size))

        st = time.time()
        for i in range(num_batches):
            start_index = i*batch_size
            end_index = min((i+1)*batch_size,num_data)
            data_batch = input_data[start_index:end_index]
            feed_dict = {self.images_placeholder:data_batch,self.phase_train_placeholder:False}
            embeddings_array[start_index:end_index,:] = self.sess.run(self.embeddings,feed_dict=feed_dict)

        time_avg_forward_pass = (time.time() - st) / float(num_data)
        print("Forward pass took avg of {0:.3f}[seconds/image] for {1} images".format(time_avg_forward_pass, num_data))

        return embeddings_array,input_labels

    def generate_single_embedding(self,image):
        image = cv2.resize(image,(self.image_size,self.image_size))
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        img_mean = np.mean(image,axis=(0,1))
        img_std = np.std(image,axis=(0,1))
        num_elements = int(self.image_size*self.image_size)
        adjusted_stddev = np.maximum(img_std,1.0/np.sqrt(num_elements))
        image = (image - img_mean) / adjusted_stddev
        #image = tf.image.per_image_standardization(image)
        image = image.reshape((1,self.image_size,self.image_size,3))
        feed_dict = {self.images_placeholder:image,self.phase_train_placeholder:False}
        embedding = self.sess.run(self.embeddings,feed_dict=feed_dict)
        return embedding

    def get_meta(self,model_dir):
		files = os.listdir(model_dir)
		meta_files = [s for s in files if s.endswith('.meta')]
		if len(meta_files)==0:
		    raise ValueError('No meta file found in the model directory (%s)' % model_dir)
		elif len(meta_files)>1:
		    raise ValueError('There should not be more than one meta file in the model directory (%s)' % model_dir)
		meta_file = os.path.join(model_dir,meta_files[0])
		return meta_file
