from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago

url_data = "URL_DATA"
output_name_extract = "OUTPUT_NAME_EXTRACT"
output_name_transform = "OUTPUT_NAME_TRANSFORM"
data_staging_path = "DATA_STAGING"

username = "MONGODB_USER"
password = "MONGODB_PASSWORD"
database = "MONGODB_DATABASE"
collection_name = "MONGODB_COLLECTION"

default_args = {
    "owner": "owner_name",
    "start_date": days_ago(1),
}


def download_from_drive(url_data, output_name, data_staging_path):
    print(f"DEBUG_statement: Downloading data from {url_data} to {data_staging_path}/{output_name}")
    return f"{data_staging_path}/{output_name}"


def transform_data(selected_columns, transform_path, data_staging_path, table_path):
    print(f"DEBUG_statement: Transforming data from {data_staging_path}/{table_path} to {data_staging_path}/{transform_path}")
    return f"{data_staging_path}/{transform_path}"


def load_to_mongodb(username, password, database, collection_name, transform_data_path):
    print(f"DEBUG_statement: Loading data from {transform_data_path} to MongoDB {database}.{collection_name}")


@task()
def extract(url_data, output_name, data_staging_path):
    return download_from_drive(url_data, output_name, data_staging_path)


@task()
def transform(selected_columns, transform_path, data_staging_path, table_path):
    return transform_data(selected_columns, transform_path, data_staging_path, table_path)


@task()
def load(username, password, database, collection_name, transform_data_path):
    load_to_mongodb(username, password, database, collection_name, transform_data_path)


with DAG(dag_id="apache_airflow_tutorial1", schedule_interval="@once", default_args=default_args, catchup=False) as dag:

    extract_data_path = extract(url_data, output_name_extract, data_staging_path)
    transform_data_path = transform(["BHK", "Size", "Bathroom", "Rent"], output_name_transform, data_staging_path, extract_data_path)
    load(username, password, database, collection_name, transform_data_path)
