import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
host_key = os.getenv("HOST_KEY")

def zomato_etl():


    url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"

    cusines = ["american","asian","british","chinese","indian"]

    main_list =[]

    for item in cusines:

        headers = {
        "X-RapidAPI-Key":api_key ,
        "X-RapidAPI-Host":host_key
        }   

        querystring = {"nutrition-type":"cooking","cuisineType[0]":item}
        response = requests.get(url, headers=headers, params=querystring)

        foods = response.json()['hints']
        for food in foods:
            # food_id = food["food"]["foodId"]
            # food_label = food["food"]["label"]
            # try:
            #     food_img = food["food"]["image"]
            # except KeyError:
            #     food_img=""
            # keys = ["ID", "Label", "Image"]
            # sub_list = [dict.fromkeys(keys) for _ in range(3)]
            # sub_list[0]["ID"] = food_id
            # sub_list[0]["Label"] = food_id
            # sub_list[0]["Image"] = food_img


            
            main_list.append(food["food"])





    df = pd.DataFrame(main_list)
    print(df.head())
    df.to_csv('out1.csv') #uploaded to s3 via connection string