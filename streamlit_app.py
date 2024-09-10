import streamlit as st
import pandas as pd


st.title('Machine Leaning app')

st.info("This is machine learnig app")

df = pd.read_csv("iris.csv")
