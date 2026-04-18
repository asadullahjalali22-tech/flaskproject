from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "welcome to home "

@app.route("/about")
def about():
    return "this is a test to check if the CI and CD work "



if __name__ == "__main__":
   app.run(host= "0.0.0.0", port=5000)
