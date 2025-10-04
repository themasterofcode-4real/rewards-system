from flask import Flask, render_template_string
import subprocess
import threading
import os

app = Flask(__name__)

# Adjust this path to where your main.py is
MAIN_PY_PATH = os.path.join(os.path.dirname(__file__), "main.py")

process = None

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Rewards System Launcher</title>
</head>
<body>
    <h1>Kids Rewards System</h1>
    <p>Click the button below to start the program.</p>
    <form action="/start" method="post">
        <button type="submit">Start Program</button>
    </form>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/start", methods=["POST"])
def start_program():
    global process
    if process is None or process.poll() is not None:
        # Start main.py in a new thread so Flask doesn't block
        threading.Thread(target=lambda: subprocess.run(["python", MAIN_PY_PATH])).start()
        return "<p>Program started! Check the server to see the GUI.</p><a href='/'>Go Back</a>"
    else:
        return "<p>Program is already running.</p><a href='/'>Go Back</a>"

if __name__ == "__main__":
    # Use port 8080 for Vercel
    app.run(host="0.0.0.0", port=8080)
