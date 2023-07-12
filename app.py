import streamlit as st
from PIL import Image
import pickle
import numpy as np

# Load the machine learning model
model = pickle.load(open('./Model/Solar_Consumption_ML_xgb.pickle', 'rb'))

# Set page configuration
st.set_page_config(
    page_title="Energy Consumption Prediction",
    page_icon="💰",
    layout="wide"
)

def predict_forest(input_data):
    input_columns = ['0:30', '1:00', '1:30', '2:00', '2:30', '3:00', '3:30', '4:00', '4:30', '5:00', '5:30', '6:00', '6:30',
                     '7:00', '7:30', '8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
                     '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00',
                     '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30', '0:00',
                     'CL', 'GC', 'GG', 'date_year', 'date_month', 'date_day']

    # Prepare the input data as a dictionary
    input_dict = {col: 0 for col in input_columns}
    
    # Update the dictionary with the user input
    for col, val in zip(input_columns, input_data):
        input_dict[col] = val
    
    input_array = np.array([list(input_dict.values())], dtype=np.float64)
    
    prediction = model.predict(input_array)
    pred = '{0:.{1}f}'.format(prediction[0], 2)
    return float(pred)

# Define the main function to run the web application
def run():
    # Add a title and image to the page
    st.title("Energy Consumption")
    img1 = Image.open('celebal.jpeg')
    img1 = img1.resize((156, 145))
    st.sidebar.image(img1, use_column_width=False)

    # Create a sidebar with project information
    st.sidebar.header("Project Details")
    st.sidebar.markdown("This web application predicts the likelihood of energy consumption based on the provided information.")

    # Feature Input
    input_data = []
    for hour in range(24):
       for minute in ['00', '30']:
            input_val = st.number_input(f"{hour}:{minute}", min_value=0.0)
            input_data.append(input_val)

    CL = st.radio("CL", [0, 1])
    GC = st.radio("GC", [0, 1])
    GG = st.radio("GG", [0, 1])
    date_year = st.number_input("Date_Year", min_value=0)
    date_month = st.number_input("Date_Month", min_value=0)
    date_day = st.number_input("Date_Day", min_value=0)

    if st.button("Predict"):
        output = predict_forest(input_data)
        st.success('The predicted energy consumption is: {}'.format(output))

# Run the application
run()
