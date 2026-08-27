from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")

def send_verification_code(email : str , user_id : int):

    data = {
        "email" : email,
        "user_id" : user_id
    }

    requests.post(f"{API_BASE_URL}/sendcode",json=data)


def verify_varification_code(user_id , entered_code):

    data={
        "user_id" : user_id,
        "code_entered" : entered_code
    }

    succsess , message = requests.post(f"{API_BASE_URL}/verifycode",json=data)

    return succsess , message