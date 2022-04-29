#데이터 잘 있나 안부 묻기
from glob import glob
from torch import nn
import torch.utils.model_zoo as model_zoo
import torch.onnx

img_list = glob('/home/yunjihwan/바탕화면/Ahagi/Cap/dataset/train/images/*.jpg')
print(len(img_list))

txt_list = glob('/home/yunjihwan/바탕화면/Ahagi/Cap/dataset/train/labels/*.txt')
print(len(txt_list))


#학습 시작합니다
#/home/yunjihwan/바탕화면/Ahagi/Cap/yolov5/train.py  --batch 64 --epochs 300 --data '/home/yunjihwan/바탕화면/Ahagi/Cap/dataset/customdata.yaml' --cfg '/home/yunjihwan/바탕화면/Ahagi/Cap/yolov5/models/yolov5s.yaml' --weights yolov5s.pt --name sevenlable0323

#python /home/yunjihwan/바탕화면/Ahagi/Cap/yolov5/detect.py --weights /home/yunjihwan/바탕화면/Ahagi/Cap/yolov5/runs/train/sevenlable0323_last/weights/best.pt --source /home/yunjihwan/바탕화면/Ahagi/Cap/haha.jpg

#python /home/yunjihwan/바탕화면/Ahagi/Cap/yolov5/export.py  --include onnx --batch 1  --weights /home/yunjihwan/바탕화면/Ahagi/Cap/yolov5/runs/train/sevenlable0323_last/weights/best.pt