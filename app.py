import streamlit as st
import numpy as np
import pandas as pd
import pickle

#col1,col2=st.columns([1,3])
#with col1:
 #   st.image("car3.jpg",width=80)
#with col2:
st.title("🚗Car Prediction APP")

st.subheader("Hello Dhaneshwari 👋")

pipe=pickle.load(open("pipe.pkl", "rb"))
df=pd.read_csv("final_data.csv")
companies=sorted(df["company"].unique())
years=range(2000,2027)

company=st.sidebar.selectbox("Select company",companies)
names=sorted(df[df['company']==company]["name"].unique())

name=st.sidebar.selectbox("Select name",names)
year=st.sidebar.selectbox("Select year",years)
km_driven=st.sidebar.number_input("Enter kms driven",value=50000,min_value=1000,max_value=200000,step=1000)
fuel=st.sidebar.selectbox("Select fuel tye",["Petrol","Diesel"])

if st.sidebar.button("Predict price"):
    #st.success(f"Welcome Dhaneshwari! 🎉")
    st.write("You have selected:")
    st.write(f"Company : {company}")
    st.write(f"Name : {name}")
    st.write(f"Year : {year}")
    st.write(f"Kilometer Driven : {km_driven}")
    st.write(f"Fuel type : {fuel}")

    myinput=[[company,name,year,km_driven,fuel]]
    columns=['company','name','year','kms_driven','fuel_type']
    myinput=pd.DataFrame(data=myinput,columns=columns)
    result=pipe.predict(myinput)

    if result[0,0]<0:
        st.write("Sorry, the predicted price is negative. Please check your input values.")
    else:
        st.success(f"💰 Estimated Treatment Cost: ₹ {round(result[0], 2)}")
        st.ballons()