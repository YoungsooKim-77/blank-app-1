import streamlit as st

st.title("🎈 김영수 app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


import streamlit as st
import pandas as pd
import numpy as np

st.text("안녕하세요 김영수입니다.")


# Example
df = pd.DataFrame(
    np.random.randn(20, 4),
    columns=["a", "b", "c", "d"])

st.area_chart(
    df,
    x="a",
    y=["b", "c", "d"],
    color=["#1764AB", "#4A98CA", "#94C5DF"],
)


if st.button('Say Hello'):
   st.write('Hello, Streamlit!')


if st.button('Click Me', key='my_button', help='Click this button to perform an action'):
   st.write('You clicked the button!')
