���ļ���Ϊ��ģ��ָ������ű���

һ��det_body_ssdģ�ͣ���������,���˳�����
1��sdk�������ļ�result.txt����ʽ���£�
test_img_name xmin ymin xmax ymax score�����Ŷȣ�

ps����һ��ͼƬ�ж������ʱ������ļ�����д�����п����ŶȽ����
test_img_name xmin ymin xmax ymax score xmin ymin xmax ymax score

2��ģ��ָ������ű�
���λ�ã�evaluatingScriptsdet_body_ssd\detBodySsdRelPre.py
 
###################################################
ִ�У�
python3 detBodySsdRelPre.py 	#Ĭ�ϲ�������

#-result_path������ļ�·����
#-img_path�����Լ�·������ͼ������Ҫ��ȡԭͼ��
#-label_path����ע��xml�ļ�����Ŀ¼��Ŀ¼���ļ��� == sdk���������
#-save_path �������������������·����
#-thr���㷨����ʦ�Ƽ���ֵ��Ĭ����ֵ��
python det_face_test.py -result_path ./result.txt -img_path test_data/px_img/ -label_path test_data/px_json/ -save_path results/ -thr 0.5
    
##################################################
��������
recall&precision����ͼ.png����������det_body_ssd.png�� ;
��ϸָ������.xlsx����������ͬ�����ļ�����result.xlsx ;




