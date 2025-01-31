from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/login', methods=['POST'])
def login():
    # Assuming the POST request contains JSON data with keys 'username' and 'password'
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Perform authentication logic here
    # For demonstration purposes, let's just return a success message
    if username == 'nurse123' and password == 'password':
        return jsonify({'ok': True})
    else:
        return jsonify({'ok': False}), 401
	
@app.route('/connect', methods=['POST'])
def connectToModel():
	print("Do something here to connect to model")
    
    # add code here to connect to AI model
    # return a JSON object with key 'advice' and 'value' whatever you is returned from the model

	return jsonify({
        'advice': 'slkdjslkfjsljfdslkjfflk'
    })
	
if __name__ == '__main__':
    app.run(port=3000)