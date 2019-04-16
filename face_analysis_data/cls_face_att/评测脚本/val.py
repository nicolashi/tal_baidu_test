import os
import cv2
import numpy as np
import tensorflow as tf
import mtcnn.det_face as mtcnn_detector

face_detector = mtcnn_detector.mtcnn()

sess = tf.Session()

with tf.gfile.GFile('./model/model_channels_last_CPU.pb', 'rb') as file:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(file.read())
    sess.graph.as_default()
    tf.import_graph_def(graph_def, name='')

sess.run(tf.global_variables_initializer())

images = tf.get_default_graph().get_tensor_by_name('input_images:0')

logits_Eyeglasses = tf.get_default_graph().get_tensor_by_name('Eyeglasses/BiasAdd:0')
logits_Male = tf.get_default_graph().get_tensor_by_name('Male/BiasAdd:0')
logits_Mouth_Slightly_Open = tf.get_default_graph().get_tensor_by_name('Mouth_Slightly_Open/BiasAdd:0')

def preprocess_img(img):
    img = cv2.resize(img, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.subtract(img, [123.68, 116.78, 103.94])

    return img

img_dir = './stu_face_attr_anno'

with open('./stu_face_attr_test_raw.txt', 'r') as val_file:
    lines = val_file.readlines()


label_count_Eyeglasses = 0
label_count_Male = 0
label_count_Mouth_Slightly_Open = 0

total_count = 0

Eyeglasses_TP = Eyeglasses_FP = Eyeglasses_TN = Eyeglasses_FN = 0
Male_TP = Male_FP = Male_TN = Male_FN = 0
Mouth_Slightly_Open_TP = Mouth_Slightly_Open_FP = Mouth_Slightly_Open_TN = Mouth_Slightly_Open_FN = 0


for line in lines:
    l = line.strip().split()

    image_name = l[0]
    
    total_count += 1
    
    label_Eyeglasses = 1 if int(l[16]) == 1 else 0
    label_Male = 1 if int(l[21]) == 1 else 0
    label_Mouth_Slightly_Open = 1 if int(l[22]) == 1 else 0
    
    if label_Eyeglasses == 1:
        label_count_Eyeglasses += 1
        
    if label_Male == 1:
        label_count_Male += 1
        
    if label_Mouth_Slightly_Open == 1:
        label_count_Mouth_Slightly_Open += 1
        

    print(image_name)
    
    img = cv2.imread(os.path.join(img_dir, image_name))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    bboxes, _ = face_detector.detect_face_img(img_rgb)

    if len(bboxes) == 1:

        xmin = bboxes[0][0]
        ymin = bboxes[0][1]
        xmax = bboxes[0][2]
        ymax = bboxes[0][3]
        center_x = int((xmin + xmax) // 2)
        center_y = int((ymin + ymax) // 2)

        face_w = int(xmax - xmin)
        face_h = int(ymax - ymin)

        fixed_h = int(face_w * 1.0 * 218 / 178)
        crop_img = img[center_y-fixed_h:center_y+fixed_h, center_x-face_w:center_x+face_w]

        if len(crop_img):

            img_p = preprocess_img(crop_img)
            
            (logit_Eyeglasses, 
            logit_Male, 
            logit_Mouth_Slightly_Open) = sess.run([logits_Eyeglasses, \
                                            logits_Male, \
                                            logits_Mouth_Slightly_Open], {images:np.expand_dims(img_p, axis=0)})
            
            pred_Eyeglasses = np.argmax(logit_Eyeglasses)
            pred_Male = np.argmax(logit_Male)
            pred_Mouth_Slightly_Open = np.argmax(logit_Mouth_Slightly_Open)

            if label_Eyeglasses == 1:
                if pred_Eyeglasses == 1:
                    Eyeglasses_TP += 1
                else:
                    Eyeglasses_FN += 1
            else:
                if pred_Eyeglasses == 0:
                    Eyeglasses_TN += 1
                else:
                    Eyeglasses_FP += 1


            if label_Male == 1:
                if pred_Male == 1:
                    Male_TP += 1
                else:
                    Male_FN += 1
            else:
                if pred_Male == 0:
                    Male_TN += 1
                else:
                    Male_FP += 1


            if label_Mouth_Slightly_Open == 1:
                if pred_Mouth_Slightly_Open == 1:
                    Mouth_Slightly_Open_TP += 1
                else:
                    Mouth_Slightly_Open_FN += 1
            else:
                if pred_Mouth_Slightly_Open == 0:
                    Mouth_Slightly_Open_TN += 1
                else:
                    Mouth_Slightly_Open_FP += 1

print('total_count', total_count)

print('Eyeglasses_count', label_count_Eyeglasses)
print('accuracy', (Eyeglasses_TP + Eyeglasses_TN) / (Eyeglasses_TP + Eyeglasses_FP + Eyeglasses_FN + Eyeglasses_TN))
print('positive')
print('precision', Eyeglasses_TP / (Eyeglasses_TP + Eyeglasses_FP))
print('recall', Eyeglasses_TP / (Eyeglasses_TP + Eyeglasses_FN))
print('negative')
print('precision', Eyeglasses_TN / (Eyeglasses_TN + Eyeglasses_FN))
print('recall', Eyeglasses_TN / (Eyeglasses_TN + Eyeglasses_FP))


print('Male_count', label_count_Male)
print('accuracy', (Male_TP + Male_TN) / (Male_TP + Male_FP + Male_FN + Male_TN))
print('positive')
print('precision', Male_TP / (Male_TP + Male_FP))
print('recall', Male_TP / (Male_TP + Male_FN))
print('negative')
print('precision', Male_TN / (Male_TN + Male_FN))
print('recall', Male_TN / (Male_TN + Male_FP))


print('Mouth_Slightly_Open_count', label_count_Mouth_Slightly_Open)
print('accuracy', (Mouth_Slightly_Open_TP + Mouth_Slightly_Open_TN) / (Mouth_Slightly_Open_TP + Mouth_Slightly_Open_FP + Mouth_Slightly_Open_FN + Mouth_Slightly_Open_TN))
print('positive')
print('precision', Mouth_Slightly_Open_TP / (Mouth_Slightly_Open_TP + Mouth_Slightly_Open_FP))
print('recall', Mouth_Slightly_Open_TP / (Mouth_Slightly_Open_TP + Mouth_Slightly_Open_FN))
print('negative')
print('precision', Mouth_Slightly_Open_TN / (Mouth_Slightly_Open_TN + Mouth_Slightly_Open_FN))
print('recall', Mouth_Slightly_Open_TN / (Mouth_Slightly_Open_TN + Mouth_Slightly_Open_FP))
