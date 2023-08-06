import requests
import json
import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()

url = "https://countriesnow.space/api/v0.1/countries/population/cities"
response = requests.get(url)
response_json = json.loads(response.text)

database = os.getenv('bd')
user = os.getenv('usuario')
password = os.getenv('senha')
host = os.getenv('servidor')
port = os.getenv('porta')
qty_cities = 4501

try:
	connection = psycopg2.connect(
		database=database,
		user=user,
		password=password,
		host=host,
		port=port
	)

	cursor = connection.cursor()
	for city in response_json["data"][:qty_cities]:
		new_insertion = (city["city"], city["country"], city["populationCounts"][0]["value"])
		insert_query = "INSERT INTO city (city, country, population) VALUES (%s, %s, %s);"
		cursor.execute(insert_query, new_insertion)
		connection.commit()

	cursor.close()
	connection.close()

except psycopg2.Error as e:
	print(f"Erro ao conectar ao banco de dados: {e}")
