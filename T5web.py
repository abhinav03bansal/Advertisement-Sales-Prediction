import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('sales.sav','rb'))
st.title("Welcome to Sales Prediction")
TV=st.number_input("TV")
Radio=st.number_input("Radio")
Newspaper=st.number_input("Newspaper")
btn=st.button("Predict")
if btn:
    pred=model.predict([[TV,Radio,Newspaper]])[0]
    print(pred)

    st.subheader(pred)