import streamlit
import pandas
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.title('My parents dine')
streamlit.header('🍞Menu')
streamlit.text('🥣Egss and Omelete')
streamlit.text(' 🥗Egss - Scrambled')
streamlit.text(' 🐔Egss - Poached')
streamlit.text(' 🥑Egss - Fried')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected= streamlit.multiselect('Pick some fruits: ' ,list(my_fruit_list. index),['Avocado', 'Strawberries'])


fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.text('https://docs.google.com/spreadsheets/d/1KVmyYT992-NzmQA2jojb1o7RMUI0o0nGsFMRbVqRVhg/edit?https://docs.google.com/document/d/1GGT8i-CHtdGiVwKSgOd4WeV0DVq8-5gqNP2_QAVg1XA/edit?usp=sharingresourcekey#gid=1372470853')
streamlit.text ('https://docs.google.com/document/d/1GGT8i-CHtdGiVwKSgOd4WeV0DVq8-5gqNP2_QAVg1XA/edit?usp=sharing')

