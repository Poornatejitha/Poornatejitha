import numpy as np
import pickle
import streamlit as st



# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))




def diabetes_prediction(input_data):
    

    
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Glucose = st.text_input('Glucose Level')
    Insulin = st.text_input('Insulin Level (mg/dL)')
    BMI = st.text_input('BMI value(weight in kg/(height in m)^2)')
    Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Glucose, Insulin, BMI, Age])
        
        
    st.success(diagnosis)

    
    
    
    
if __name__ == '__main__':
    main()
    # Function to handle chatbot responses
def chatbot_response(user_input): 
    # Simple rule-based responses
    responses = {
        "hi": "Hello! How can I help you?",
        "hello":"hi!",
        "how are you": "I'm a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
        "help": "Sure, I am here to help. Ask me anything!",
        "symptoms": "Common symptoms include increased thirst, frequent urination, extreme fatigue, blurred vision, and slow healing of wounds.",
        "risk factors for diabetes": "Risk factors include being overweight, being 45 years or older, having a family history of diabetes, and having high blood pressure.",
        "how to prevent": "Preventing diabetes involves maintaining a healthy diet, regular physical activity, and keeping a healthy weight.",
        "how to cure": "There is no cure for diabetes, but it can be managed with medication, lifestyle changes, and regular monitoring.",
        "role of insulin": "Insulin is a hormone that helps glucose from food enter your cells to be used for energy. In diabetes, the body either doesn't produce enough insulin or can't use it effectively, leading to high blood sugar levels.",
        "complications of diabetes": "Long-term complications of diabetes can include cardiovascular disease, nerve damage (neuropathy), kidney damage (nephropathy), eye damage (retinopathy), foot damage, skin conditions, and hearing impairment.",
        "how is diabetes diagnosed": "Diabetes is diagnosed through blood tests such as the fasting plasma glucose test, oral glucose tolerance test, and A1C test, which measures average blood glucose levels over the past 2-3 months.",
        "lifestyle changes for diabetes": "Key lifestyle changes include eating a balanced diet, engaging in regular physical activity, monitoring blood sugar levels, maintaining a healthy weight, and avoiding smoking and excessive alcohol consumption.",
        "myths about diabetes": "Common myths include the idea that eating too much sugar causes diabetes, only overweight people get diabetes, and people with diabetes can't eat any sugar. It's important to distinguish these myths from facts.",
        "what is gestational diabetes": "Gestational diabetes is a type of diabetes that develops during pregnancy. It usually goes away after the baby is born, but it increases the risk of developing Type 2 diabetes later in life.",
        "can children get diabetes": "Yes, children can develop both Type 1 and Type 2 diabetes. Type 1 diabetes is more common in children and is usually diagnosed in childhood or adolescence.",
        "what is prediabetes": "Prediabetes is a condition where blood sugar levels are higher than normal but not high enough to be diagnosed as Type 2 diabetes. It increases the risk of developing Type 2 diabetes, heart disease, and stroke.",
        
    }
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")



# Title of the app
st.title("QUERIES?")

# Main section
st.write("DO YOU HAVE ANY QUERIES?.ASK ME!")

# Create a placeholder for chat history
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Function to display chat messages
def display_chat():
    for message in st.session_state['messages']:
        if message['role'] == 'user':
            st.markdown(f"**You:** {message['content']}")
        else:
            st.markdown(f"**Bot:** {message['content']}")

# Input text box for user input
user_input = st.text_input("You:", key="user_input")

# If user enters a message
if user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})
    response = chatbot_response(user_input)
    st.session_state['messages'].append({"role": "bot", "content": response})
   

# Display chat history
display_chat()