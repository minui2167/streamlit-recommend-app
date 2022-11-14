# streamlit-recommend-app
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

아마존 리뷰의 별점과 상품정보 분석하고

별점을 기반으로 리뷰 텍스트의 감정을 예측하고

상품을 입력하면 추천 상품을 출력해주는 앱입니다.

[http://ec2-3-34-50-142.ap-northeast-2.compute.amazonaws.com:8503/](http://ec2-3-34-50-142.ap-northeast-2.compute.amazonaws.com:8503/)

데이터 출처 [https://nijianmo.github.io/amazon/index.html](https://nijianmo.github.io/amazon/index.html)

![dd](https://media-cldnry.s-nbcnews.com/image/upload/newscms/2020_38/3412555/amazon-prime-day-history-kr-2x1-tease-200916.jpg)

# 데이터셋
* overall 별점
* verified 인증 여부
* reviewerID 리뷰어 id
* asin 상품 식별 번호
* title 상품 이름
* price 가격
* imageURLHighRes 이미지 url
* ratings 별점 평균

# 분석

* plotly를 통해서 별점, 인증 여부, 가격대 분포 시각화
* histogram 시각화
* groupby를 통해서 가장 높은 별점과 낮은 별점 분석 
* str.contains로 단어를 포함하는 상품 검색 기능

# 감정 예측

* 구두점, 불용어 처리
* CountVectorizer로 텍스트 전처리
* RandomUnderSampler로 클래스 불균형 맞추고
* MultinomialNB로 리뷰의 긍정 부정 예측

![다운로드 (4)](https://user-images.githubusercontent.com/105832345/173176227-acdb4f6e-e218-4259-860c-42fdb0932d89.png)

# 추천 시스템

* pivot 테이블로 filltering
* item-based collaorative filltering을 통해서 상품끼리 상관관계 구함
* 각 상품에 대해 상관관계가 높은 5개 상품만 저장
* 상품을 입력하면 추천 상품 출력
