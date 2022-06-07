import streamlit as st
import pandas as pd
import random
from app_home import run_home
from app_eda import run_eda
from app_predict import run_predict
from app_recommend import run_recommend

import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
my_stopwords = stopwords.words('english')

def message_cleaning(sentence):
    # 1. 구두점 제거
    Test_punc_removed = [char for char in sentence if char not in string.punctuation]
    # 2. 각 글자들을 하나의 문자열로 합친다.
    Test_punc_removed_join = ''.join(Test_punc_removed)
    # 3. 문자열에 불용어가 포함되어 있는지 확인해서, 불용어 제거한다.
    Test_punc_removed_join_clean = [word for word in Test_punc_removed_join.split() if word.lower() not in my_stopwords]
    # 4. 결과로 남은 단어들만 리턴한다.
    return Test_punc_removed_join_clean

def main():
    st.set_page_config('아마존 리뷰 분석 및 추천 시스템')
    menu = ['Home', '분석', '감정예측', '추천'] 
    st.sidebar.header('아마존 리뷰 분석 및 추천 시스템')
    choice = st.sidebar.selectbox('메뉴 선택', menu)
    st.sidebar.subheader('상품예시')
    meta_Prime_Pantry = pd.read_csv('data/meta_Prime_Pantry.csv', index_col = 0)

    example_rand = random.randint(0, len(meta_Prime_Pantry) - 1)
    example_temp = meta_Prime_Pantry.loc[example_rand, 'imageURLHighRes'].split(',')
    if len(example_temp) == 1:
        example_index = -2
    else:
        example_index = -1
    example = example_temp[0][2:][:example_index] 
    example_address = 'https://amazon.com/dp/' + meta_Prime_Pantry.loc[example_rand, 'asin']
    st.sidebar.markdown(f'''
    <a href = "{example_address}">
        <div style ="text-align:center; width:304px; height:304px; line-height:304px;";>
            <img src="{example}" style = "max-width : 304px; max-height:304px";/>
        </div>
    <a/>
    ''',unsafe_allow_html=True)
    st.sidebar.subheader(meta_Prime_Pantry.loc[example_rand, 'title'])
    st.sidebar.text(meta_Prime_Pantry.loc[example_rand, 'price'] 
    + ' | *'
    + str(round(meta_Prime_Pantry.loc[example_rand, 'ratings'], 2)))
    
    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_predict()
    elif choice == menu[3]:
        run_recommend()

if __name__ == '__main__':
    main()