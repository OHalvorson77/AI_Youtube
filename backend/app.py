from flask import Flask, render_template, request, jsonify
from main import main  # This should be your video upload logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Call your main upload logic
        main()
        return jsonify({'status': 'success', 'message': 'Video uploaded successfully!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
