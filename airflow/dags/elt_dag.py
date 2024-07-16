from datetime import datetime, timedelta
from airflow import DAG
from docker.types import Mount
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
import subprocess

default_args={
    'owner':'airflow',
    'depends_on_past':False,
    'email_on_failure': False,
    'email_on_retry':False,
}

def run_elt_script():
    # this function is to run the elt_script 
    script_path = "/opt/airflow/elt/elt_script.py"
    result = subprocess.run(["python",script_path], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Script failed with error:{result.stderr}")
    else:
        print(result.stdout)

dag = DAG(
    'elt_and_dbt',
    default_args=default_args,
    description='An ELT workflow with dbt',
    start_date=datetime(2024, 7, 15),
    catchup=False,
)


# now we erite the tasks

# first task that we want is elt_script 

t1 = PythonOperator(
    task_id='run_elt_script',
    python_callable = run_elt_script,
    dag= dag,
)

# task 2 is DBT

t2 = DockerOperator(
    task_id = 'dbt_run',
    # we did not create any function to for DBT so we kinda have to do everything here
    image='ghcr.io/dbt-labs/dbt-postgres:1.5.0',
    command=
    [
        "run",
        "--profiles-dir",
        "/root",
        "--project-dir",
        "/dbt"
    ],
    auto_remove = True, # to automatically remove container once it's finished
    docker_url = "unix://var/run/docker.sock",
    network_mode = "bridge",
    mounts=[
        Mount(source='/Users/navyasri/Desktop/CODE/Docker/ELT/custom_postgres',
              target='/dbt', type='bind'),
        Mount(source='/Users/navyasri/.dbt',
              target='/root', type='bind')
    ],
    dag=dag

)

t1 >> t2 #t1 take priority over t2