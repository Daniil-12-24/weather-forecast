import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast days', min_value=1, max_value=7,
                 help='Select amount of days to Forecast')
option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')


def get_data(days):
    dates = ['2023-01-25', '2023-01-26', '2023-01-27']
    temperatures = [5, 6, -1]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


date, temperature = get_data(days)

figure = px.line(x=date, y=temperature, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)