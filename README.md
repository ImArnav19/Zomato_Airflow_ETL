# Zomato_Airflow_ETL
Scraped data from Zomato public api, transformed it to familiar terms to be required for analysis.

APi INFO from Zomato_API

1. Through scraping and gathering data used python for making functions to do so
<img width="959" alt="Screenshot 2023-11-01 235556" src="https://github.com/ImArnav19/Zomato_Airflow_ETL/assets/117253613/7dd851d4-cd10-4aea-961e-8c431af224f4">


2. Once data ready , launced an EC2 where airflow server was setup and the dag files were uploaded on the /airflow directory

<img width="885" alt="Screenshot 2023-11-01 233253" src="https://github.com/ImArnav19/Zomato_Airflow_ETL/assets/117253613/4edb4201-16d2-47c1-8951-c8f0222a5a5d">

3. Once everything was ready and the dag file was visible on port 8080, i can run the commands anytime, and my etl will give me health checks and i connect with various sources as well

<img width="954" alt="Screenshot 2023-11-02 000139" src="https://github.com/ImArnav19/Zomato_Airflow_ETL/assets/117253613/239f9359-6f6e-4d66-81b7-88cf9df2e3c9">
