from utils import SCORES_FILE_NAME


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