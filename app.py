from flask import Flask,request,jsonify
import pickle
import pandas as pd
import numpy as np
import sklearn
import streamlit as st
import re

data = pd.read_csv('GlobalLandTemperaturesByMajorCity.csv')
data['Latitude_value']=data['Latitude']
data['Longitude_value'] = data['Longitude']
data['Latitude_value'] = data['Latitude_value'].apply(lambda x: re.sub(r'[^0-9.-]', '', x))
data['Latitude_value'] = data['Latitude_value'].astype(float)

data['Longitude_value'] = data['Longitude_value'].apply(lambda x: re.sub(r'[^0-9.-]', '', x))
data['Longitude_value'] = data['Longitude_value'].astype(float)


# Create a Streamlit app
st.title("Integer Field Example")


model = pickle.load(open('globle_temp.pkl', 'rb'))


year_number = list(range(1849,2014))
month_numbers = list(range(1, 13))
day_number = list(range(1,32))
Latitude_value_array = data['Latitude_value'].unique()
Longitude_value_array = data['Longitude_value'].unique()


Latitude_value_selected = st.selectbox("Select an Latitude value", Latitude_value_array)
Longitude_value_selected = st.selectbox("Select an Longitude value", Longitude_value_array)
year = st.selectbox("Select year value", year_number)
month = st.selectbox("Select month value", month_numbers)
day = st.selectbox("Select day value",day_number)
Latitude_direction = st.selectbox("Select Latitude direction", ["N", "S"])
Longitude_direction = st.selectbox("Select Longitude direction", ["W", "E"])

Latitude_direction_numric = None
Longitude_direction_numric = None

if(Latitude_direction=="N"):
    Latitude_direction_numric=0
elif(Latitude_direction == "S"):
    Latitude_direction_numric=1

if(Longitude_direction == "E"):
    Longitude_direction_numric = 0
elif(Longitude_direction == "W"):
    Longitude_direction_numric= 1

data = np.array([[Latitude_value_selected, Longitude_value_selected, year, month, day, Latitude_direction_numric,Longitude_direction_numric]])

result = model.predict(data)[0]

result_list =result.tolist()

#return jsonify({'Temperature in your area': result_list})
if st.button("Submit"):
    # Display the selected gender
    st.write("Temperature in your area:", result_list)
