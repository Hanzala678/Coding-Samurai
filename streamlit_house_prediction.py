# -*- coding: utf-8 -*-
"""
Created on Sat Oct 02 02:20:31 2023

@author: Syed Hanzala Ali
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 02 02:20:31 2023

@author: Syed Hanzala Ali
"""


import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("random_forest_model.pkl","rb")
regressor=pickle.load(pickle_in)

def welcome():
    return "Welcome All"


def predict_note_authentication(Zip, Area, Room):

   
    prediction=regressor.predict([[Zip, Area, Room]])
    price = int(prediction[0])
    return f'{price:,} Euros'


def main():
    st.title("House Price Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">House Price Estimator </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    options = [1, 2,3,4,5,6,7,8,9,10,11,12,13,14]
    Room = st.selectbox('Select No of Rooms', options)
   #precip = st.text_input("Precip Type","Type Here")
    Area = st.text_input("Enter Area (in sq feet)",placeholder="Type Here")
    Zip = st.text_input("Enter Zip code",placeholder="Type Here")

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Zip, Area, Room)
    st.success('The price of this house is {}'.format(result))
    if st.button("About"):
        st.text("This app is created as a task for Coding Samurai")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
