import streamlit as st
import pandas as pd

def run_search():
    Prime_Pantry_Review = pd.read_csv('data/Prime_Pantry_Review.csv', index_col = 0)
    meta_Prime_Pantry = pd.read_csv('data/meta_Prime_Pantry.csv', index_col = 0)