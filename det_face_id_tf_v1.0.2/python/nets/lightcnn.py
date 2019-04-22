from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import tensorflow.contrib.slim as slim


def MFM(x,name):
	with tf.variable_scope(name):
		#shape is in format [batchsize, x, y, channel]
		shape = x.get_shape().as_list()
		#print(shape)
		res = tf.reshape(x,[-1,shape[1],shape[2],2,shape[-1]//2])
		res = tf.reduce_max(res,axis=[3])
		return res

def MFM_FC(x,name):
	with tf.variable_scope(name):
		shape = x.get_shape().as_list()
		# print('fcshape:',shape)
		res = tf.reduce_max(tf.reshape(x,[-1,2,shape[-1]//2]),reduction_indices=[1])
	return res


def inference(images, keep_probability, phase_train=True,
              bottleneck_layer_size=128, weight_decay=0.0, reuse=None):
    batch_norm_params = {
        # Decay for the moving averages.
        'decay': 0.995,
        # epsilon to prevent 0s in variance.
        'epsilon': 0.001,
        # force in-place updates of mean and variance estimates
        'updates_collections': None,
        # Moving averages ends up in the trainable variables collection
        'variables_collections': [ tf.GraphKeys.TRAINABLE_VARIABLES ],
    }

    with slim.arg_scope([slim.conv2d, slim.fully_connected],
                        weights_initializer=tf.truncated_normal_initializer(stddev=0.1),
                        weights_regularizer=slim.l2_regularizer(weight_decay),
                        normalizer_fn=slim.batch_norm,
                        normalizer_params=batch_norm_params):
        return light_cnn(images, is_training=phase_train,
              dropout_keep_prob=keep_probability, bottleneck_layer_size=bottleneck_layer_size, reuse=reuse)


def light_cnn(inputs, is_training=True,
                        dropout_keep_prob=0.75,
                        bottleneck_layer_size=512,
                        reuse=None,
                        scope='Light_CNN'):
    end_points = {}

    with tf.variable_scope(scope, 'Light_CNN', [inputs], reuse=reuse):
        with slim.arg_scope([slim.batch_norm, slim.dropout],
                            is_training=is_training):
            with slim.arg_scope([slim.conv2d, slim.max_pool2d, slim.avg_pool2d],
                                stride=1, padding='SAME'):

                net = slim.conv2d(inputs, 96, 5, stride=1, padding='SAME',activation_fn=None,
                                  scope='Conv2d_1a_5x5')
                net = MFM(net,name='Conv2d_1a_5x5_MFM')
                net = slim.max_pool2d(net, [2, 2], stride=2, scope='maxpool1')
                end_points['Conv2d_1a_5x5'] = net

                net = slim.conv2d(net, 96, 1, padding='SAME',activation_fn=None,
                                  scope='Conv2d_1b_1x1')
                net = MFM(net,name='Conv2d_1b_1x1_MFM')
                end_points['Conv2d_1b_1x1'] = net

                net = slim.conv2d(net, 192, 3, stride=1, padding='SAME',activation_fn=None,
                                  scope='Conv2d_2a_3x3')
                net = MFM(net,name='Conv2d_2a_3x3_MFM')
                net = slim.max_pool2d(net, [2, 2], stride=2, scope='maxpool2')
                end_points['Conv2d_2a_3x3'] = net

                net = slim.conv2d(net, 192, 1, padding='SAME',activation_fn=None,
                                  scope='Conv2d_2b_1x1')
                net = MFM(net,name='Conv2d_2b_1x1_MFM')
                end_points['Conv2d_2b_1x1'] = net

                net = slim.conv2d(net, 384, 3, stride=1, padding='SAME',activation_fn=None,
                                  scope='Conv2d_3a_3x3')
                net = MFM(net,name='Conv2d_3a_3x3_MFM')
                net = slim.max_pool2d(net, [2, 2], stride=2, scope='maxpool3')
                end_points['Conv2d_3a_3x3'] = net

                net = slim.conv2d(net, 384, 1, padding='SAME',activation_fn=None,
                                  scope='Conv2d_3b_1x1')
                net = MFM(net,name='Conv2d_3b_1x1_MFM')
                end_points['Conv2d_3b_1x1'] = net

                net = slim.conv2d(net, 256, 3, stride=1, padding='SAME',activation_fn=None,
                                  scope='Conv2d_4a_3x3')
                net = MFM(net,name='Conv2d_4a_3x3_MFM')
                end_points['Conv2d_4a_3x3'] = net

                net = slim.conv2d(net, 256, 1, padding='SAME',activation_fn=None,
                                  scope='Conv2d_4b_1x1')
                net = MFM(net,name='Conv2d_4b_1x1_MFM')
                end_points['Conv2d_4b_1x1'] = net

                net = slim.conv2d(net, 256, 3, stride=1, padding='SAME',activation_fn=None,
                                  scope='Conv2d_5a_3x3')
                net = MFM(net,name='Conv2d_5a_3x3_MFM')
                net = slim.max_pool2d(net, [2, 2], stride=2, scope='maxpool5')
                end_points['Conv2d_5a_3x3'] = net


                with tf.variable_scope('Logits'):
                    end_points['PrePool'] = net
                    net = slim.flatten(net)

                    net = slim.dropout(net, dropout_keep_prob, is_training=is_training,
                                       scope='Dropout')

                    end_points['PreLogitsFlatten'] = net

                net = slim.fully_connected(net, bottleneck_layer_size*2, activation_fn=None,
                        scope='Bottleneck', reuse=False)
                net = MFM_FC(net,name='MFM_output')

    return net, end_points
