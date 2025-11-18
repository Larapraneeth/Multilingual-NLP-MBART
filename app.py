from flask import Flask, render_template, request
from transformers import MBart50TokenizerFast, MBartForConditionalGeneration

app = Flask(__name__)

# ---------------- MODEL LOADING ---------------- #
# Load model once, outside the reloader
print("Loading mBART-50 model... This may take some time.")
model_name = "facebook/mbart-large-50-many-to-many-mmt"

tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

print("Model loaded successfully!")


# -------------- SUPPORTED LANGUAGES ------------- #
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
    "Japanese": "ja_XX",
}


# ---------------- TRANSLATION LOGIC -------------- #
def translate_text(text, src, tgt):
    tokenizer.src_lang = src

    encoded = tokenizer(text, return_tensors="pt")

    generated_tokens = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.lang_code_to_id[tgt]
    )

    return tokenizer.decode(generated_tokens[0], skip_special_tokens=True)


# ---------------------- ROUTES ---------------------- #
@app.route("/", methods=["GET", "POST"])
def index():
    translation = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        src_lang = request.form.get("src_lang")
        tgt_lang = request.form.get("tgt_lang")

        if text.strip():
            translation = translate_text(text, src_lang, tgt_lang)

    return render_template("index.html", languages=LANGUAGES, translation=translation)


# -------------------- RUN SERVER -------------------- #
if __name__ == "__main__":
    # Turn OFF debug for heavy model apps (prevents reloading twice)
    app.run(debug=False, port=5001)
