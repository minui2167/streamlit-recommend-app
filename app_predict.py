import streamlit as st
import numpy as np
import joblib 

def run_predict():
    # 제목
    st.subheader('리뷰 긍정 부정 예측하기')
    st.info('리뷰 텍스트와 별점을 학습한 인공지능이 긍정 부정을 예측합니다.')

    # 입력 받기
    sentence = st.text_input('문장 입력')

    # 유저가 버튼을 누르면, 에측하도록 만든다.
    if st.button('예측 실행'):
        
        # 분류모델과 전처리 모델들 불러오고 전처리후 분류
        classifier = joblib.load('data/classifier.pkl')
        vec = joblib.load('data/vec.pkl')
        new_data = np.array([sentence])
        X_new =vec.transform(new_data)
        X_new = X_new.toarray()
        y_pred = classifier.predict(X_new)
        
        if y_pred[0]  == 5:
            st.subheader('입력하신 문장은 긍정입니다.')
        else:
            st.subheader('입력하신 문장은 부정입니다.')