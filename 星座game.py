import streamlit as st
import time  # Ensure time module is imported

# Set the correct answer (your zodiac sign)
my_星座 = "射手"

# Title for the app
st.title("Guess what is my xingzuo")


# List to store guesses (only 1 guess)
guess = st.text_input("What's my xingzuo?", key="guess_0")
if st.button("Check My Answer"):
    if guess.strip().lower() == my_星座.lower():
        st.success("✅ Correct! You guessed my xingzuo!")
    else:
        st.error("❌ Sorry! That's not my xingzuo.")

