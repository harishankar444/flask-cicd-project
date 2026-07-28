from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My Website</h1>
    <h2>CI/CD using Jenkins + AWS EC2</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)