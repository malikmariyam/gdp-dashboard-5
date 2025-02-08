import streamlit as st
import google.generativeai as genai
import time

# Configure the Gemini API key
genai.configure(api_key="AIzaSyC86IqnS0vAzkijFfnDW2yOEtpWNiea1Vc")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# System Prompt
SYSTEM_PROMPT = """
You are a highly knowledgeable and friendly fitness assistant for an advanced gym website. 
Your task is to answer all gym-related queries with accurate, professional, and practical advice.

You can handle any gym-related topic, including:
- Workout Plans (Strength, Weight Loss, Muscle Gain)
- Diet & Nutrition (Meal Plans, Supplements, Recovery)
- Fat Loss & Muscle Gain (Guidance & Tips)
- Gym Equipment Usage, Class & Trainer Schedules
- Motivation, Consistency, Membership & Pricing Details

If a user asks something unrelated to the gym, politely let them know you only answer gym-related queries.
"""

# Function to get chatbot response
def get_gym_chatbot_response(user_query):
    prompt = SYSTEM_PROMPT + f"\nUser Query: {user_query}\nResponse:"
    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit UI Configuration
st.set_page_config(page_title="Gym Chatbot", page_icon="🏋️‍♂️", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #f8f9fa !important;  /* Light Grey */
        }

        /* Chat Container */
        .chat-container {
            max-width: 750px;
            margin: auto;
            padding: 20px;
            border-radius: 12px;
            background: #ffffff;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
        }

        /* Chat Messages */
        .chat-bubble {
            padding: 14px;
            margin: 10px;
            border-radius: 12px;
            max-width: 75%;
            font-size: 16px;
            word-wrap: break-word;
            transition: all 0.3s ease-in-out;
        }

        /* User Message (Right-Aligned) */
        .user-bubble {
            background: #cce5ff; /* Light Blue */
            color: #004085; /* Dark Blue Text */
            font-weight: bold;
            align-self: flex-end;
            margin-left: auto;
            text-align: left;
            animation: fadeInRight 0.3s;
        }

        /* Bot Message (Left-Aligned) */
        .bot-bubble {
            background: #f8f9fa; /* Very Light Grey */
            color: black;
            font-weight: 500;
            align-self: flex-start;
            margin-right: auto;
            text-align: left;
            animation: fadeInLeft 0.3s;
        }

        /* Chat Input Box */
        .stTextInput>div>div>input {
            background-color: #cce5ff !important;  /* Light Blue */
            border: 1px solid #0078FF !important; /* Darker Blue Border */
            color: black !important;
        }

        /* Animations */
        @keyframes fadeInLeft {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }

        @keyframes fadeInRight {
            from { opacity: 0; transform: translateX(20px); }
            to { opacity: 1; transform: translateX(0); }
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar - Chat History
st.sidebar.title("📜 Chat History")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history in sidebar
if st.session_state.chat_history:
    for i, chat in enumerate(st.session_state.chat_history):
        if st.sidebar.button(f"Chat {i+1} 🏋️", key=f"chat_{i}"):
            st.session_state.messages = chat["messages"]
            st.rerun()

# Button to Start New Chat
if st.sidebar.button("➕ Start New Chat", key="new_chat"):
    st.session_state.messages = []
    st.session_state.chat_history.append({"messages": []})
    st.rerun()

# Main Chat Interface
st.markdown('<div style="text-align: center; font-size: 32px; font-weight: bold;">💪 AI Gym Chatbot</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 18px; color: #333;">Ask me anything about fitness, workouts, diet plans, and more!</p>', unsafe_allow_html=True)

# Session State for Messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input Box
user_input = st.chat_input("Type your message here...")

if user_input:
    # Store and Display User Message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Typing Effect
    with st.spinner("🤖 Thinking..."):
        time.sleep(1.5)

    # Generate Bot Response
    bot_response = get_gym_chatbot_response(user_input)

    # Store and Display Bot Response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)

# Save Chat to History
if st.session_state.messages and len(st.session_state.chat_history) > 0:
    st.session_state.chat_history[-1]["messages"] = st.session_state.messages
