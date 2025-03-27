import streamlit as st
import time
my_xingzuo="射手"
st.title("Guess what is my xingzuo")
tries = st.number_input("How many tries?", min_value=1, max_value=5, value=3)
time_limit = st.number_input("Time limit (in seconds):", min_value=10, max_value=60, value=30)
start_time = time.time()
guesses=[]

for i in range(int(tries)):
    elapsed_time = time.time() - start_time  # Time passed since the start of the game
    if elapsed_time > time_limit:
        st.warning("⏰ Time's up! You ran out of time.")
        break
    guess = st.text_input(f"Attempt {i+1}: What is my xingzuo?", key=f"guess_{i}")
    guesses.append(guess)

# Button to check the user's answers
if st.button("Check My Answers"):
    correct = False
    # Loop through the guesses to check if any guess is correct
    for guess in guesses:
        if guess.strip().lower() == my_xingzuo.lower():
            st.success("✅ Correct! You guessed my xingzuo!")
            correct = True
            break
    if not correct:
        st.error("❌ Sorry! That's not my xingzuo.")
