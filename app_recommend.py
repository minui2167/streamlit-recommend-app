import streamlit as st
import pandas as pd

def run_recommend():
    st.subheader('사용자 기반 상품 추천')
    sentence = st.text_input('단어를 입력하면 단어가 포함된 상품을 기반으로 추천합니다.').lower()

    if st.button('추천 실행'):
        try:  
            print(0)
            corr = pd.read_csv('data/corr.csv')
            print(55)
            meta_Prime_Pantry = pd.read_csv('data/meta_Prime_Pantry.csv')
            item_input = meta_Prime_Pantry.loc[meta_Prime_Pantry['title'].str.lower().str.contains(sentence)].sort_values(by = 'ratings', ascending = False).iloc[0]['asin']            
            recommend_asin = corr['asin'][corr[item_input].sort_values(ascending = False).index[:5]]
            print(111)
            col1, col2, col3, col4, col5 = st.columns(5)
            cols = [col1, col2, col3, col4, col5]

            for i in range(5):
                with cols[i]:
                    print(i)
                    asin = recommend_asin.iloc[i]
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
        except:
            st.subheader('리뷰가 적거나 상품이 없습니다.')
    