import streamlit
import pandas
import requests
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

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

