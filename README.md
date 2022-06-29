## 소개

저희 Do_not_worry 프로젝트는 시각장애인들을 위한 프로젝트 입니다.

 시각장애라는 상황 덕에 비장애인과 비교했을때, 압도적으로 교육과 관련된 환경이 많이 부족한것은 사실입니다.
 
 그렇기 때문에 시각장애인들의 책 읽는 눈을 대신하는 프로젝트로써, 사진을 스캔하면 사진속의 텍스트들을 음성으로 들을 수 있도록 해주는 프로젝트를 구현 했습니다.
 
  시각정보가 제한된다는 상황에서, 다른 사람이 읽어주지 않는 한 글을 보기 지 않지만,  직접 이미지를 스캔하여 음성으로 들어 정보를 얻을 수 있다는 장점이 있습니다.
  
  해당 프로젝트를 사용하여, 읽고 싶은 책 또는 텍스트가 담긴 정보를  다른 사람의 도움 없이 언제 어디서든 쉽게 이해할 수 있게 함으로써 시각장애인들 또한 불편함 속에서 더 나은 양질의 교육을 받을 수 있는 기반을 마련할 수 있습니다.


## 개발 환경 및 사용 기술
-------------------
저희 프로젝트는 `Front-end` 로는 `Flutter` 를 사용했고, `Back-end` 로는 `Django` 를 사용했습니다.

### 개발 운영체제

- `Flutter` - Windows 10
- `Django` - ubuntu 18.04
  
### 사용 라이브러리 및 API

- `Flutter` 

  * [image_picker](https://pub.dev/packages/image_picker)
  * [audioplayers](https://pub.dev/packages/audioplayers)
  * http


- `Django`
  
  * [REST framework](https://www.django-rest-framework.org/)
  * [Requests](https://docs.python-requests.org/en/latest/)
  * [NaverClova OCR](https://www.ncloud.com/product/aiService/ocr)

  
## 사전 작업

사용하기 전에, [Requests](https://docs.python-requests.org/en/latest/) 라이브러리를 사용하여 [NaverClova OCR](https://www.ncloud.com/product/aiService/ocr) 를 통해 OCR 을 수행하므로, API 키를 발급 해야 합니다.

[NAVER OCR 공식문서](https://guide.ncloud-docs.com/docs/ko/ocr-ocr-1-1) 를 참고해주세요.



## 기능 소개
-------------------
시각 장애인들을 위한 프로젝트이기 때문에 UI 자체의 디자인은 심플하게 구현했습니다.

구현된 기능은 자신이 읽고 싶은 텍스트가 있는 사진을 스캔하면 스피커를 통하여 스캔된 텍스트를 읽어줍니다.


구현 이미지
-------------------
![image](https://user-images.githubusercontent.com/81365408/152623074-bdf6b4d7-fbcf-4fcd-baa4-264665b9a645.png)

앱 실행시 로딩 화면

![image](https://user-images.githubusercontent.com/81365408/152622085-7938211f-26c7-47f8-8926-bb94434dfaff.png)

현재 화면에서는 앱의 사용법이 간단하게 음성으로 나오고 있습니다.

![image](https://user-images.githubusercontent.com/81365408/152622064-217ff48d-6b82-434a-8535-97f9362ed03f.png)

예시로 해커톤의 포스터를 이미지로 스캔하여 찍으면

![image](https://user-images.githubusercontent.com/81365408/152622188-223963d3-7aa8-432d-9f4a-0927ea5334e5.png)

`Flutter` 콘솔에서 변환된 텍스트를 확인할수 있으며, 첫번째 사진의 화면으로 돌아가며 현재 콘솔에 적혀있는 텍스트 그대로 음성으로 전달 합니다. 


## 성장 가능한 전략
-------------------
양질의 교육의 주제로 보자면 크게 텍스트를 읽어주는것이 대부분이라고 생각하지만 충분히 발전 가능이 있다고 생각합니다.

스마트안경이 보급화가 된다면, 시각장애인들이 안경의 버튼 혹은 음성으로 기능들을 조작하여, 내 앞에 무슨 물건이 무엇인지, 무엇이 적혀 있는지, 내 앞에 있는 사람은 어떤 표정을 하고 있는지 등을 음성으로 알려주어 조금이나 시각장애인분들이 삶의 질과 교육의 질이 향상된 삶을 만들어 줄 수 있다고 생각합니다.


## 멤버

`Flutter`- 김정현,최재원

`Django` - 지석민,김도현
