import streamlit as st
#from utils import PrepProcesor, columns 

import time
import requests


import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# load lottie animation file
import json
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

path = "/Users/sandi/Student_Dropout/graduate_lottie.json"
with open(path,"r") as file: 
    graduate_lottie = json.load(file)


model = joblib.load('model.joblib')
#scaler = model("scaler")

# -- Set page config
st.set_page_config(page_title='Student Dropout Prediction', page_icon=':student:')

# Title the app
st.title('Student Dropout Prediction :student:')
st.markdown("""
* Select parameters on the menu on the left and submit
* Prediction results and recommended actions will appear below
""")

# Enter column details
col_1, col_2, col_3 = st.columns([0.2,0.7,0.1])

#with st.sidebar.form(key='Predict & Recommend'):
st.sidebar.markdown('## Select Parameters')

# Applicationmode = st.sidebar.slider("Application Mode",1,20,1)
DaytimeEveningAttendance = st.sidebar.number_input("Attendance: 1 - yes; 0 - no",0,1)
Displaced = st.sidebar.number_input("Displaced: 1 - yes; 0 - no",0,1)
# Debtor = st.sidebar.number_input("Debtor: 1 - yes; 0 - no",0,1)
Tuitionfeesuptodate = st.sidebar.number_input("Tuition fees up to date: 1 - yes; 0 - no",0,1)
Gender = st.sidebar.number_input("Gender:1- male, 0 - female",0,1)
Scholarshipholder = st.sidebar.number_input("Scholarship Holder: 1 - yes; 0 - no",0,1)
Ageatenrollment = st.sidebar.slider("Age at Enrollment",0,70,20)
#Curricularunits1stsemenrolled = st.sidebar.slider("Curricular units 1st sem (enrolled)",0,20,5)
#Curricularunits1stsemapproved = st.sidebar.slider("Curricular units 1st sem (approved)",0,20,5)
Curricularunits1stsemgrade = st.sidebar.slider("Curricular units 1st sem (grade)",0,20,5)
#Curricularunits2ndsemenrolled = st.sidebar.slider("Curricular units 2nd sem (enrolled)",0,20,5)
#Curricularunits2ndsemapproved = st.sidebar.slider("Curricular units 2nd sem (approved)",0,20,5)
Curricularunits2ndsemgrade = st.sidebar.slider("Curricular units 2nd sem (grade)",0,20,5)

row = np.array([DaytimeEveningAttendance, Displaced, Tuitionfeesuptodate, Gender, Scholarshipholder, Ageatenrollment, 
            Curricularunits1stsemgrade, Curricularunits2ndsemgrade])
columns = ['Attendance', 'Displaced', 'Tuition fees up to date', 'Gender', 'Scholarship holder', 'Age at enrollment',
           'Curricular units 1st sem (grade)', 'Curricular units 2nd sem (grade)']  

#row_scaled = StandardScaler().fit_transform(row)

X = pd.DataFrame([row], columns = columns)
prediction = model.predict(X)[0]

def predict():
    with col_1:
        if prediction == 1: 
            st.error ('Dropout :thumbsdown:')
        else:
            st.success('Graduate :thumbsup:')
            st.balloons()
            st_lottie(graduate_lottie)


def recommend():
    if prediction != 1:
       st.markdown("""None - Keep up the good work!""")
    elif Tuitionfeesuptodate == 0 and Curricularunits2ndsemgrade <4:
        st.markdown("""Financial Assistance :finance: 
                    https://www2.ed.gov/policy/elsec/leg/essa/index.html""")
        with st.expander("See notes"):
            st.markdown(""" ​The primary purpose of Every Student Succeeds Act (ESSA) is to make sure public schools provide a quality 
                        education for all kids. ESSA also provides funding for literacy programs and other grants that can help students 
                        in poverty, minorities, students who receive special education, and students with limited English language skills 
                        succeed. It also encourages innovation in how schools teach kids.""")
        st.markdown("""Counselling Assistance :counselling:
                    https://sites.google.com/musd.org/mhs-counseling/home""")
        with st.expander("See notes"):
            st.markdown("""
                        This is an example of the School counselling site providing assitance to help students design the course 
                        curriculam for success.
                        """)
        st.markdown("""Tutoring Assistance :tutor
                    https://www.khanacademy.org/""")
        with st.expander("See notes"):
            st.markdown("""Khan Academy offers online personalized learning content created by experts, where students can practice at 
                        their own pace. It also provides tools to empower teachers to identify gaps in their students’ understanding, 
                        tailor instruction, and meet the needs of every student.
                        """)   
    elif Tuitionfeesuptodate == 0:
        st.markdown("""Financial Assistance: https://www2.ed.gov/policy/elsec/leg/essa/index.html""")
        with st.expander("See notes"):
                st.markdown(""" ​The primary purpose of Every Student Succeeds Act (ESSA) is to make sure public schools provide a quality 
                        education for all kids. ESSA also provides funding for literacy programs and other grants that can help students 
                        in poverty, minorities, students who receive special education, and students with limited English language skills 
                        succeed. It also encourages innovation in how schools teach kids.""")
# if a student curricular units enrollment drops from sem 1(>5) to sem 2 (<2)    
    elif Curricularunits1stsemgrade >5 and Curricularunits2ndsemgrade <4:
        st.markdown("""Counselling Assistance: https://sites.google.com/musd.org/mhs-counseling/home""")
        with st.expander("See notes"):
            st.markdown("""
                        This is an example of the School counselling site providing assitance to help students design the course 
                        curriculam for success.
                        """)
        st.markdown("""Tutoring Assistance: https://www.khanacademy.org/""")
        with st.expander("See notes"):
            st.markdown("""Khan Academy offers online personalized learning content created by experts, where students can practice at 
                        their own pace. It also provides tools to empower teachers to identify gaps in their students’ understanding, 
                        tailor instruction, and meet the needs of every student.
                        """)
    elif Curricularunits2ndsemgrade <4:
        st.markdown("""Counselling Assistance: https://sites.google.com/musd.org/mhs-counseling/home""")
        with st.expander("See notes"):
                st.markdown("""
                        This is an example of the School counselling site providing assitance to help students design the course 
                        curriculam for success.
                        """)
    else:
        st.markdown("Not identified")

if st.sidebar.button("Submit"):
    with col_1:
        st.subheader("Prediction", divider='blue')
        predict()
        
    with col_2:
        st.subheader("Recommendations", divider='blue')
        recommend()

with col_1:
    st.sidebar.button("Reset", st.rerun)

#with col_2:        
    # def master_callback():
    #     st.empty()
    #     title()
    #     predict()
    #     recommend()
     
#    trigger = st.sidebar.button(label = 'Predict', on_click = master_callback, help='click for dropout prediction and recommendations')
#    st.button("Re-run")