# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:50:58 2024

@author: BHAVYA MITTAL 1729
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the models
diabetes_model = pickle.load(open('G:/multiplediseaseprediction/models/diabeties_model.sav', 'rb'))
heart_disease_model = pickle.load(open('G:/multiplediseaseprediction/models/heartdisease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('G:/multiplediseaseprediction/models/parkinson_model.sav', 'rb'))

# Sidebar menu for selecting prediction type
with st.sidebar:
    selected = option_menu('SEHAT',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Predictions'],
                           icons=['activity', 'heart', 'person'],
                           menu_icon='cast', default_index=0,
                           styles={
                               "container": {"padding": "5px", "background-color": "#f8f9fa"},
                               "icon": {"color": "orange", "font-size": "25px"},
                               "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                               "nav-link-selected": {"background-color": "#02ab21"},
                           })

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    st.subheader('Enter the details:')
    col1,col2,col3 = st.columns(3)
    # Input fields
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1)
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0, max_value=200, step=1)
    with col3:
        BloodPressure = st.number_input('Blood Pressure Value', min_value=0, max_value=140, step=1)
    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0, max_value=100, step=1)
    with col2:
        Insulin = st.number_input('Insulin value', min_value=0, max_value=900, step=1)
    with col3:
        BMI = st.number_input('Body Mass Index Value', min_value=0.0, max_value=70.0, step=0.1)
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value', min_value=0.0, max_value=2.5, step=0.01)
    with col2:
        Age = st.number_input('Age of person', min_value=0, max_value=120, step=1)
    
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is not Diabetic'
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    st.subheader('Enter the details:')
    col1,col2,col3 = st.columns(3)
    # Input fields
    with col1:
        age = st.number_input('Age of the person', min_value=0, max_value=120, step=1)
    with col2:
        sex = st.selectbox('Sex', [0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
    with col3:
        cp = st.number_input('Chest pain type (0-3)', min_value=0, max_value=3, step=1)
    with col1:
        trestbps = st.number_input('Resting blood pressure (in mm Hg)', min_value=0, max_value=200, step=1)
    with col2:
        chol = st.number_input('Serum cholesterol in mg/dl', min_value=0, max_value=600, step=1)
    with col3:
        fbs = st.selectbox('Fasting blood sugar > 120 mg/dl', [0, 1], format_func=lambda x: 'False' if x == 0 else 'True')
    with col1:
        restecg = st.number_input('Resting electrocardiographic results (0-2)', min_value=0, max_value=2, step=1)
    with col2:
        thalach = st.number_input('Maximum heart rate achieved', min_value=0, max_value=220, step=1)
    with col3:
        exang = st.selectbox('Exercise induced angina', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise relative to rest', min_value=0.0, max_value=10.0, step=0.1)
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment (0-2)', min_value=0, max_value=2, step=1)
    with col3:
        ca = st.number_input('Number of major vessels (0-3) colored by fluoroscopy', min_value=0, max_value=3, step=1)
    with col1:
        thal = st.selectbox('Thalassemia', [1, 2, 3], format_func=lambda x: 'Normal' if x == 1 else 'Fixed defect' if x == 2 else 'Reversable defect')
    
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        heart_prediction = heart_disease_model.predict([input_data])
        
        if heart_prediction[0] == 0:
            heart_diagnosis = 'The Person is likely to have a healthy heart.'
        else:
            heart_diagnosis = 'The Person is likely to have heart disease.'
    st.success(heart_diagnosis)

# Parkinson's Predictions Page
if selected == 'Parkinsons Predictions':
    st.title('Parkinson\'s Prediction using ML')
    st.subheader('Enter the details:')
    col1,col2,col3 = st.columns(3)
    # Input fields for Parkinson's prediction
    with col1:
        fo = st.number_input('MDVP:Fo (Hz) - Average vocal fundamental frequency', min_value=0.0, max_value=300.0, step=0.1)
    with col2:
        fhi = st.number_input('MDVP:Fhi (Hz) - Maximum vocal fundamental frequency', min_value=0.0, max_value=300.0, step=0.1)
    with col3:
        flo = st.number_input('MDVP:Flo (Hz) - Minimum vocal fundamental frequency', min_value=0.0, max_value=300.0, step=0.1)
    with col1:
        jitter_percent = st.number_input('MDVP Jitter (%)', min_value=0.0, max_value=1.0, step=0.01)
    with col2:
        jitter_abs = st.number_input('MDVP Jitter (Abs)', min_value=0.0, max_value=0.1, step=0.001)
    with col3:
        rap = st.number_input('MDVP RAP', min_value=0.0, max_value=1.0, step=0.01)
    with col1:
        ppq = st.number_input('MDVP PPQ', min_value=0.0, max_value=1.0, step=0.01)
    with col2:
        ddp = st.number_input('Jitter DDP', min_value=0.0, max_value=1.0, step=0.01)
    with col3:
        shimmer = st.number_input('MDVP Shimmer', min_value=0.0, max_value=1.0, step=0.01)
    with col1:
        shimmer_db = st.number_input('MDVP Shimmer (dB)', min_value=0.0, max_value=1.0, step=0.01)
    with col2:
        apq3 = st.number_input('Shimmer APQ3', min_value=0.0, max_value=1.0, step=0.01)
    with col3:
        apq5 = st.number_input('Shimmer APQ5', min_value=0.0, max_value=1.0, step=0.01)
    with col1:
        apq = st.number_input('MDVP APQ', min_value=0.0, max_value=1.0, step=0.01)
    with col2:
        dda = st.number_input('Shimmer DDA', min_value=0.0, max_value=1.0, step=0.01)
    with col3:
        nhr = st.number_input('NHR', min_value=0.0, max_value=1.0, step=0.01)
    with col1:
        hnr = st.number_input('HNR', min_value=0.0, max_value=50.0, step=0.1)
    with col2:
        rpde = st.number_input('RPDE', min_value=0.0, max_value=1.0, step=0.01)
    with col3:
        dfa = st.number_input('DFA', min_value=0.0, max_value=1.0, step=0.01)
    with col1:
        spread1 = st.number_input('Spread1', min_value=-10.0, max_value=10.0, step=0.1)
    with col2:
        spread2 = st.number_input('Spread2', min_value=-10.0, max_value=10.0, step=0.1)
    with col3:
        d2 = st.number_input('D2', min_value=0.0, max_value=10.0, step=0.1)
    with col1:
        ppe = st.number_input('PPE', min_value=0.0, max_value=1.0, step=0.01)
    
    parkinsons_diagnosis = ''
    
    if st.button('Parkinson\'s Disease Test Result'):
        try:
            # Convert inputs to appropriate numeric types
            input_data = [
                float(fo), float(fhi), float(flo), float(jitter_percent), float(jitter_abs), 
                float(rap), float(ppq), float(ddp), float(shimmer), float(shimmer_db), 
                float(apq3), float(apq5), float(apq), float(dda), float(nhr), 
                float(hnr), float(rpde), float(dfa), float(spread1), float(spread2), 
                float(d2), float(ppe)
            ]
            # Reshape input data as model expects a 2D array
            input_data = [input_data]
            
            # Make prediction
            parkinsons_prediction = parkinsons_model.predict(input_data)
            
            # Display result
            if parkinsons_prediction[0] == 0:
                parkinsons_diagnosis = 'The Person is not likely to have Parkinson\'s disease.'
            else:
                parkinsons_diagnosis = 'The Person is likely to have Parkinson\'s disease.'
        
        except ValueError:
            st.error('Please enter valid numeric values for all fields.')
    
    st.success(parkinsons_diagnosis)
