import numpy as np
import streamlit as st
import pickle
with open('models/ct.pkl','rb') as file:
    ct = pickle.load(file)
with open('models/model.pkl','rb') as file:
    model = pickle.load(file) 

st.title("Placement Prediction Using Machine Learning")

cgpa = st.number_input('Enter CGPA:')
Intern = st.number_input('Number Of Interships:')
projects = st.number_input('Number OF Projects:')
Work = st.number_input('Number Of Workshop/Certificates:')
app = st.number_input("Aptitude Test Score:")
soft = st.number_input("SoftSkillRating:")
Extra = st.selectbox("Extracurricular Activities:",['Yes','No'])
training = st.selectbox('Placement Training',['Yes','No'])
ssc = st.number_input('10th marks:')
hsc = st.number_input('12th marks:')

input_array = np.array([[cgpa,Intern,projects,Work,app,soft,Extra,training,ssc,hsc]])

if st.button('Predict'):
    input_array = ct.transform(input_array)
    pred = model.predict(input_array)
    st.text(pred.item())