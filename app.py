from flask import Flask, request, jsonify
import requests
from typing import Dict, Union, List
app = Flask(__name__)


@app.route('/')
def index():
    return """hello mf"""

@app.route('/test', methods=['POST'])
def test():
    # Get the JSON data from the request
    data = request.get_json()

    # If the request doesn't have JSON data, return an error
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    if data is None:
            return jsonify({"error": "Request must contain JSON data"})
    if 'message' not in data:
        return jsonify({"error": "Request must contain a 'message' key"})
    
    user_input = data['message']
    conversation_id = data.get('conversation_id', None)

    # TODO 模拟获取美国server的ip地址
    ip_address = data.get('ip_address', '47.254.85.209')
    port = data.get('port', '8080')
    path = data.get('path', 'test')
    url = f'http://{ip_address}:{port}/{path}'

    # Get the request body to send as JSON
    request_body: Dict[str, Union[str, int, List[str]]] = {}
    request_body['message'] = user_input
    request_body['conversation_id'] = conversation_id

    # Make a POST request to the URL with JSON data
    try:
        response = requests.post(url, json=request_body)
        response.raise_for_status()
        data = response.text
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

    # Return the data from the URL
    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

