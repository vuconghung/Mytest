# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:02:35 2024

@author: ADMIN
"""

import streamlit as st
import pickle
import pandas as pd
import os



def dudoan(param):  
    # load mô hình
    filename=os.getcwd()+'\\Downloads\model_house.sav'
    st.write(filename)
    loaded_model = pickle.load(open(filename,'rb')) 
    y_pred=loaded_model.predict(param)
    return y_pred

st.title("Ứng dụng Streamlit dự đoán")
st.write("test")
st.write(os.getcwd())
SquareFeet=st.number_input("Input SquareFeet:",2000)
Bedrooms=st.number_input("Input Beedrooms:",6)
Bathrooms=st.number_input("Bathrooms:",3)
Neighborhood= st.selectbox(
    "Select Neighborhood:",
    ("Rural", "Suburb", "Urban"),
    index=0,
    placeholder="Select...",
    )

YearBuilt=st.number_input("Input YearBuilt",5) 

if st.button('Dự đoán'):
    if(Neighborhood=="Rural"):
        Rural=1
        Suburb=0
        Urban=0
    elif (Neighborhood=="Suburb"):
        Rural=0
        Suburb=1
        Urban=0
    else:
        Rural=0
        Suburb=0
        Urban=1
    param=pd.DataFrame([[SquareFeet,Bedrooms,Bathrooms,Rural,Suburb,Urban,YearBuilt]])
    st.write(param)
    output_value = dudoan(param)
    st.write("Giá trị đầu ra dự đoán:", output_value)