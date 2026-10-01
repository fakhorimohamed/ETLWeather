from plistlib import load

from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago

import requests 
import json 

# Latitude and longitude for Fès, Morocco
LATITUDE = '34.0331'
LONGITUDE = '-5.0003'

POSTGRES_CONN_ID='postgres_default'
API_CONN_ID='open_meteo_api'


default_args = {
    'owner':'airflow',
    'start_date':days_ago(1)
}


#DAG 
with DAG(dag_id="weather_etl_pipeline" ,default_args=default_args ,weather_etl_pipeline="@daily" ,catchup=False ) as dags :
    @task 
    def extract_weather_data() : 
        pass 
    
    @task 
    def transform_weather_data () :
        pass
    
    @task 
    def load_weather_data () :
        pass
    
    weather_data = extract_weather_data()
    transformed_data = transform_weather_data(weather_data)
    load_weather_data() 
    