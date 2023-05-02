## My PC - 퍼스널 컬러 진단 키오스크, 웹페이지 제작

#### My PC 링크(웹, 모바일) : [http://i8c201.p.ssafy.io:3000](http://i8c201.p.ssafy.io:3000/)

---

#### 소개 영상 보기 :

---

#### 프로젝트 진행 기간

2023.01.03 ~ 2023.02.17(총 7주)

---

#### My PC - 특장점

- ##### 빠르고 간편한 퍼스널컬러 진단
  
  - 많은 사람들이 자신의 퍼스널 컬러를 모르는데 그 이유는 비싼 비용, 꽉 차 있는 예약시스템 그리고 직접 가야되는 귀찮기때문이다.
    
  - 진단이 필요한 상황이 면접이나 정장을 맞출 때 등 외에는 거의 전무하다.
    
  - 그렇다고 진단이 필요한 상황에 진단을 하느냐? 그것도 아니다. 왜? 진단 과정이 귀찮고, 시간과 비용이 부담이 되어서.
    
  - 우리 시스템을 이용하면 10초면 진단이 가능하다. 진단을 위해 귀찮게 어딜 찾아가야할 필요도 없다. 비용도 들지 않는다.
    
- ##### 사용자의 제품 선택을 보조한다
  
  - 퍼스널 컬러에 적합한 화장품, 예를 들어 파운데이션의 호수나 블러셔의 색상 등, 의류라면 어울리는 색상과 조합을 추천하기 때문에 사용자의 제품 선택을 보조할 수 있다. 사용자의 구매욕을 높여 수익성 증대로도 이어질 것이다.
- ##### 기업의 제품 기획 단계에서 손실 최소
  
  - 키오스크에서 진단을 마친 사용자들의 컬러 데이터가 데이터베이스에 숫자로
    저장되어있기 때문에 제품 기획 단계에서 손실이 줄어든다. 예를 들어 100명의 사람이 진단을 하였고 70명의 사람이 봄 웜톤 컬러로 진단, 나머지 30명의 사람이 여름,가을,겨울 컬러로 분산되어있다고 가정하자. 제품 기획 단계에서 봄 웜톤에게 어울리는 색상의 의류와 화장품 호수를 주력으로 제작하거나, 홍보하였을 때 기존의 기획과 제작방식보다 재고관리에 용이하고 수익성 또한 증대될 수 있을 것이다.

---

#### 주요 기능

- ##### 퍼스널 컬러 진단
  
- ##### 게시글(개인PC 별 게시판 나눔)
  
- ##### 화장 시뮬레이션
  
- ##### 팔로우
  

---

#### 주요 기술

###### Backend

- node.js
- express

###### Frontend

- React

###### CI/CD

- AWS
- Jenkins

---

#### 프로젝트 파일 구조

##### Back

```
backend
  ├── BeautyGAN
  ├── config
  │   └── db
  ├── images
  ├── MobileNetV2
  ├── models
  │   ├── board
  │   ├── index
  │   ├── story
  │   └── user
  ├── node_modules
  ├── distance.py
  ├── Dockerfile
  ├── encoding_img_list.pkl
  ├── makeup.py
  ├── package-lock.json
  ├── package.json
  ├── personalcolor.py
  ├── README.md
  ├── requirements.txt
  ├── server.js
  └── storage.js
```

##### Front

```
frontend
  ├── node_modules
  ├── public
  ├── config
  ├── scripts
  └── src
      ├── App.css
      ├── App.js
      ├── App.test.js
      ├── index.css
      ├── index.js
      ├── logo.svg
      ├── reportWebVitals.js
      ├── setupTests.js
      ├── components
      │   ├── Card
      │   ├── ChangePc
      │   ├── ColorSelector
      │   ├── Home
      │   ├── ImageUploader
      │   ├── MakeUp
      │   ├── MyProfileimageUploader
      │   ├── OutputImg
      │   ├── ProfileCard
      │   ├── SeasonSelector
      │   ├── StoryEdit
      │   ├── StoryUploader
      │   └── TextArea
      ├── Layout
      │   ├── Footer
      │   └── Header
      ├── pages
      │   ├── Addboard
      │   ├── Board
      │   ├── BoardList
      │   ├── EditPage
      │   ├── Login
      │   ├── MakeUp
      │   ├── MyProfile
      │   ├── PersonalColor
      │   ├── Season
      │   ├── SignPersonalColor
      │   ├── Signup
      │   ├── StoryCreator
      │   ├── StoryUploader
      │   └── UserProfile
      ├── redux
      ├── routes
      └── utils
          ├── api.js
          └── jwtUtils.js
```

---

#### 협업 툴

- Git
  
- JIRA
  
- MatterMost
  
- Webex
  

---

#### 협업 환경

- Gitlab
  
  - 코드의 버전을 관리
  - 이슈 발행, 해결을 위한 토론
  - 머지시 코드리뷰 후 피드백
- JIRA
  
  - 매주 목표량을 설정하고 등록하여 Sprint 진행
  - 업무의 할당량을 정하여 Story Point를 설정
- 스크럼 회의

  - 매일 아침마다 오늘 할 일을 생각하고 실행

---

#### My PC 임베디드 구조물

 
<img src="./emb_jpg/구조물.jpg" width="400" height="250"/>

 - RPI4 리눅스 내의 구동을 태블릿 PC를 이용해 가시적으로 출력
 
 - 카메라 모듈이 태블릿 PC 상단에 설치되어 있어 촬영 기능 수행
 
 - 키오스크 형태의 구조물로 의자에 앉아서 사용할 수 있도록 구조 설치
 
 - 기업과 연계함을 가정해 사업장 앞에 설치한다고 가정
 
 
 
 
 - ###### 사용자 화면
 
   - 사용자에게 보여지는 첫 화면
   
   - 퍼스널 컬러 진단 키오스크임을 알림
   
<img src="./emb_jpg/0_첫화면.jpg" width="400" height="250"/>



 - ###### 서비스 설명
 
   - 서비스 설명 화면
   
   <img src="./emb_jpg/1_서비스설명.jpg" width="400" height="250"/>
   


 - ###### 성별 선택
 
   - 정확한 진단과 정보 수집을 위한 성별 선택
   
   <img src="./emb_jpg/2_성별선택.jpg" width="400" height="250"/>
   
   
    

 - ###### 카메라 촬영
 
   - 진단을 위한 카메라 촬영
   
   - 카메라 모듈은 Opencv와 tensorflow를 이용해 사용자의 눈, 코, 입 위치를 판별
   
   - 정확한 진단을 위해 눈,코,입이 모두 판별된다면 그 시점 촬영
   
   - 촬영된 사진은 Pytorch를 이용한 AI 모듈에 올라가게 된다.
   
   <img src="./emb_jpg/3_카메라촬영.jpg" width="400" height="250"/>
      
   
    

 - ###### AI진단
 
   - AI 퍼스널컬러 진단 화면
   
   - AI 모듈이 결과 값을 낼 때까지 시간이 소요되기 때문에 그 시간 동안 출력되는 화면
   
   <img src="./emb_jpg/4_AI진단.jpg" width="400" height="250"/>
         
   
    

 - ###### 진단 후 아이템 추천
 
   - 퍼스널컬러 진단이 완료 되어 결과값이 출력된다. 결과값은 겨울쿨톤,가을웜톤,여름쿨톤,봄웜톤 4가지이다.
   
   - 각 퍼스널컬러 결과에 맞는 QR 코드가 출력되어 웹페이지로 연결가능하도록 출력된다.
   
   - 각 퍼스널컬러 결과에 어울리는 사업장 내 컬러 아이템이 출력된다.
   
   
   <img src="./emb_jpg/5_진단후추천.jpg" width="400" height="250"/>
           
   
    

 - ###### 아이템 상세 내용
   
   
   - 아이템을 선택하면 가능한 사이즈, 사이즈 표, 환불정책 등 상세내용을 볼 수 있다.
   
   
   
   <img src="./emb_jpg/6_상세내용.jpg" width="400" height="250"/>
   
   

#### My PC 웹 서비스 화면

- ###### 회원가입
  
  - 아이디 중복 제한
    
  - 비밀번호 유효성 검증
    
  - 회원가입 페이지 에서 PC진단 가능

<img src="./gif/회원가입_AdobeExpress.gif" width="400" height="250"/>


- ###### 게시판
  
  - 봄, 여름, 가을, 겨울 별 커뮤니티 공유
    
  - 톤 별 Best Color과 Worst Color 제공

<img src="./gif/게시판_AdobeExpress.gif" width="400" height="250"/>


- ###### 게시물 등록
  
  - 추천하고 싶은 아이템 등록 가능

<img src="./gif/게시물_등록_AdobeExpress.gif" width="400" height="250"/>


- ###### 내 PC 진단
  
  - 내 PC 진단 기능

<img src="./gif/PC_진단_AdobeExpress.gif" width="400" height="250"/>

- ###### 화장 시뮬레이션
  
  - 톤별 기본 화장 이미지 6개 제공
    
  - 자신의 사진에 화장을 입힐 수 있음
    
  - 만족시 결과 사진과 유사한 5장 불만족시 상반된 사진 5장 추천

<img src="./gif/화장_시뮬레이션_AdobeExpress.gif" width="400" height="250"/>    

- ###### 내 프로필
  
  - 프로필 이미지 등록기능
    
  - 자기소개 등록기능
    
  - 내가 작성한 게시물 확인 가능
    
  - 내 팔로워수 확인

<img src="./gif/내_프로필_AdobeExpress.gif" width="400" height="250"/>    

- ###### 유저 프로필
  
  - 팔로우기능
    
  - 유저의 게시글 확인

<img src="./gif/유저_프로필_AdobeExpress.gif" width="400" height="250"/>    

---
