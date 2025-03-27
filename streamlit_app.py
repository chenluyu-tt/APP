import streamlit as st
import random

st.title("🎲 Coin Flip Simulator")

st.write("This app simulates flipping a coin 100 times!")

if st.button("Flip the Coin"):
    outcomes = {"Heads": 0, "Tails": 0}
    for _ in range(100):
        result = random.choice(["Heads", "Tails"])
        outcomes[result] += 1

    st.write("Heads:", outcomes["Heads"])
    st.write("Tails:", outcomes["Tails"])
