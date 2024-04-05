import streamlit as st
from joblib import load

model = load("logistic_model.joblib")
st.write ("Model uploaded!")

def get_user_input():
  Pregnancies = st.number_input("How many pregnancies have you had?")
  Glucose = st.number_input("What is your glucose level?")
  BloodPressure = st.number_input("What is your blood pressure?")
  SkinThickness = st.number_input("What is your skin thickness level in mm?")
  Insulin = st.number_input("What is your insulin level?")
  BMI = st.number_input("What is your BMI?")
  DiabetesPedigreeFunction = st.number_input("What is your diabetes pedigree function")
  Age = st.number_input("What is your age?")
  input_features = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
  return input_features

def make_prediction(model, input):
  return model.predict(input)

def get_app_response(prediction):
  if prediction == 1:
    st.write("The model predicts that you have diabetes.")
  elif prediction == 0:
    st.write("The model predicts that you do not have diabetes.")
  else:
    st.write ("No results yet.")

input_features = get_user_input()
prediction = make_prediction(model, input_features)
get_app_response(prediction)
