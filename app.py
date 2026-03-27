import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#load data
url = 'https://raw.githubusercontent.com/jfkoehler/nyu_bootcamp_spr26/refs/heads/main/data/food_data.csv'
df = pd.read_csv(url)

st.title("Customer Behavior and Campaign Response")

# filter by income
income_range = st.slider(
    "Select Income Range",
    int(df["Income"].min()),
    int(df["Income"].max()),
    (20000, 100000)
)

filtered_df = df[
    (df["Income"] >= income_range[0]) &
    (df["Income"] <= income_range[1])
]

st.write("Filtered Data Preview")
st.write(filtered_df.head())

# scatter plot
fig, ax = plt.subplots()
ax.scatter(filtered_df["Income"], filtered_df["MntWines"])
ax.set_xlabel("Income")
ax.set_ylabel("Wine Spending")
ax.set_title("Income vs Wine Spending")

st.pyplot(fig)