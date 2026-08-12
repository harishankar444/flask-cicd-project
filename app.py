from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS CI/CD Project</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                text-align: center;
                padding-top: 100px;
            }

            .container {
                background: white;
                width: 600px;
                margin: auto;
                padding: 50px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            }

            h1 {
                color: #222;
            }

            .status {
                color: green;
                font-weight: bold;
                font-size: 20px;
            }

            .tech {
                margin-top: 25px;
                font-size: 18px;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🚀 AWS CI/CD Project</h1>

            <p>Automated Flask Web Application Deployment</p>

            <p class="status">● LIVE</p>

            <div class="tech">
                GitHub → Jenkins → AWS EC2
            </div>

            <p>Deployment completed successfully!</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)