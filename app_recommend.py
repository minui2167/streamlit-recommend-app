import streamlit as st
import joblib
import numpy as np

def run_recommend():
    vec = joblib.load('data/vec.pkl')
    classifier = joblib.load('data/classifier.pkl')
    new_data = np.array(['amazing food! highly recommmended', 'shit food, made me sick'])
    X_new = vec.transform(new_data)
    st.text(classifier.predict(X_new))