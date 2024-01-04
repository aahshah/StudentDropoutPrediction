import streamlit as st
#from utils import PrepProcesor, columns 

import numpy as np
import pandas as pd
import joblib

model = joblib.load('model.joblib')

st.title('Student Dropout Prediction :student:')


# Enter column details
Applicationmode = st.slider("Application Mode",1,100)
Displaced = st.number_input("Displaced: 1 – yes; 0 – no",0,1)
Debtor = st.number_input("Debtor: 1 – yes; 0 – no",0,1)
Tuitionfeesuptodate = st.number_input("Tuition fees up to date: 1 – yes; 0 – no",0,1)
Gender = st.number_input("Gender:1- male,0 - female",0,1)
Scholarshipholder = st.number_input("Scholarship Holder: 1 – yes; 0 – no",0,1)
Ageatenrollment = st.slider("Age at Enrollment",0,100)
Curricularunits1stsemenrolled = st.slider("Curricular units 1st sem (enrolled)",0,30)
Curricularunits1stsemapproved = st.slider("Curricular units 1st sem (approved)",0,30)
Curricularunits1stsemgrade = st.slider("Curricular units 1st sem (grade)",0,30)
Curricularunits2ndsemenrolled = st.slider("Curricular units 2nd sem (enrolled)",0,30)
Curricularunits2ndsemapproved = st.slider("Curricular units 2nd sem (approved)",0,30)
Curricularunits2ndsemgrade = st.slider("Curricular units 2nd sem (grade)",0,30)

def predict(): 
    row = np.array([Applicationmode, Displaced, Debtor, Tuitionfeesuptodate, Gender, Scholarshipholder, Ageatenrollment, 
                   Curricularunits1stsemenrolled, Curricularunits1stsemapproved, Curricularunits1stsemgrade, 
                   Curricularunits2ndsemenrolled, Curricularunits2ndsemapproved, Curricularunits2ndsemgrade])
    columns = ['Application mode', 'Displaced', 'Debtor', 'Tuition fees up to date', 'Gender', 'Scholarship holder', 'Age at enrollment',
               'Curricular units 1st sem (enrolled)', 'Curricular units 1st sem (approved)', 'Curricular units 1st sem (grade)',
               'Curricular units 2nd sem (enrolled)', 'Curricular units 2nd sem (approved)', 'Curricular units 2nd sem (grade)']  
    X = pd.DataFrame([row], columns = columns)
    prediction = model_lr.predict(X)[0]
    if prediction == 0: 
        st.error ('Dropout :thumbsdown:')
    elif prediction == 1:
        st.success('Enrolled :thumbsup:') 
    else:
        st.success('Graduate :thumbsup:')
 
trigger = st.button('Predict', on_click = predict)

