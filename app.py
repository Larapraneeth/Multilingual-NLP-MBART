from flask import Flask, render_template, request, jsonify
from transformers import MBart50TokenizerFast, MBartForConditionalGeneration
import torch
import speech_recognition as sr
import uuid, os

app = Flask(__name__)

# Load model
print("Loading mBART-50...")
model_name = "facebook/mbart-large-50-many-to-many-mmt"

tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

print("mBART50 Loaded Successfully!")


LANGUAGES = {
    "English": "en_XX",
    "Hindi": "hi_IN",
    "Telugu": "te_IN",
    "Tamil": "ta_IN",
    "Spanish": "es_XX",
    "French": "fr_XX",
    "German": "de_DE",
    "Italian": "it_IT",
    "Chinese": "zh_CN",
    "Japanese": "ja_XX"
}


# Translation Function
def translate_text(text, src, tgt):
    tokenizer.src_lang = src
    encoded = tokenizer(text, return_tensors="pt").to(device)

    output = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.lang_code_to_id[tgt]
    )

    return tokenizer.decode(output[0], skip_special_tokens=True)



# Home Route
@app.route("/", methods=["GET", "POST"])
def index():
    translation = ""

    if request.method == "POST":
        text = request.form.get("text")
        src = request.form.get("src_lang")
        tgt = request.form.get("tgt_lang")

        if text.strip():
            translation = translate_text(text, src, tgt)

    return render_template("index.html", languages=LANGUAGES, translation=translation)



# Speech-to-Text Route
@app.route("/speech_to_text", methods=["POST"])
def speech_to_text():
    if "audio" not in request.files:
        return jsonify({"error": "No audio"}), 400

    audio_file = request.files["audio"]

    # Save WAV
    filename = f"{uuid.uuid4()}.wav"
    path = f"temp_{filename}"
    audio_file.save(path)

    recog = sr.Recognizer()

    try:
        with sr.AudioFile(path) as src:
            audio = recog.record(src)
            text = recog.recognize_google(audio)

    except Exception as e:
        text = f"(Error: {e})"

    if os.path.exists(path):
        os.remove(path)

    return jsonify({"text": text})



if __name__ == "__main__":
    app.run(debug=False, port=5001)
