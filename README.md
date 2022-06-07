# streamlit-recommend-app
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![streamlit](https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png)

아마존 리뷰 분석과 감정 예측, 상품 추천하는 앱입니다.

[http://ec2-3-35-26-163.ap-northeast-2.compute.amazonaws.com:8504/](http://ec2-3-35-26-163.ap-northeast-2.compute.amazonaws.com:8504/)

![dd](https://media-cldnry.s-nbcnews.com/image/upload/newscms/2020_38/3412555/amazon-prime-day-history-kr-2x1-tease-200916.jpg)

# 분석

* plotly를 통해서 시각화 
* groupby를 통해서 가장 높은 별점과 낮은 별점 분석 

# 감정 예측

* CountVectorizer로 텍스트 전처리
* MultinomialNB로 감정 예측

# 추천 시스템

* pivot 테이블로 filltering
* item-based collaorative filltering을 통해서 상품 추천
