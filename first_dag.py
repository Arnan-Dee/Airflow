from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def print_firstdag():
    return 'My First DAG from HevoData!'

dag = DAG('first_dag', description='HevoData Dag',
          start_date=datetime(2022, 2, 24), catchup=False)

print_operator = PythonOperator(task_id='first_task', python_callable=print_firstdag, dag=dag)

print_operator