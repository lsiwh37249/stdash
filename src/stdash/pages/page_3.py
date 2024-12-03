import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import datetime as dt
import numpy as np

st.title("CNN JOB MON")

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()

    return d
data = load_data()
df = pd.DataFrame(data)

df['request_user']=df['request_user'].astype(str)
requestu=df.groupby('request_user').size()

# df_groupuser['request_count'] = df.groupby('request_user').size['num']
# #df_groupuser['key'] = df_grouped.index
# #df_groupuser['key']
# df_groupuser['request_count']

df['prediction_model']=df['prediction_model'].astype(str)
predictionm=df.groupby('prediction_model').size()

# #size()
# df_prediction = df.groupby('prediction_model').size()
# df_prediction

plt.figure(figsize=(16, 8))
plt.bar(requestu.index, requestu.values, width=0.4, label='request', color='blue', align='center')
plt.bar(predictionm.index, predictionm.values, width=0.4, label='predicton', color='red', align="edge")

plt.title('Request user(BLUE) and Prediction(RED) Counts over Time')
plt.xlabel('time')
plt.ylabel('count')

# plt.figure(figsize=(16,8))
# #.index .values
# plt.bar(df_groupuser.index, df_groupuser.values)
# plt.bar(df_prediction.index, df_prediction.values)

st.pyplot(plt)
st.sidebar.markdown("# Page 3 ❄️")
