#import package

import glob
import dlib
import os.path as osp
import pymysql
# import mysql.connector
import random
import numpy as np
import json
from PIL import Image
from tqdm import tqdm
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import torchvision
from torchvision import models, transforms




#파이토치 버전
print("PyTorch Version: ", torch.__version__)
print("Torchvision Version: ", torchvision.__version__)

torch.manual_seed(1234)
np.random.seed(1234)
random.seed(1234)

#입력 이미지의 전처리 클래스
#훈련시와 추론시 처리가 다르다

class ImageTransform():

    def __init__(self, resize, mean, std):
        
        self.data_transform = {
            'train': transforms.Compose([
                transforms.RandomResizedCrop(
                    resize,scale = (0.5,1.0) #데이터 확장
                ),
                transforms.RandomHorizontalFlip(), #데이터 확장
                transforms.ToTensor(), #텐서 변환
                transforms.Normalize(mean,std) #표준화
            ]),
            'val': transforms.Compose([
                transforms.Resize(resize), #리사이즈
                transforms.CenterCrop(resize), #이미지 중앙을 resize*resize로 자르기
                transforms.ToTensor(), #텐서로 변환
                transforms.Normalize(mean,std) #표준화
            ])
        }

    def __call__(self,img,phase='train'):
        


        return self.data_transform[phase](img)


def align_faces(img):  #원본이미지를 넣으면 align 완료된 얼굴이미지 반환하는 함수
    
    # plt.imshow(img)

    dets = detector(img,1)

    objs = dlib.full_object_detections()

    for detection in dets:
        s = sp(img, detection)
        objs.append(s)

    faces = dlib.get_face_chips(img, objs, size=256, padding=0.35)

    return faces



# 이미지 파일의 경로 리스트 작성하기
def make_datapath_list(phase="train"):
    

    rootpath = "./imgdata/personal_data/"
    target_path = osp.join(rootpath+phase+'/**/*.jpg')

    path_list = [] #여기에 저장

    #glob를 이용하여 하위 디렉토리의 파일 경로를 가져온다
    for path in glob.glob(target_path):
        
        path_list.append(path)
    
    return path_list



#학습된 mobilenetv2 모델을 로드
#모델의 인스턴스를 생성

use_pretrained = True #학습된 파라미터를 사용한다
net = models.mobilenet_v2(pretrained = False)
'''새롭게 훈련시킨 모델 사용하기 때문에 pretrained: False)
# use_pretrained'''


#마지막 출력층의 출력 유닛을 spring,summer,fall,winter 4가지로 바꾼다

net.classifier[1] = nn.Linear(in_features=1280, out_features=4, bias=True)
loadmodel = torch.load('/home/pi/pythonProject/model.pth')
net.load_state_dict(loadmodel)
# 훈련 모드
# net.train()


print("네트워크 설정 완료: 학습된 가중치를 읽어들여 훈련 모드로 설정했다.")



size = 224

mean = (0.485, 0.456, 0.406)

std = (0.229, 0.224, 0.225)


detector = dlib.get_frontal_face_detector()  #얼굴 영역 인식 모델 로드
sp = dlib.shape_predictor("/home/pi/pythonProject/shape_predictor_5_face_landmarks.dat")


# 테스트할 이미지 경로
# jpg 이미지 처리

image_file_path = '/home/pi/pythonProject/photo.jpg'
#image_file_path = './photo.jpg'

#img = Image.open(image_file_path)
img = dlib.load_rgb_image(image_file_path)
img = align_faces(img)
img = Image.fromarray(np.uint8(img[0])).convert('RGB')


#plt.imshow(img)
#plt.show()



transform = ImageTransform(size,mean,std)
img_transformed = transform(img,phase='val')
img_transformed = img_transformed.unsqueeze(0)
net.eval()
outputs = net(img_transformed)
_, preds = torch.max(outputs, 1)

######### DB Part ########

db = pymysql.Connect(host='52.78.177.38', user='hihi', password='1234', database='IGOAT')
cursor = db.cursor()

query = "select count from IGOAT.people"
allcount = cursor.execute(query)

color = "color"

import shutil

import data

query = "select man from IGOAT.select"
man_cnt = cursor.execute(query)



print('--------')
if preds[0] == torch.tensor(0) and man_cnt == 1:
    print('spring')
    color = "spring"
    source = "/home/pi/pythonProject/spring.jpg"
    query = "UPDATE `IGOAT`.`select` SET `blue_cnt` = '0' WHERE (`blue_cnt` = '1');"
    cursor.execute(query)

elif preds[0] == torch.tensor(0) and man_cnt == 0:
    print('springwomen')
    color = "spring"
    source = "/home/pi/pythonProject/springwomen.jpg"
    query = "UPDATE `IGOAT`.`select` SET `blue_cnt` = '0' WHERE (`blue_cnt` = '1');"
    cursor.execute(query)

elif preds[0] == torch.tensor(1) and man_cnt == 1:
    print('summer')
    color = "summer"
    source = "/home/pi/pythonProject/summer.jpg"
    query = "UPDATE `IGOAT`.`select` SET `blue_cnt` = '1' WHERE (`blue_cnt` = '0');"
    cursor.execute(query)

elif preds[0] == torch.tensor(1) and man_cnt == 0:
    print('summerwomen')
    color = "summer"
    source = "/home/pi/pythonProject/summerwomen.jpg"
    query = "UPDATE `IGOAT`.`select` SET `blue_cnt` = '1' WHERE (`blue_cnt` = '0');"
    cursor.execute(query)

elif preds[0] == torch.tensor(2) and man_cnt == 1:
    print('fall')
    color = "fall"
    source = "/home/pi/pythonProject/fall.jpg"
    query = "UPDATE `IGOAT`.`select` SET `blue_cnt` = '0' WHERE (`blue_cnt` = '1');"
    cursor.execute(query)

elif preds[0] == torch.tensor(2) and man_cnt == 0:
    print('fallwomen')
    color = "fall"
    source = "/home/pi/pythonProject/fallwomen.jpg"
    query = "UPDATE `IGOAT`.`select` SET `blue_cnt` = '0' WHERE (`blue_cnt` = '1');"
    cursor.execute(query)

elif preds[0] == torch.tensor(3) and man_cnt == 1:
    print('winter')
    color = "winter"
    source = "/home/pi/pythonProject/winter.jpg"
    query = "UPDATE `IGOAT`.`select` SET `blue_cnt` = '1' WHERE (`blue_cnt` = '0');"
    cursor.execute(query)

elif preds[0] == torch.tensor(3) and man_cnt == 0:
    print('winterwomen')
    color = "winter"
    source = "/home/pi/pythonProject/winterwomen.jpg"
    query = "UPDATE `IGOAT`.`select` SET `blue_cnt` = '1' WHERE (`blue_cnt` = '0');"
    cursor.execute(query)

query3 = "insert into people(count,color) values (%s,%s)"
value = (allcount,color)

cursor.execute(query3,value)
db.commit()



destination = "/home/pi/pythonProject/crst.jpg"

shutil.copyfile(source, destination)

print(preds)

print('--------')
