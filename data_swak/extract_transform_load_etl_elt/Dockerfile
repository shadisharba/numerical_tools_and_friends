# from https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
# docker compose up airflow-init
# docker compose up
# https://airflow.apache.org/docs/apache-airflow/2.3.0/tutorial.html

FROM apache/airflow:2.9.1
COPY requirements.txt .
LABEL Name=airflowextracttransformload Version=0.0.1
RUN pip install -r requirements.txt
