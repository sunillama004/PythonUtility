from flask import Flask, render_template, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to handle cross-origin issues

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    # Execute the Python script
    try:
        result = subprocess.run(['python3', 'script.py'], capture_output=True, text=True)
        output = result.stdout
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"output": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
