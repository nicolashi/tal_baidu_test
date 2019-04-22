【版权所有】：(C)2017 TAL-AI Lab
【模型名称】：det_face_id
【发布版本】：v1.0.2
【发布时间】：2018-09-13
【训练作者】：蔡育锋

【功能简介】
 1-人脸向量化-用于人脸识别

【性能测试-Python】
 1-CPU型号：
 2-CPU占用：
 3-GPU型号：
 4-GPU占用：
 5-GPU峰值：
 6-内存占用：
 7-精   度： 0.88372
 8-前向运算速度： ~0.04 秒/图

【性能测试-C++】
 1-CPU型号：
 2-CPU占用：
 3-GPU型号：
 4-GPU占用：
 5-GPU峰值：
 6-内存占用：
 7-精   度：
 8-前向运算速度：

【输入数据】
input place_holder: "input:0"
train phrase place_holder: "phase_train:0"

【输出结果】
output place_holder: "embeddings:0" // 长度为256维的特征向量
