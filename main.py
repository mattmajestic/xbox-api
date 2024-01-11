from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
import requests
import os
from dotenv import load_dotenv

app = FastAPI()

# Load the environment variables from .env file
load_dotenv()

# Define the base URL
base_url = "https://xbl.io/api/v2/"

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url='/docs')

@app.get("/get-xbox-account-info")
async def get_xbox_account_info():
    # Get PUBLIC_KEY from the .env file or use a default
    public_key = os.getenv('PUBLIC_KEY', 'default_public_key')

    # Headers with Public Key
    headers = {'X-Authorization': public_key}

    # Making the GET request to the account endpoint
    response = requests.get(f"{base_url}account", headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the response data
        return response.json()
    else:
        return {"error": f"Failed to retrieve data: Status code {response.status_code}"}

@app.get("/player-summary")
async def player_summary():
    # Get PUBLIC_KEY from the .env file or use a default
    public_key = os.getenv('PUBLIC_KEY', 'default_public_key')

    # Headers with Public Key
    headers = {'X-Authorization': public_key}

    # Making the GET request to the player summary endpoint
    response = requests.get(f"{base_url}player/summary", headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the response data
        return response.json()
    else:
        return {"error": f"Failed to retrieve data: Status code {response.status_code}"}

@app.get("/friends")
async def friends():
    # Get PUBLIC_KEY from the .env file or use a default
    public_key = os.getenv('PUBLIC_KEY', 'default_public_key')

    # Headers with Public Key
    headers = {'X-Authorization': public_key}

    # Making the GET request to the friends endpoint
    response = requests.get(f"{base_url}friends", headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the response data
        return response.json()
    else:
        return {"error": f"Failed to retrieve data: Status code {response.status_code}"}
