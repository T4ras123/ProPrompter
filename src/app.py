import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    blocks = request.get_json().get('blocks', [])
    formatted_blocks = []
    for block in blocks:
        name = block['name']
        content = block['content']
        formatted_block = f"<{name}>\n{content}\n</{name}>"
        formatted_blocks.append(formatted_block)
    formatted = '\n\n'.join(formatted_blocks)
    return jsonify({'formatted': formatted})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)