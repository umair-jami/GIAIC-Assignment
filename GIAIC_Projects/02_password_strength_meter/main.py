import streamlit as st
import re

def check_strength(password: str) -> tuple:
    """Check password strength and return a score and description."""
    score = 0

    # Criteria
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Rating based on score
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score == 3 or score == 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return score, strength, color

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    score, strength, color = check_strength(password)

    st.markdown(f"### Strength: :{color}[{strength}]")
    st.progress(score / 5)

    with st.expander("Tips for Stronger Passwords"):
        st.markdown("""
        - Use at least **8 characters**
        - Include **uppercase** and **lowercase** letters
        - Add **numbers**
        - Use **special characters** (e.g., !, @, #, $)
        """)

else:
    st.info("Please enter a password to check its strength.")
