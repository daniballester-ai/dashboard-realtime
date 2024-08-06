import pandas as pd
import streamlit as st
import numpy as np
import time
import plotly.express as px     

# read the csv file from github (static data for this example)
df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

st.set_page_config(
    page_title='Real-Time Finance/Marketing/Data Science Dashboard',
    page_icon='🎲',
    layout='wide',      
)
# title
st.title('Real-Time Finance/Marketing Live Data Science Dashboard')

# filter
job_filter = st.selectbox("Select the Job", pd.unique(df['job']))

# container to refresh and replace elements in real time
# just create, not use yet
placeholder = st.empty()

# ------------------------- usar isso para filtrar o dataframe -----------------------
# dataframe filter
df = df[df.job == job_filter]

# ---------- real- time simulatinon --------------------------------------------------
# update in seconds: here we will simulate a dinamic data with random lines from csv
# but you can read from an api

for seconds in range(200):
#while True: 
    
    # new data from random csv or an api
    df['age_new'] = df['age'] * np.random.choice(range(1,5))
    df['balance_new'] = df['balance'] * np.random.choice(range(1,5))

    # creating KPIs 
    avg_age = np.mean(df['age_new']) 

    count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))
    
    balance = np.mean(df['balance_new'])

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs 
        kpi1.metric(label="Age ⏳", value=round(avg_age), delta= round(avg_age) - 10)
        kpi2.metric(label="Married Count 💍", value= int(count_married), delta= - 10 + count_married)
        kpi3.metric(label="A/C Balance ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_married) * 100)

        # create two columns for charts 

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(data_frame=df, y='age_new', x='marital',
                color_continuous_scale=['#460598','#FF0000', '#FFA500', '#FFFF00'])
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame = df, x = 'age_new')
            st.write(fig2)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
    #placeholder.empty()

    #commited