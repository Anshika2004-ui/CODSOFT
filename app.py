from flask import Flask, render_template, request

app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower()
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello there! I am ANSHIKA, a rule-based chatbot."
    elif 'how are you' in user_input:
        return "I'm just a bunch of code, but I'm doing fine!"
    elif 'your name' in user_input:
        return "I'm a rule-based chatbot created by Anshika."
    elif 'bye' in user_input or 'exit' in user_input:
        return "Goodbye! Have a great day."
    else:
        return "I'm not available to chat right now."

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        response = get_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)