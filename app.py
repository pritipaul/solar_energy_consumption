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
    Time1:00 = st.number_input("1:00 am", min_value=0)
    Time1:30 = st.number_input("1:30 am", min_value=0)
    Time2:00 = st.number_input("2:00 am", min_value=0)
    Time2:30 = st.number_input("2:30 am", min_value=0)
    Time3:00 = st.number_input("3:00 am", min_value=0)
    Time3:30 = st.number_input("3:30 am", min_value=0)
    Time4:00 = st.number_input("4:00 am", min_value=0)
    Time4:30 = st.number_input("4:30 am", min_value=0)
    Time5:00 = st.number_input("5:00 am", min_value=0)
    Time5:30 = st.number_input("5:30 am", min_value=0)
    Time6:00 = st.number_input("6:00 am", min_value=0)
    Time6:30 = st.number_input("6:30 am", min_value=0)
    Time7:00 = st.number_input("7:00 am", min_value=0)
    Time7:30 = st.number_input("7:30 am", min_value=0)
    Time8:00 = st.number_input("8:00 am", min_value=0)
    Time8:30 = st.number_input("8:30 am", min_value=0)
    Time9:00 = st.number_input("9:00 am", min_value=0)
    Time9:30 = st.number_input("9:30 am", min_value=0)
    Time10:00 = st.number_input("10:00 am", min_value=0)
    Time10:30 = st.number_input("10:30 am", min_value=0) 
    Time11:00 = st.number_input("11:00 am", min_value=0)
    Time11:30 = st.number_input("11:30 am", min_value=0)
    Time12:00 = st.number_input("12:00 pm", min_value=0)
    Time12:30 = st.number_input("12:30 pm", min_value=0)
    Time13:00 = st.number_input("1:00 pm", min_value=0)
    Time13:30 = st.number_input("1:30 pm", min_value=0)
    Time14:00 = st.number_input("2:00 pm", min_value=0)
    Time14:30 = st.number_input("2:30 pm", min_value=0)
    Time15:00 = st.number_input("3:00 pm", min_value=0)
    Time15:30 = st.number_input("3:30 pm", min_value=0)
    Time16:00 = st.number_input("4:00 pm", min_value=0)
    Time16:30 = st.number_input("4:30 pm", min_value=0)
    Time17:00 = st.number_input("5:00 pm", min_value=0)
    Time17:30 = st.number_input("5:30 pm", min_value=0)
    Time18:00 = st.number_input("6:00 pm", min_value=0)
    Time18:30 = st.number_input("6:30 pm", min_value=0)
    Time19:00 = st.number_input("7:00 pm", min_value=0)
    Time19:30 = st.number_input("7:30 pm", min_value=0)
    Time20:00 = st.number_input("8:00 pm", min_value=0)
    Time20:30 = st.number_input("8:30 pm", min_value=0)
    Time21:00 = st.number_input("9:00 pm", min_value=0)
    Time21:30 = st.number_input("9:30 pm", min_value=0)
    Time22:00 = st.number_input("10:00 pm", min_value=0)
    Time22:30 = st.number_input("10:30 pm", min_value=0)
    Time23:00 = st.number_input("11:00 pm", min_value=0)
    Time23:30 = st.number_input("11:30 pm", min_value=0)
    Time0:00 = st.number_input("12:00 am", min_value=0)
    Energy_Consumption = st.number_input("Energy Consumption", min_value=0)
    CL	= st.radio("CL", [0, 1])
    GC	= st.radio("GC", [0, 1])
    GG	= st.radio("GG", [0, 1])
    date_year = st.number_input("Date_Year", min_value=0000)
    date_month	= st.number_input("Date_Month", min_value=00)
    date_day = st.number_input("Date_Day", min_value=00)

    if st.button("Predict"):
        features = [Time0,Time1,Time1,Time2,Time2,Time3,Time3,Time4,Time4,Time5,Time5,Time6,Time6,Time7,Time7,Time8,Time8,Time9,Time9,Time10,Time10,Time11,Time11,Time12,Time12,Time13,Time13,Time14,Time14,Time15,Time15,Time16,Time16,Time17,Time17,Time18,Time18,Time19,Time19,Time20,Time20,Time21,Time21,Time22,Time22,Time23,Time23,Time00,Energy_Consumption,CL,GC,GG,date_year,date_month,date_day]
        predicted_label = predict_energy_consumption(features)
        st.write("Predicted Label:", predicted_label)
  


# Run the application
run()
