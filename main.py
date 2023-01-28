import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast days', min_value=1, max_value=5,
                 help='Select amount of days to Forecast')
option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

if place:
    filtered_data = get_data(place, days)

    if option == 'Temperature':
        temperature = [dict['main']['temp'] for dict in filtered_data]

        dates = [dict['dt_txt'] for dict in filtered_data]
        figure = px.line(x=dates, y=temperature, labels={'x': 'Date', 'y': 'Temperature (C)'})
        st.plotly_chart(figure)

    if option == 'Sky':
        images = {'Clear': 'pictures/clear.png',
                  'Clouds': 'pictures/cloud.png',
                  'Rain': 'pictures/rain.png',
                  'Snow': 'pictures/snow.png'}
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        images_path = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(images_path, width=115)

