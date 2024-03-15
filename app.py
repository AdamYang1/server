from flask import Flask, request, jsonify
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return """hello mf"""

@app.route('/test')
def test():
    # Get the IP address and port from the request parameters
    ip_address = "47.254.85.209"
    port = "8080"
    path = "ask"

    # Construct the full URL
    url = f'http://{ip_address}:{port}/{path}'

    # Make a GET request to the URL
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}", 500

    # Return the data from the URL
    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

