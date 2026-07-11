from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Project 1 - CI/CD Pipeline</h1>
    <h2>Application Successfully Deployed!</h2>
    <p>Jenkins + Docker + Kubernetes + AWS EC2</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
