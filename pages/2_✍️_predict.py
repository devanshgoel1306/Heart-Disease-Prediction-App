import streamlit as st
import pandas as pd
#for using the saved model
import joblib

st.title('Heart Disease Prediction.')

age= st.text_input("Age")
bp= st.text_input("Resting Blood Pressure")
chol= st.text_input("Cholesterol")
hr= st.text_input("Maximum Heart Rate")
peak= st.text_input("Old Peak")

bs= st.radio("Fasting Blood Sugar",[0,1])
gender= st.radio("Gender",['Male','Female'])
pain= st.radio("Chest Pain Type",['Atypical Angina','Non Anginal','Asymptomatic','Typical Angina'])
ecg= st.radio("Resting ECG",['Normal','Left ventricular hypertrophy(LVH)','ST-T wave Abnormal'])
angina= st.radio("Excercise Angina",['Yes','No'])
slope= st.radio("ST slope",['Up','Flat'])

#change the value of variables
#according to our need
if gender == 'Male': gender= 1  
else: gender= 0
        
if pain == 'Atypical Angina': pain= [1,0,0]
elif pain == 'Non Anginal': pain= [0,1,0]
elif pain == 'Asymptomatic': pain= [0,0,1]
else: pain= [0,0,0]
        
if ecg == 'Left ventricular hypertrophy(LVH)': ecg= [0,0]
elif ecg == 'Normal': ecg= [1,0]
elif ecg == 'ST-T wave Abnormal': ecg= [0,1]

if angina == 'Yes': angina= 1
else: angina= 0
        
if slope == 'Flat': slope= [1,0]
else: slope= [0,1]

#adding a button
if st.button('Predict'):
    data= {'Age':int(age),'RestingBP':int(bp),'Cholesterol':int(chol),'FastingBS':int(bs), 'MaxHR':int(hr), 
    'Oldpeak':float(peak),'Sex_M':gender, 'ChestPainType_ATA':pain[0], 'ChestPainType_NAP':pain[1], 
    'ChestPainType_TA':pain[2], 'RestingECG_Normal':ecg[0], 'RestingECG_ST':ecg[1], 'ExerciseAngina_Y':angina,
    'ST_Slope_Flat':slope[0], 'ST_Slope_Up':slope[1]}

    df= pd.DataFrame(data,index=[0])

    #filename of model
    model_name= 'heart_model.sav'

    #load the model
    model= joblib.load(model_name)
        
    predicted= model.predict(df)
        
    if predicted == 0:
        st.success('This person has very less chances of Heart Attack.')
    else:
        st.warning('This person has high chances of Heart Attack.')


