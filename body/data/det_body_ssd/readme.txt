此文件夹为各模型指标评测脚本；

一、det_body_ssd模型（人脸检测框,多人场景）
1、sdk结果存放文件result.txt，格式如下：
test_img_name xmin ymin xmax ymax score（置信度）

ps：若一张图片有多个检测框时，结果文件依次写入所有框及置信度结果：
test_img_name xmin ymin xmax ymax score xmin ymin xmax ymax score

2、模型指标评测脚本
存放位置：evaluatingScriptsdet_body_ssd\detBodySsdRelPre.py
 
###################################################
执行：
python3 detBodySsdRelPre.py 	#默认参数见下

#-result_path（结果文件路径）
#-img_path（测试集路径，画图部分需要获取原图）
#-label_path（标注框xml文件所在目录，目录内文件数 == sdk结果行数）
#-save_path （最终输出各项结果保存路径）
#-thr（算法工程师推荐阈值，默认阈值）
python det_face_test.py -result_path ./result.txt -img_path test_data/px_img/ -label_path test_data/px_json/ -save_path results/ -thr 0.5
    
##################################################
输出结果：
recall&precision曲线图.png（命名规则：det_body_ssd.png） ;
详细指标数据.xlsx（命名规则同输入文件名：result.xlsx ;




