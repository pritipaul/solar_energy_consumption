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
    Time0:30 = st.number_input("12:30 am", min_value=0)
    1:00 = st.number_input("1:00 am", min_value=0)
    1:30 = st.number_input("1:30 am", min_value=0)
    2:00 = st.number_input("2:00 am", min_value=0)
    2:30 = st.number_input("2:30 am", min_value=0)
    3:00 = st.number_input("3:00 am", min_value=0)
    3:30 = st.number_input("3:30 am", min_value=0)
    4:00 = st.number_input("4:00 am", min_value=0)
    4:30 = st.number_input("4:30 am", min_value=0)
    5:00 = st.number_input("5:00 am", min_value=0)
    5:30 = st.number_input("5:30 am", min_value=0)
    6:00 = st.number_input("6:00 am", min_value=0)
    6:30 = st.number_input("6:30 am", min_value=0)
    7:00 = st.number_input("7:00 am", min_value=0)
    7:30 = st.number_input("7:30 am", min_value=0)
    8:00 = st.number_input("8:00 am", min_value=0)
    8:30 = st.number_input("8:30 am", min_value=0)
    9:00 = st.number_input("9:00 am", min_value=0)
    9:30 = st.number_input("9:30 am", min_value=0)
    10:00 = st.number_input("10:00 am", min_value=0)
    10:30 = st.number_input("10:30 am", min_value=0) 
    11:00 = st.number_input("11:00 am", min_value=0)
    11:30 = st.number_input("11:30 am", min_value=0)
    12:00 = st.number_input("12:00 pm", min_value=0)
    12:30 = st.number_input("12:30 pm", min_value=0)
    13:00 = st.number_input("1:00 pm", min_value=0)
    13:30 = st.number_input("1:30 pm", min_value=0)
    14:00 = st.number_input("2:00 pm", min_value=0)
    14:30 = st.number_input("2:30 pm", min_value=0)
    15:00 = st.number_input("3:00 pm", min_value=0)
    15:30 = st.number_input("3:30 pm", min_value=0)
    16:00 = st.number_input("4:00 pm", min_value=0)
    16:30 = st.number_input("4:30 pm", min_value=0)
    17:00 = st.number_input("5:00 pm", min_value=0)
    17:30 = st.number_input("5:30 pm", min_value=0)
    18:00 = st.number_input("6:00 pm", min_value=0)
    18:30 = st.number_input("6:30 pm", min_value=0)
    19:00 = st.number_input("7:00 pm", min_value=0)
    19:30 = st.number_input("7:30 pm", min_value=0)
    20:00 = st.number_input("8:00 pm", min_value=0)
    20:30 = st.number_input("8:30 pm", min_value=0)
    21:00 = st.number_input("9:00 pm", min_value=0)
    21:30 = st.number_input("9:30 pm", min_value=0)
    22:00 = st.number_input("10:00 pm", min_value=0)
    22:30 = st.number_input("10:30 pm", min_value=0)
    23:00 = st.number_input("11:00 pm", min_value=0)
    23:30 = st.number_input("11:30 pm", min_value=0)
    0:00 = st.number_input("12:00 am", min_value=0)
    Energy Consumption = st.number_input("Energy Consumption", min_value=0)
    CL	= st.radio("CL", [0, 1])
    GC	= st.radio("GC", [0, 1])
    GG	= st.radio("GG", [0, 1])
    date_year = st.number_input("Date_Year", min_value=0000)
    date_month	= st.number_input("Date_Month", min_value=00)
    date_day = st.number_input("Date_Day", min_value=00)

    if st.button("Predict"):
        features = [0:30,1:00,1:30,2:00,2:30,3:00,3:30,4:00,4:30,5:00,5:30,6:00,6:30,7:00,7:30,8:00,8:30,9:00,9:30,10:00,10:30,11:00,11:30,12:00,12:30,13:00,13:30,14:00,14:30,15:00,15:30,16:00,16:30,17:00,17:30,18:00,18:30,19:00,19:30,20:00,20:30,21:00,21:30,22:00,22:30,23:00,23:30,0:00,Energy Consumption,CL,GC,GG,date_year,date_month,date_day]
        predicted_label = predict_energy_consumption(features)
        st.write("Predicted Label:", predicted_label)
  


# Run the application
run()
