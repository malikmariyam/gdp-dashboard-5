import streamlit as st
import google.generativeai as genai

# Configure the Gemini API key
genai.configure(api_key="AIzaSyC86IqnS0vAzkijFfnDW2yOEtpWNiea1Vc")

# Define System Prompt
SYSTEM_PROMPT = """
You are a highly knowledgeable and friendly fitness assistant for an advanced gym website. Your task is to answer all gym-related queries with accurate, professional, and practical advice. Your responses should always be:

1. **Comprehensive and Direct** – Provide complete answers addressing the user's query.
2. **Friendly and Motivational** – Encourage users with positive and engaging language.
3. **Expert-Backed** – Base your responses on fitness science, proper training techniques, and nutritional guidelines.

You can handle any gym-related topic, including but not limited to:

- **Workout Plans:** Strength training, weight loss, muscle gain, and flexibility.
- **Diet & Nutrition:** Meal plans for different fitness goals.
- **Fat Loss & Muscle Gain:** Step-by-step guidance for users.
- **Personalized Recommendations:** Routines based on fitness level and goals.
- **Class & Trainer Information:** Gym schedules, personal trainers, and bookings.
- **Gym Equipment & Usage:** Proper use of machines and free weights.
- **Supplements & Recovery:** Protein intake, hydration, and injury prevention.
- **Membership & Services:** Gym memberships, pricing, and facilities.
- **Motivation & Consistency:** Tips to stay committed to fitness.

If a user asks something unrelated to the gym, politely let them know you only answer gym-related queries.
"""

# Function to get chatbot response
def get_gym_chatbot_response(user_query):
    prompt = SYSTEM_PROMPT + f"\nUser Query: {user_query}\nResponse:"
    # Use generate_text instead of directly calling model
    response = genai.generate_text(prompt=prompt)
    return response.text.strip()

# Streamlit UI
st.set_page_config(page_title="Gym Chatbot", page_icon="🏋️‍♂️", layout="centered")

st.markdown(
    """
    <style>
        .chat-container {
            max-width: 650px;
            margin: auto;
            padding: 20px;
            border-radius: 10px;
            background-color: #f9f9f9;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }
        .chat-bubble {
            padding: 12px;
            margin: 10px;
            border-radius: 10px;
            max-width: 80%;
        }
        .user-bubble {
            background-color: #4CAF50;
            color: white;
            align-self: flex-end;
        }
        .bot-bubble {
            background-color: #e3e3e3;
            color: black;
            align-self: flex-start;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align: center;'>💪 Gym Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask me anything about fitness, workouts, diet plans, and more!</p>", unsafe_allow_html=True)

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble bot-bubble'>{msg['content']}</div>", unsafe_allow_html=True)

# Input field
user_input = st.text_input("Type your message...", key="user_input")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f"<div class='chat-bubble user-bubble'>{user_input}</div>", unsafe_allow_html=True)

    # Get bot response
    bot_response = get_gym_chatbot_response(user_input)

    # Display bot response
    st.session_state.messages.append({"role": "bot", "content": bot_response})
    st.markdown(f"<div class='chat-bubble bot-bubble'>{bot_response}</div>", unsafe_allow_html=True)

# Add a clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
