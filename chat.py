from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response

app = Flask("_name_")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_msg = request.args.get('msg')
    response = chatbot_response(user_msg)
    return jsonify(response)

if "_name_" == "_main_":
    app.run(debug=True)
