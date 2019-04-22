# -*- coding: utf-8 -*-

import sys
import os
import tensorflow as tf
import numpy as np
import facenet
import random
import cv2
import time


def load_gallery(data_dir):
	gallery_list = os.listdir(data_dir)
	gallery_img = [s for s in gallery_list if (s.endswith('.png') or s.endswith('.jpg'))]

	gallery = [0 for i in range(len(gallery_img))]
	for img_path in gallery_img:
		#label = int(img_path.split('.')[0])-150
		label = int(img_path.split('.')[0])
		gallery_img = cv2.imread(os.path.join(data_dir,img_path))
		gallery[label] = gallery_img
	return gallery

def load_test_data(test_data_dir):
	file_list = os.listdir(test_data_dir)
	person_list = [p for p in file_list if not os.path.isfile(os.path.join(test_data_dir,p))]
	#print person_list
	img_path_list = []
	for p in person_list:
		person_path = os.path.join(test_data_dir,p)
		tmp_path = os.listdir(person_path)
		#print tmp_path
		for img in tmp_path:
			if (img.endswith('.png') or img.endswith('.jpg')):
				#img_pair = (os.path.join(test_data_dir,p,img),int(p)-150)
				img_pair = (os.path.join(test_data_dir,p,img),int(p))
				img_path_list.append(img_pair)
	return img_path_list

def cal_cos_dist(emb1,emb2):
	dot_result = np.sum(emb1*emb2)
	emb1_norm = np.sqrt(np.sum(np.square(emb1)))
	emb2_norm = np.sqrt(np.sum(np.square(emb2)))
	#print dot_result, emb1_norm, emb2_norm
	return float(dot_result/(emb1_norm*emb2_norm))

def main():
    # Path to gallery
	gallery_dir = '../images/gallery'
	gallery = load_gallery(gallery_dir)

	# Path to test data
	test_data_dir = '../images/test'
	test_data = load_test_data(test_data_dir)

	# Path to model
	print "[FaceNet]Loading trained model..."
	model_dir = '../models_ckpt'
	encoder = facenet.facenet_encoder(model_dir)

	correct = [0 for i in range(len(gallery))]
	group_count = [0 for i in range(len(gallery))]
	count = 0


	gallery_embedding = []
	for g_img in gallery:
		g_rep = encoder.generate_single_embedding(g_img)
		gallery_embedding.append(g_rep)

	for img_path in test_data:
		img = cv2.imread(img_path[0])
		l = img_path[1]
		test_rep = encoder.generate_single_embedding(img)
		dist = []
		for rep in gallery_embedding:
			tmp_dist = cal_cos_dist(rep,test_rep)
			dist.append(tmp_dist)
		tmp_l = np.argmax(dist)
		if tmp_l == l:
			correct[l] += 1
		group_count[l] += 1
		count += 1
		print "{0} / {1} acc: {2}".format(np.sum(correct),count,float(np.sum(correct))/count)


	for i in range(len(group_count)):
		print "Label {0} : {1} / {2}  acc: {3:.5f}".format(i,correct[i],group_count[i],float(correct[i])/group_count[i])
	print "Total correct image: {0}".format(correct)
	print "Overall test accuracy: {0:.5f}    of {1} images".format(float(np.sum(correct))/count,count)

if __name__ == '__main__':
	main()
