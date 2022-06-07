import streamlit as st
import pandas as pd
import plotly.express as px

def run_eda():
    Prime_Pantry_Review = pd.read_csv('data/Prime_Pantry_Review.csv', index_col = 0)
    meta_Prime_Pantry = pd.read_csv('data/meta_Prime_Pantry.csv', index_col = 0)

    st.subheader('별점 분포')
    fig = px.histogram(Prime_Pantry_Review, x = 'overall')
    st.plotly_chart(fig)

    st.subheader('인증된 사용자')
    fig = px.histogram(Prime_Pantry_Review, x = 'verified')
    st.plotly_chart(fig)


    ratings = Prime_Pantry_Review.groupby('asin').mean('overall')['overall']
    counts = Prime_Pantry_Review.groupby('asin').count()['overall']
    ratings_counts = pd.concat([ratings, counts], axis = 1)
    ratings_counts.columns = ['ratings', 'overall']
    ratings_counts_sort = ratings_counts.loc[ratings_counts['overall']> 100].sort_values(by = 'ratings', ascending = False)
    top5_asin = list(ratings_counts_sort.index[:5])
    bottom5_asin = list(ratings_counts_sort.index[-5:])

    st.subheader('상품검색')
    goods_text = st.text_input('입력', 'hershey').lower()
    st.dataframe(meta_Prime_Pantry.loc[meta_Prime_Pantry['title'].str.lower().str.contains(goods_text)])

    st.subheader('별점이 높은순 상품 5개 (100명이상 리뷰)')
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            asin = top5_asin[i]
            temp = meta_Prime_Pantry.loc[meta_Prime_Pantry['asin'] == asin].iloc[0]
            temp_image = temp['imageURLHighRes'].split(',')
            if len(temp_image) == 1:
                temp_index = -2
            else:
                temp_index = -1
            example_address = 'https://amazon.com/dp/' + asin
            st.markdown(f'''
            <a href = "{example_address}">
                <div style ="text-align:center; width:128px; height:128px; line-height:128px;";>
                    <img src="{temp['imageURLHighRes'].split(',')[0][2:][:temp_index]}" style = "max-width : 128px; max-height:128px";/>
                </div>
            <a/>
            ''',unsafe_allow_html=True)
            st.text(temp['title'])
            st.text(temp['price'] + ' | *' + str(round(temp['ratings'],2)))
    
    st.subheader('별점이 낮은순 상품 5개 (100명이상 리뷰)')
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            asin = bottom5_asin[4 - i]
            temp = meta_Prime_Pantry.loc[meta_Prime_Pantry['asin'] == asin].iloc[0]
            temp_image = temp['imageURLHighRes'].split(',')
            if len(temp_image) == 1:
                temp_index = -2
            else:
                temp_index = -1
            example_address = 'https://amazon.com/dp/' + asin
            st.markdown(f'''
            <a href = "{example_address}">
                <div style ="text-align:center; width:128px; height:128px; line-height:128px;";>
                    <img src="{temp['imageURLHighRes'].split(',')[0][2:][:temp_index]}" style = "max-width : 128px; max-height:128px";/>
                </div>
            <a/>
            ''',unsafe_allow_html=True)
            st.text(temp['title'])
            st.text(temp['price'] + ' | *' + str(round(temp['ratings'],2)))