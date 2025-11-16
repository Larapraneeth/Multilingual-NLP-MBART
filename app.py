from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.json
        print("Received data:", data)

        text = data.get("text")
        src_lang = data.get("src_lang")
        tgt_lang = data.get("tgt_lang")

        if not text or not src_lang or not tgt_lang:
            return jsonify({"error": "Missing parameters"}), 400

        # Perform translation
        translation = GoogleTranslator(source=src_lang, target=tgt_lang).translate(text)

        return jsonify({"translation": translation})

    except Exception as e:
        print("Exception:", e)
        return jsonify({"error": "Server error", "details": str(e)}), 500

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == "__main__":
    app.run(debug=True, port=5001)
