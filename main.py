import streamlit as st
import pickle
import pandas as pd 
PAGE_CONFIG={"page_title":"Health Insurance Amount Prediction","page_icon":"icon.png","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)
#st.title("Health Insurance Amount Prediction")
placed = pickle.load(open('ai.pkl', 'rb'))

def pred(age, gender, bmi, children, smoke, reg):
    prediction = placed.predict([[age, gender, bmi, children, smoke, reg]])
    prediction=float((prediction*(float(62648.55411)))+1121.8739)
    return prediction

def mainn():

    html_temp = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap" rel="stylesheet">
    <div style="background-color:rgb(108, 207, 133);opacity:0.9;padding:10px;border-radius:10px;font-family: 'Josefin Sans', sans-serif;">
    <h2 style="color:#fff;text-align:center;">Health Insurance Amount Prediction</h2>
    </div>
    """
    
    html_temp1="""
    <div style="background-color:black;opacity:0.8;padding:10px;border-radius:10px;font-family: 'Josefin Sans', sans-serif;">
    <h3 style="color:#fff;text-align:center;">Data Set of our M L Model</h3>
    </div>
    """
    
    html_temp2="""
    <div style="background-color:black;border-radius:10px;opacity:0.7;font-family: 'Josefin Sans', sans-serif;">
    <h3 style="color:#fff;text-align:center;">Exploring the Dataset of our Problem Statement:</h3>
    </div>
    """
    details=st.sidebar.selectbox(label="HOME",options=['Web-App','Data'])
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.image('ii.png')
    if details=='Web-App':
       st.markdown(html_temp, unsafe_allow_html=True)
       st.write("")
       st.write("This is an application to predict insurance amount based on few parameters")
       st.write("")
       age = st.number_input("Enter your Age: ",min_value=18,max_value=64,step=1)
       age=(age-18)/46
       gender = st.selectbox("Enter your Gender",options=['Male','Female'])
       if gender == 'Male':
                gender = 1
       elif gender == 'Female':
                gender = 0
       bmi = st.number_input("BMI",min_value=15.0,max_value=54.0,step=0.01)
       bmi=(bmi-15.96)/37.17
       children = st.number_input("Enter the number of Children dependent: ",min_value=0,max_value=5,step=1)
       children=children/5
       smoke = st.selectbox("Do You Smoke: ",options=['Yes','No'])
       if smoke == 'Yes':
                smoke = 1
       elif smoke == 'No':
                smoke = 0
       region = st.selectbox("Select your Region ",options=['southeast','southwest','noertheast','northwest'])
       regi=0
       if region == 'southwest':
                regi=1
       elif region == 'southeast':
                regi=2
       elif region == 'northwest':
                regi=3
       elif region == 'northeast':
                regi=4
       reg=(regi-1)/3
       result =""
       if (st.button("Predict")):
        result = pred(age, gender, bmi, children, smoke, reg)
        st.write("Insurance amount is {}".format(result))
    elif details=='Data':    
        st.markdown(html_temp1, unsafe_allow_html=True)
        data=pd.read_csv('insurance.csv')
        st.write("")
        st.write(data)
        st.markdown(html_temp2, unsafe_allow_html=True)
        st.write(" ")
        st.write("The univariate distribution of Age : ")
        st.image('age.png')
        st.write("The univariate distribution of BMI : ")
        st.image('bmi.png')
        st.write("Graph for Gender : ")
        st.image('gender.png')
        st.write("Graph for Smoking : ")
        st.image('smoke.png')
        st.write("Graph for Children dependent on insurance: ")
        st.image('child.png')
        st.write("Graph for region they belong: ")
        st.image('region.png')

if __name__ == '__main__':
    mainn()
