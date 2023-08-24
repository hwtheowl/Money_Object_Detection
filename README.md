# Money_Object_Detection
Yolov5를 이용하여 저시력자를 위한 원화 화폐 분류를 위한 시각지능 인공지능 모델 개발 프로젝트
<br>
<br>
<br>

## 목차
- [프로젝트 개요](#프로젝트-개요)
- [프로젝트 목적](#프로젝트-목적)
- [개발 환경](#개발-환경)
- [사용 기술](#사용-기술)
- [데이터 소개](#데이터-소개)
- [데이터 전처리](#데이터-전처리)
- [모델링](#모델링)
- [결론](#결론)
- [프로젝트를 통해 느낀점](#프로젝트를-통해-느낀점)
<br>
<br>

## 프로젝트 개요
**원화 권종 분류**

사용자가 스마트폰으로 촬영한 사진, 동영상에서 원화를 판별하고 해당 원화의 금액을 표시
<br>
<br>
<br>

## 프로젝트 목적
**왜?**

시각지능 인공지능을 활용하여 시각적으로 불편한 분들을 위한 편의 서비스를 고려하였습니다.

비교적 빠르고 활용도가 높은 yolov5를 이용하여 간단하게 만들어보았습니다.
<br>
<br>
<br>

## 개발 환경
- Visual Studio Code
- Github
- Colab
- Ubuntu 22.04
<br>
<br>

## 사용 기술
- Python
- Yolov5
<br>
<br>

## 데이터 소개
**원화 권종 8가지, 합산 약 5000개 가량의 이미지 데이터 및 바운딩박스에 관한 정보를 담은 json파일**

![money_images](https://github.com/hwtheowl/Money_Object_Detection/assets/132368135/56df4f48-d460-495c-a007-eb2d9a59a18e)
![image](https://github.com/hwtheowl/Money_Object_Detection/assets/132368135/df310fd3-6624-4240-9468-8b55287acc0a)
<br>
<br>
<br>

## 데이터 전처리
![image](https://github.com/hwtheowl/Money_Object_Detection/assets/132368135/9dd66d44-aecf-4919-83d3-3aee8b87c0fc)

![image](https://github.com/hwtheowl/Money_Object_Detection/assets/132368135/6f338908-4adf-4745-911a-25007af7616f)

이미지파일의 사이즈가 json파일의 정보대비 1/5인 것을 발견하여 사이즈 정보에 대해 1/5 축소 작업 시행

라벨정보중 원화의 앞뒤 구분 제거

라벨 명을 숫자로 변경
<br>
<br>
<br>

## 모델링
**사용 모델: Yolov5l**
**학습 횟수: 50epochs**
![image](https://github.com/hwtheowl/Money_Object_Detection/assets/132368135/0a6163bd-b1f9-4f59-bd4c-54b828138637)

![image](https://github.com/hwtheowl/Money_Object_Detection/assets/132368135/085c0251-4fef-4b0e-8b57-0338e597d7d1)

![results](https://github.com/hwtheowl/Money_Object_Detection/assets/132368135/9a4b5515-e900-463f-8f0a-f8bc39e5b611)

학습및 검증 데이터에 대해서 상당히 높은 정확도를 보임

학습 횟수가 오히려 너무 많아 과적합 문제가 발생 할 것으로 판단
<br>
<br>
<br>

## 결론
![Group 20](https://github.com/hwtheowl/Money_Object_Detection/assets/132368135/65097882-063d-4e99-bd38-4fdc08ef4ec9)

[최종 모델 시연 영상](https://drive.google.com/file/d/1daRO39Z7LAxNOTodlnFBNizc9S_IdmaH/view?usp=drive_link)

똑바로 놓인 하폐에 대해서는 잘 탐지하고 정확도도 준수한 편이지만 손으로 들고 있는 화폐에 대한 탐지 및 정확도가 떨어지는 것으로 판단
<br>
<br>

## 프로젝트를 통해 느낀점
학습에 필요한 데이터 양이 많이 부족하고 모델 성능이 만족스럽지 않다고 느꺘습니다.

로컬 환경의 특성상 yolov5n 모델로 돌려보니 결과가 만족스럽지 못해 점점 큰 모델을 사용하고 결국 코랩에서 yolov5l모델까지 사용하여 학습에서 만족스럽다고 느꼈지만 실제로는 과적합이었다는 것을 알았습니다.

과적합 문제는 학습데이터를 더 늘리고 데이터 변형을 통한 방법으로 해결 할 수 있을거로 생각하고 향후 진행 할 예정입니다.

아쉬움이 있는 프로젝트이지만 시각지능 딥러닝을 학습해보기에 좋은 프로젝트였고 많은 것을 공부해볼수 있었습니다.
