FROM apache/airflow:latest

RUN pip install apache-airflow-providers-docker

# we need this to build an image which runs the container