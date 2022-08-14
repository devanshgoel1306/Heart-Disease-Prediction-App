import streamlit as st
#for adding navigation bar
from streamlit_option_menu import option_menu
#for using the saved model
import joblib
import pandas as pd


#giving title
st.title('Heart Disease Predictor')

#adding navigation bar
with st.sidebar:
    choice= option_menu(
        menu_title="Main Menu",
        options=['About','Predict','Other info']
    )

if choice=='About':
    st.image('Capture.jpg', width= 700)
    st.subheader('Types of Cardio Vascular Diseases(CVDs)')

    #We have used True to activate the markdown syntax.
    st.markdown('''
    ##### 1.Heart Failure
            Blockage in blood flow to the heart\n
    ##### 2.Strokes
          Blockage in blood flow to the brain''', True)

    st.subheader('Causes of CVDS')
    #we could have used text function also.
    #But, it will not adjust the text according to the page.
    st.markdown('''
    ##### 1.High Blood Pressure
            If a person's bp is high it can damage blood vessels.\n
    ##### 2.Smoking
            The harmful substances in tobacco narrows the blood vessels.\n
    ##### 3.High Cholestrol
            It narrows the blood vessels and increase the risk of blood clot in vessel.''')

    st.subheader('Ways to avoid CVDS')
    st.markdown('''
    1. Stop Smoking\n
    2. Have a balanced diet\n
    3. Do Yoga regularly- Specific pranayams for CVDS are Bhastrika, kapalbhati, bahya.''')
    st.video('https://www.youtube.com/watch?v=wrECGnoJPLg')

elif choice=='Predict':
    age= st.text_input("Age")
    bp= st.text_input("Resting Blood Pressure")
    chol= st.text_input("Cholesterol")
    hr= st.text_input("Maximum Heart Rate")
    peak= st.text_input("Old Peak")

    bs= st.radio("Fasting Blood Sugar",[0,1])
    gender= st.radio("Gender",['Male','Female'])
    pain= st.radio("Chest Pain Type",['Atypical Angina','Non Anginal','Asymptomatic','Typical Angina'])
    ecg= st.radio("Resting ECG",['Normal','Left ventricular hypertrophy(LVH)','ST-T wave Abnormal'])
    angina= st.radio("Angina",['Yes','No'])
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
            st.success('This person has less chance of Heart Attack.')
        else:
            st.warning('This person has high chances of Heart Attack.')

else:
    st.subheader('Resting Blood Pressure')
    st.write('''Blood Pressure is the pressure of the blood within the arteries. It is produced primarily by the contraction 
    of the heart muscle. Its measurement is recorded by two numbers. The first(systolic pressure) is measured after the heart 
    contracts and is highest. The second(diastolic pressure) is measured before the heart contracts and is the lowest. 
    A blood pressure cuff is used to measure the pressure. Elevation of blood pressure is called 'hypertension'. 
    BP below 120/80 mm Hg is considered to be normal.''')

    st.subheader('Cholestrol')
    st.write('''A waxy type of fat, or lipid, which moves throughout your body in your blood. Lipids are substances that do 
    not dissolve in water, so they do not come apart in blood. Your body makes cholestrol, but you can also get it from foods. 
    Cholestrol is only found in foods that come from animals. Total cholestrol levels less than 200 milligrams per 
    deciliter(mg/dL) are considered for adults.''')

    st.subheader('Fasting Blood Sugar Test')
    st.markdown('''This measures your blood sugar after an overnight fast(not eating).<br> 1: if fastingBS > 120 mg/dl, <br>0: other wise''',True)

    st.subheader('Resting ECG')
    st.write('''The resting electrocardiogram is a test that measures the electrical activity of the heart. The heart is a 
    muscular organ which pumps blood through rhythmic contractions induced by electric impulses generated by the sinus node, 
    the heart's natural pacemaker.''')

    st.subheader('Chest Pain Type')
    st.write('''Typical (classic) angina(TA) chest pain consists of 
\n(1) Substernal chest pain or discomfort that is 
\n(2) Provoked by exertion or emotional stress and 
\n(3) relieved by rest or nitroglycerine (or both). 
\n
\n-Atypical (probable) angina(ATA) chest pain applies when 2 out of 3 criteria of classic angina are present.
\n
\n-Non-Anginal Pain(NAP)- A chest pain is very likely nonanginal if its duration is over 30 minutes or less than 5 seconds, it increases with inspiration, can be brought on with one movement of the trunk or arm, can be brought on by local fingers pressure, or bending forward, or it can be relieved immediately on lying down.
\n
\n-Asymptotic Pain(ASY)- Heart Attack which have no signs 
    ''')
