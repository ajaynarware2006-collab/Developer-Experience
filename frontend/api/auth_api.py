from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")

def check_user(email):

    response = requests.get(f"{API_BASE_URL}/checkuser/{email}",timeout=3)

    response.raise_for_status()

    return response

def signup_user(name , email , password):

    data = {
        "name" : name,
        "email" : email,
        "password" : password,
        }

    user = requests.post(f"{API_BASE_URL}/signup",json=data)
    

    return user
