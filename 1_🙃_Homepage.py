import streamlit as st
#for adding navigation bar
from streamlit_option_menu import option_menu

#giving title
st.title('About Heart Disease')
st.image('Capture.jpg', width= 700)

st.write('''The heart is a fist-sized organ that pumps blood throughout your body. It's the primary organ of your
circulatory system.

Your heart contains four main sections (chambers) made of muscle and powered by electrical impulses. Your brain and
nervous system direct your heart’s function.

Your heart’s main function is to move blood throughout your body. Your heart also:\n
-Controls the rhythm and speed of your heart rate.\n
-Maintains your blood pressure.
''')

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
    
