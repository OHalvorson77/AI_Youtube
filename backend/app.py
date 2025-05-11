from flask import Flask, render_template, request, jsonify
from main import main  # This should be your video upload logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        prompt = data['prompt']
        title = data['title']
        description = data['description']

        # Call your main function with the values
        main(prompt, title, description)

        return jsonify({'status': 'success', 'message': 'Video uploaded successfully!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
    
if __name__ == '__main__':
    port = 5000
    print(f"🚀 Running on http://localhost:{port}")
    app.run(debug=True, port=port)