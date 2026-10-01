# Weather ETL Pipeline

A small **ETL pipeline built with Apache Airflow** to collect and process weather data from the [Open-Meteo API](https://open-meteo.com/).

I started this project while learning **Apache Airflow and ETL pipelines**. Instead of learning the concepts only theoretically, I chose to build a simple project to understand how data extraction, transformation, loading, scheduling, Hooks, and Connections work together in a real pipeline.

### Pipeline

```text
Open-Meteo API
      ↓
   Extract
      ↓
  Transform
      ↓
    Load
      ↓
 PostgreSQL
```

### Technologies

* Apache Airflow
* Astro CLI
* Python
* PostgreSQL
* Open-Meteo API

This project is mainly focused on **learning data engineering and workflow orchestration concepts**.
