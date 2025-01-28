import streamlit as st
import google.generativeai as genai


# Configure your API key
genai.configure(api_key="AIzaSyC86IqnS0vAzkijFfnDW2yOEtpWNiea1Vc")

# Define the system prompt to guide the chatbot
SYSTEM_PROMPT = """
You are a knowledgeable and helpful assistant for a sophisticated gym website. Your task is to answer all questions related to gym topics with direct and clear answers. Your responses should always be:
1. Direct and complete, addressing the user’s query.
2. Friendly and professional, with a focus on gym-related topics.

For common gym queries like class schedules, gym timings, memberships, and equipment, provide **direct answers**. 

If the user asks an ambiguous or non-gym-related question, gently let them know that you can only answer gym-related questions. 

Example topics you can cover:
- **Gym Schedule & Timings:** Answer questions like "What time does the gym open?" or "When are you closed on holidays?"
- **Classes:** Availability, types of classes (e.g., Hatha Yoga, Vinyasa Flow), schedules, and booking.
- **Trainers:** Availability of trainers and booking personal training sessions.
- **Payments & Billing:** Answer questions about gym memberships, payment methods, and billing cycles.
- **Gym Equipment & Facilities:** Information about the gym’s equipment and other amenities (sauna, pool, etc.).

If the question is not related to the gym or you don’t have enough information, say: "I’m sorry, I can only answer gym-related questions."

Do not ask for additional information unless it's absolutely necessary to clarify a query.
"""

# Initialize the model using Gemini
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get a response from the chatbot
def get_gym_chatbot_response(user_query):
    prompt = SYSTEM_PROMPT + f"\nUser Query: {user_query}\nResponse:"
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
def chatbot():
    st.title("Gym Chatbot")
    st.write("Welcome to the Gym Chatbot! Ask me any gym-related questions.")
    
    user_input = st.text_input("You: ", "")
    
    if user_input:
        bot_response = get_gym_chatbot_response(user_input)
        st.write(f"Bot: {bot_response}")
    
    if st.button('Exit'):
        st.write("Goodbye! Have a great day at the gym!")
        
# Run the app
if __name__ == '__main__':
    chatbot()
