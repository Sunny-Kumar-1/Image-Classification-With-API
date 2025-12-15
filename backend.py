from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for frontend-backend communication

# Nyckel API details
TOKEN_URL = 'https://www.nyckel.com/connect/token'
INVOKE_URL = 'https://www.nyckel.com/v1/functions/recycling-identifier/invoke'
CLIENT_ID = ''
CLIENT_SECRET = ''


def get_access_token():
    """
    Fetch an access token from Nyckel.
    """
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    try:
        response = requests.post(TOKEN_URL, data=data)
        response.raise_for_status()
        token = response.json().get('access_token')
        if not token:
            raise Exception("Access token not found in response.")
        return token
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching access token: {str(e)}")


@app.route('/invoke', methods=['POST'])
def invoke_api():
    """
    Invokes the Nyckel API with an image URL.
    """
    request_data = request.get_json()
    if not request_data or 'image_url' not in request_data:
        return jsonify({"error": "Image URL is required in the request body"}), 400

    image_url = request_data['image_url']

    try:
        # Get access token
        access_token = get_access_token()

        # Prepare headers and payload
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        payload = {'data': image_url}

        # Call Nyckel API
        response = requests.post(INVOKE_URL, headers=headers, json=payload)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/', methods=['GET'])
def home():
    return "Backend is running!"


if __name__ == '__main__':
    app.run(debug=True)

