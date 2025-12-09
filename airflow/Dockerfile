FROM apache/airflow:2.7.1

USER root
# Install git for dbt deps if needed
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

USER airflow

# Install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
