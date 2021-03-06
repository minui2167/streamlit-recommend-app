import streamlit as st
import pandas as pd
import plotly.express as px

def run_eda():
    # 데이터 불러오기
    meta_Prime_Pantry = pd.read_csv('data/meta_Prime_Pantry.csv', index_col = 0)

    # 별점 분포 그래프
    st.subheader('별점 분포')
    st.image('data/overall.png')

    # 인증된 사용자 그래프
    st.subheader('인증된 사용자')
    st.image('data/verified.png')

    # 가격 분포
    st.subheader('가격대')
    fig = px.histogram(meta_Prime_Pantry, x = meta_Prime_Pantry['price'].str[1:].astype(float), nbins = 100, labels = {'x':'price'})
    st.plotly_chart(fig)

    # 별점 평균과 리뷰 개수를 구해서 100개 이상의 리뷰가 달린 제품중 별점 높은순 5개 낮은순 5개 구하기
    top5_asin = ['B00TDEDS7Q', 'B000VKA1SA', 'B012XBZLNY', 'B00P6EQW6G', 'B00OZENQK8']
    bottom5_asin = ['B00UB6ZL0W', 'B00VWH5SSO', 'B00QJGVTGS', 'B00QJGW1OC', 'B016F7GMV2']
    
    # 문자열을 포함하는 상품 검색
    st.subheader('상품검색')
    goods_text = st.text_input('입력', 'hershey').lower()
    st.dataframe(meta_Prime_Pantry.loc[meta_Prime_Pantry['title'].str.lower().str.contains(goods_text)])

    # 높은순 5개 출력
    st.title('')
    st.subheader('별점이 높은순 상품 5개 (100명이상 리뷰)')
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            # 식별번호
            asin = top5_asin[i]

            # 이미지 url 분리
            temp = meta_Prime_Pantry.loc[meta_Prime_Pantry['asin'] == asin].iloc[0]
            temp_image = temp['imageURLHighRes'].split(',')
            if len(temp_image) == 1:
                temp_index = -2
            else:
                temp_index = -1
            
            # 제품 페이지
            example_address = 'https://amazon.com/dp/' + asin

            # 제품 출력
            st.markdown(f'''
            <a href = "{example_address}">
                <div style ="text-align:center; width:128px; height:128px; line-height:128px;";>
                    <img src="{temp['imageURLHighRes'].split(',')[0][2:][:temp_index]}" style = "max-width : 128px; max-height:128px";/>
                </div>
            <a/>
            ''',unsafe_allow_html=True)
            st.text(temp['title'])
            st.text(temp['price'] + ' | *' + str(round(temp['ratings'],2)))
    
    # 낮은순 5개 출력
    st.title('')
    st.subheader('별점이 낮은순 상품 5개 (100명이상 리뷰)')
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            # 식별번호
            asin = bottom5_asin[4 - i]

            # 이미지 url 분리
            temp = meta_Prime_Pantry.loc[meta_Prime_Pantry['asin'] == asin].iloc[0]
            temp_image = temp['imageURLHighRes'].split(',')
            if len(temp_image) == 1:
                temp_index = -2
            else:
                temp_index = -1

            # 제품 페이지
            example_address = 'https://amazon.com/dp/' + asin

            # 제품 출력
            st.markdown(f'''
            <a href = "{example_address}">
                <div style ="text-align:center; width:128px; height:128px; line-height:128px;";>
                    <img src="{temp['imageURLHighRes'].split(',')[0][2:][:temp_index]}" style = "max-width : 128px; max-height:128px";/>
                </div>
            <a/>
            ''',unsafe_allow_html=True)
            st.text(temp['title'])
            st.text(temp['price'] + ' | *' + str(round(temp['ratings'],2)))