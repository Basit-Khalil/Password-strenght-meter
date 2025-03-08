import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Custom Scoring System
    if len(password) >= 8:
        score += 2  # Higher weight for length
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 2
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 2  # Higher weight for special characters
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    return score, feedback

def generate_strong_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

# Streamlit Theme Configuration
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .stApp {
            background-color: #121212;
            color: white;
        }
        .stTextInput>label {
            color: white !important;
            font-weight: bold;
        }
        .stTextInput>div>div>input {
            background-color: #1e1e1e !important;
            color: white !important;
            border-radius: 8px;
            border: 1px solid white;
            padding: 10px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff8c00, #ff2d55);
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #ff9f40,#ff3b70);
        }
        .stCode {
            background-color: #1e1e1e;
            color: #00ff00;
            padding: 10px;
            border-radius: 5px;
        }
        .footer {
            position: fixed;
            bottom: 10px;
            width: 100%;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: white;
        }
        .strength-bar {
            width: 100%;
            height: 10px;
            border-radius: 5px;
            margin-top: 10px;
        }
        .weak { background-color: white; }
        .moderate { background-color: orange; }
        .strong { background-color: green; }
        .copy-btn {
            background-color: #444;
            color: white;
            border-radius: 5px;
            padding: 5px 10px;
            margin-top: 5px;
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Secure your accounts by using strong passwords!")
st.write("Enter a password below and click the button to check its strength.")
st.write("This tool helps you check the strength of your password and provides suggestions for improvement.")

password = st.text_input("Enter your password:", type="password")



if st.button("Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)
        
        if score >= 6:
            st.success("✅ Strong Password!")
            strength_class = "strong"
        elif score >= 4:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
            strength_class = "moderate"
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")
            strength_class = "weak"
        
        st.markdown(f'<div class="strength-bar {strength_class}"></div>', unsafe_allow_html=True)
        
        if feedback:
            st.write("### Suggestions:")
            for tip in feedback:
                st.write(f"- {tip}")
        
        if score < 6:
            strong_password = generate_strong_password()
            st.write("### Suggested Strong Password:")
            st.code(strong_password)
            st.button("📋 Copy Password", key="copy_btn", help="Click to copy the suggested password")
    else:
        st.warning("Please enter a password before checking strength.")

st.markdown('<div class="footer">Developed By Basit Khalil 🚀 </div>', unsafe_allow_html=True)
