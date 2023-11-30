import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("LR_model.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome ALL"
def predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk):
     prediction=classifier.predict([[industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk]])
     print(prediction)
     return prediction





def main():
    st.title("Bankruptcy Prevention")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Bankruptcy Prevention App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    industrial_risk = st.text_input("industrial_risk","  ")
    management_risk = st.text_input("management_risk","  ")
    financial_flexibility = st.text_input("financial_flexibility","  ")
    credibility = st.text_input("credibility","  ")
    competitiveness = st.text_input("competitiveness","  ")
    operating_risk = st.text_input("operating_risk","  ")
    result=""
    if st.button("Predict"):
        result=predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk)
        if result==0:    
            st.success("Company is Non-Bankrupt")
        else:
            st.success("Company is Bankrupt")
    if st.button("About"):
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()