from utils import SCORES_FILE_NAME
from flask import Flask


def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            SCORE = int(file.read())            
            return f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is:</h1>
                    <div id="score">{SCORE}</div>
                </body>
            </html>
            """
    except Exception as ERROR:
        return f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>ERROR:</h1>
                <div id="score" style="color:red">{ERROR}</div>
            </body>
        </html>
        """
    
app = Flask(__name__)

@app.route('/')
def run_app():
    return score_server()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)