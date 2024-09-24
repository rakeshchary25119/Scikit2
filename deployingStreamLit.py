import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image

# loading in the model to predict on the data 
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in) 


def welcome(): 
    return 'welcome all'

# defining the function which will make the prediction using  
# the data which the user inputs 
def prediction(CustomerId, Surname, CreditScore, Geography,
       Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard,
       IsActiveMember, EstimatedSalary):   
   
    prediction = classifier.predict( 
        [['CustomerId', 'Surname', 'CreditScore', 'Geography',
       'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
       'IsActiveMember', 'EstimatedSalary']]) 
    print(prediction) 
    return prediction 
      
  
# this is the main function in which we define our webpage  
def main(): 
      # giving the webpage a title 
    st.title("Iris Flower Prediction") 
      
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding and the text to be displayed 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Iris Flower Classifier ML App </h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
    CustomerId = st.text_input("CustomerId", "Type Here") 
    Surname = st.text_input("Surname", "Type Here") 
    CreditScore = st.text_input("CreditScore", "Type Here") 
    Geography = st.text_input("Geography", "Type Here") 
    Gender = st.text_input("Gender", "Type Here") 
    Age = st.text_input("Age", "Type Here") 
    Tenure = st.text_input("Tenure", "Type Here") 
    Balance = st.text_input("Balance", "Type Here") 
    NumOfProducts = st.text_input("NumOfProducts", "Type Here") 
    HasCrCard = st.text_input("HasCrCard", "Type Here") 
    IsActiveMember = st.text_input("IsActiveMember", "Type Here") 
    EstimatedSalary = st.text_input("EstimatedSalary", "Type Here") 
    result ="" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if st.button("Predict"): 
        result = prediction(CustomerId, Surname, CreditScore, Geography,
       Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard,
       IsActiveMember, EstimatedSalary) 
    st.success('The output is {}'.format(result)) 
     
if __name__=='__main__': 
    main() 