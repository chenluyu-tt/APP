import streamlit as st

# ✅ Your name
my_name = "Brigitta"

# Title
st.title("🧠 Who Is Your Best Friend?")

# Make a list to store guesses
guesses = []

# For loop to ask multiple times

guess = st.text_input(f" What's your best friend's name?", key=0)
guesses.append(guess)

# Button to check answers
if st.button("Check My Answers"):
    correct = False
    for guess in guesses:
        if guess.strip().lower() == my_name.lower():
            st.success("✅ Correct! You are my best friend 💖")
            correct = True
            break
    if not correct:
        st.error("❌ Sorry! That's not my best friend 😢")
