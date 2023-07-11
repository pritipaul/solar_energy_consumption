import streamlit as st
from PIL import Image
import pickle


# Load the machine learning model
model = pickle.load(open('./Model/Solar_Consumption_ML.pickle', 'rb'))

# Set page configuration
st.set_page_config(
    page_title="Energy Consumption Prediction",
    page_icon="💰",
    layout="wide"
)


# Define the main function to run the web application
def run():
    # Add a title and image to the page
    st.title("Energy Consumption")
    img1 = Image.open('celebal.jpeg')
    img1 = img1.resize((156, 145))
    st.sidebar.image(img1, use_column_width=False)

    # Create a sidebar with project information
    st.sidebar.header("Project Details")
    st.sidebar.markdown("This web application predicts the likelihood of a energy_consumption based on the provided information.")

    # Feature Input
    Time030 = st.number_input("12:30 am")
    Time100 = st.number_input("1:00 am")
    Time130 = st.number_input("1:30 am")
    Time200 = st.number_input("2:00 am")
    Time230 = st.number_input("2:30 am")
    Time300 = st.number_input("3:00 am")
    Time330 = st.number_input("3:30 am")
    Time400 = st.number_input("4:00 am")
    Time430 = st.number_input("4:30 am")
    Time500 = st.number_input("5:00 am")
    Time530 = st.number_input("5:30 am")
    Time600 = st.number_input("6:00 am")
    Time630 = st.number_input("6:30 am")
    Time700 = st.number_input("7:00 am")
    Time730 = st.number_input("7:30 am")
    Time800 = st.number_input("8:00 am")
    Time830 = st.number_input("8:30 am")
    Time900 = st.number_input("9:00 am")
    Time930 = st.number_input("9:30 am")
    Time1000 = st.number_input("10:00 am")
    Time1030 = st.number_input("10:30 am") 
    Time1100 = st.number_input("11:00 am")
    Time1130 = st.number_input("11:30 am")
    Time1200 = st.number_input("12:00 pm")
    Time1230 = st.number_input("12:30 pm")
    Time1300 = st.number_input("1:00 pm")
    Time1330 = st.number_input("1:30 pm", min_value=0)
    Time1400 = st.number_input("2:00 pm")
    Time1430 = st.number_input("2:30 pm")
    Time1500 = st.number_input("3:00 pm")
    Time1530 = st.number_input("3:30 pm")
    Time1600 = st.number_input("4:00 pm")
    Time1630 = st.number_input("4:30 pm")
    Time1700 = st.number_input("5:00 pm")
    Time1730 = st.number_input("5:30 pm")
    Time1800 = st.number_input("6:00 pm")
    Time1830 = st.number_input("6:30 pm")
    Time1900 = st.number_input("7:00 pm")
    Time1930 = st.number_input("7:30 pm")
    Time2000 = st.number_input("8:00 pm")
    Time2030 = st.number_input("8:30 pm")
    Time2100 = st.number_input("9:00 pm")
    Time2130 = st.number_input("9:30 pm")
    Time2200 = st.number_input("10:00 pm")
    Time2230 = st.number_input("10:30 pm")
    Time2300 = st.number_input("11:00 pm")
    Time2330 = st.number_input("11:30 pm")
    Time000 = st.number_input("12:00 am")
    CL	= st.radio("CL", [0, 1])
    GC	= st.radio("GC", [0, 1])
    GG	= st.radio("GG", [0, 1])
    date_year = st.number_input("Date_Year", min_value=0000)
    date_month	= st.number_input("Date_Month", min_value=00)
    date_day = st.number_input("Date_Day", min_value=00)

    if st.button("Predict"):
        features = [Time030,Time100,Time130,Time200,Time230,Time300,Time330,Time400,Time430,Time500,Time530,Time600,Time630,Time700,Time730,Time800,Time830,Time900,Time930,Time1000,Time1030,Time1100,Time1130,Time1200,Time1230,Time1300,Time1330,Time1400,Time1430,Time1500,Time1530,Time1600,Time1630,Time1700,Time1730,Time1800,Time1830,Time1900,Time1930,Time2000,Time2030,Time2100,Time2130,Time2200,Time2230,Time2300,Time2330,Time0000,CL,GC,GG,date_year,date_month,date_day]
        predicted_label = predict_energy_consumption(features)
        st.write("Predicted Label:", predicted_label)
  


# Run the application
run()
