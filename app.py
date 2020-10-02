from flask import Flask
from flask import render_template, jsonify, request
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


@app.route('/mail_chimp_api', methods=["POST"])
def mail_chimp_api():
    try:
        data = request.json
        url = 'https://us17.api.mailchimp.com/3.0/lists/eedbc7a412/members'
        auth = ('Geekeedatascience1307', '45ad8a1e64d059a203aa6fc5bdf56ffd')
        requests.post(url, auth=auth, json=data)
        return jsonify({"success": True, "data": [], "message": "Thanks For Subscribed"})
    except Exception as e:
        return jsonify({"status": "failure", "message": "internal server error" + str(e)})


if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0',threaded=True, port=8080)