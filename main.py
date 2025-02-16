from chatbot import chatbot_response
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/send")
def get_bot_response():
  userText = request.args.get('msg')
  history = [] 
   
  return chatbot_response(userText, history)

if __name__ == "__main__":
  app.run(debug=True)