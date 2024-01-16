import streamlit as st
#from utils import PrepProcesor, columns 

import numpy as np
import pandas as pd
import joblib

model = joblib.load('model.joblib')

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
Displaced = st.sidebar.number_input("Displaced: 1 - yes; 0 - no",0,1)
# Debtor = st.sidebar.number_input("Debtor: 1 - yes; 0 - no",0,1)
Tuitionfeesuptodate = st.sidebar.number_input("Tuition fees up to date: 1 - yes; 0 - no",0,1)
# Gender = st.sidebar.number_input("Gender:1- male, 0 - female",0,1)
Scholarshipholder = st.sidebar.number_input("Scholarship Holder: 1 - yes; 0 - no",0,1)
Ageatenrollment = st.sidebar.slider("Age at Enrollment",0,70,20)
Curricularunits1stsemenrolled = st.sidebar.slider("Curricular units 1st sem (enrolled)",0,20,5)
Curricularunits1stsemapproved = st.sidebar.slider("Curricular units 1st sem (approved)",0,20,5)
Curricularunits1stsemgrade = st.sidebar.slider("Curricular units 1st sem (grade)",0,20,5)
Curricularunits2ndsemenrolled = st.sidebar.slider("Curricular units 2nd sem (enrolled)",0,20,5)
Curricularunits2ndsemapproved = st.sidebar.slider("Curricular units 2nd sem (approved)",0,20,5)
Curricularunits2ndsemgrade = st.sidebar.slider("Curricular units 2nd sem (grade)",0,20,5)
    

row = np.array([Displaced, Tuitionfeesuptodate, Scholarshipholder, Ageatenrollment, 
            Curricularunits1stsemenrolled, Curricularunits1stsemapproved, Curricularunits1stsemgrade, 
            Curricularunits2ndsemenrolled, Curricularunits2ndsemapproved, Curricularunits2ndsemgrade])
columns = ['Displaced', 'Tuition fees up to date', 'Scholarship holder', 'Age at enrollment',
        'Curricular units 1st sem (enrolled)', 'Curricular units 1st sem (approved)', 'Curricular units 1st sem (grade)',
        'Curricular units 2nd sem (enrolled)', 'Curricular units 2nd sem (approved)', 'Curricular units 2nd sem (grade)']  
X = pd.DataFrame([row], columns = columns)
prediction = model.predict(X)[0]

def predict():
    with col_1:
        if prediction == 0: 
            st.error ('Dropout :thumbsdown:')
        elif prediction == 1:
            st.success('Enrolled :thumbsup:') 
        else:
            st.success('Graduate :thumbsup:')


def recommend():
    if prediction != 0:
       st.markdown("""None - Keep up the good work!""")
    elif Tuitionfeesuptodate == 0 and Curricularunits2ndsemenrolled < 5:
        st.markdown("""Financial Assistance: https://www.khanacademy.org/""")
        with st.expander("See notes"):
            st.markdown("""
                        This is a placeholder for "See notes" info
                        """)
        st.markdown("""Counselling: https://www.khanacademy.org/""")
        with st.expander("See notes"):
            st.markdown("""
                        This is a placeholder for "See notes" info
                        """)
        st.markdown("""Tutoring: https://www.khanacademy.org/""")
        with st.expander("See notes"):
            st.markdown("""
                        This is a placeholder for "See notes" info
                        """)   
    elif Tuitionfeesuptodate == 0:
        st.markdown("""Financial Assistance: https://www.khanacademy.org/""")
        with st.expander("See notes"):
                st.markdown("""This is a placeholder for "See notes" info""")
# if a student curricular units enrollment drops from sem 1(>5) to sem 2 (<2)    
    elif Curricularunits1stsemenrolled >5 and Curricularunits2ndsemenrolled <2:
        st.markdown("""Counselling: https://www.khanacademy.org/""")
        with st.expander("See notes"):
            st.markdown("""
                        This is a placeholder for "See notes" info
                        """)
        st.markdown("""Tutoring: https://www.khanacademy.org/""")
        with st.expander("See notes"):
            st.markdown("""
                        This is a placeholder for "See notes" info
                        """)
    elif Curricularunits2ndsemenrolled <5:
        st.markdown("""Counselling: https://www.khanacademy.org/""")
        with st.expander("See notes"):
                st.markdown("""
                        This is a placeholder for "See notes" info
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