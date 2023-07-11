import streamlit as st
from PIL import Image
import pickle


# Load the machine learning model
model = pickle.load(open('./Model/Solar_Consumption_ML.pickle', 'rb'))

# Set page configuration
st.set_page_config(
    page_title="Bank Loan Prediction",
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
    st.sidebar.markdown("This web application predicts the likelihood of a loan approval by a bank based on the provided information.")

    # Feature Input
    0:30 = st.number_input("12:30 am", min_value=0)
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
    GG	= st.radio("GG

    date_month	
    date_day

  
    if st.button("Submit"):
        duration = [60, 180, 240, 360, 480]
        dur_mapping = dict(zip(dur_options, duration))
        duration = dur_mapping[dur]

        # Prepare features for prediction
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))

        # Display prediction result
        if ans == 0:
            st.error(f"Hello: {fn} | Account number: {account_no} | According to our analysis, you are unlikely to receive a loan from the bank.")
        else:
            st.success(f"Hello: {fn} | Account number: {account_no} | Congratulations! You are eligible for a loan from the bank.")


# Run the application
run()
