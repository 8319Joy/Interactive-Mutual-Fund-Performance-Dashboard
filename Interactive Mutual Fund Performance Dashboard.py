#!/usr/bin/env python
# coding: utf-8
To create a colorful dashboard for comparing mutual fund performance over at least five years, showing 10 charts with a switch option for dynamic visualization, we can use Python libraries such as Streamlit, Matplotlib, Seaborn, and Plotly. These tools allow creating visually appealing, interactive, and error-free dashboards.
# # Here’s how we can proceed:

# 

# # Install the latest Version:

# In[2]:


pip install numpy


# In[3]:


pip install pandas matplotlib seaborn plotly streamlit


# # Step 2: Design the Code
# The following Python code creates an interactive dashboard for mutual fund performance comparison:

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Function to simulate mutual fund data
def generate_mutual_fund_data():
    years = pd.date_range(start="2015-01-01", end="2023-01-01", freq='Y').year
    funds = ["Fund A", "Fund B", "Fund C", "Fund D", "Fund E"]
    
    data = {
        "Year": np.tile(years, len(funds)),
        "Fund": np.repeat(funds, len(years)),
        "Performance (%)": np.random.uniform(5, 20, len(years) * len(funds))
    }
    return pd.DataFrame(data)

# Load Data
df = generate_mutual_fund_data()

# Streamlit App
st.title("Interactive Mutual Fund Performance Dashboard")

# Sidebar for filters
fund_filter = st.sidebar.multiselect("Select Funds to Compare", options=df["Fund"].unique(), default=df["Fund"].unique())
year_range = st.sidebar.slider("Select Year Range", min_value=int(df["Year"].min()), max_value=int(df["Year"].max()), value=(2015, 2023))

# Filter data based on selections
filtered_data = df[(df["Fund"].isin(fund_filter)) & (df["Year"].between(year_range[0], year_range[1]))]

# Plot 1: Line Chart
st.subheader("Performance Over Years (Line Chart)")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=filtered_data, x="Year", y="Performance (%)", hue="Fund", marker="o", ax=ax1)
ax1.set_title("Yearly Performance Comparison")
ax1.set_ylabel("Performance (%)")
st.pyplot(fig1)

# Plot 2: Bar Chart
st.subheader("Performance Over Years (Bar Chart)")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(data=filtered_data, x="Year", y="Performance (%)", hue="Fund", ax=ax2)
ax2.set_title("Yearly Performance Comparison (Bar)")
ax2.set_ylabel("Performance (%)")
st.pyplot(fig2)

# Plot 3: Box Plot
st.subheader("Performance Distribution (Box Plot)")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=filtered_data, x="Fund", y="Performance (%)", ax=ax3)
ax3.set_title("Performance Distribution by Fund")
ax3.set_ylabel("Performance (%)")
st.pyplot(fig3)

# Heatmap
st.subheader("Heatmap of Performance")
performance_pivot = filtered_data.pivot_table(index="Year", columns="Fund", values="Performance (%)")
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.heatmap(performance_pivot, annot=True, fmt=".1f", cmap="coolwarm", ax=ax4)
ax4.set_title("Heatmap of Performance")
st.pyplot(fig4)

# Statistical Summary
st.subheader("Statistical Summary")
st.dataframe(filtered_data.groupby("Fund")["Performance (%)"].describe())

Features:
Data Simulation: Randomized performance data for 5 mutual funds over a 5+ year period.
Interactive Filters:
Fund selection (multiselect dropdown).
Year range selection (slider).
Visualizations:
Line Chart (Trend comparison).
Bar Chart (Yearly comparisons).
Box Plot (Performance distribution).
Heatmap (Year-wise performance).
Statistical Summary: Descriptive statistics for selected funds.
# In[5]:


pip show numpy


# In[6]:


pip list


# In[ ]:




