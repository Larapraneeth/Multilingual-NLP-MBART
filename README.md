# Multilingual NLP Translation using mBART-50 and Flask

This project is a web-based multilingual machine translation application built using the mBART-50 model and the Flask web framework. It supports translation across 50 languages using a single unified transformer model. The system loads the model once at startup and provides real-time translations through a simple HTML-based user interface.

## Features
- Real-time output
- Flask-based backend
- Clean and simple web interface
- Uses mBART-50 (facebook/mbart-large-50-many-to-many-mmt)
- Model loads once for fast inference
- Built using Python, Flask, and HuggingFace Transformers

## Project Structure
Multilingual-NLP-MBART/
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│ └── index.html


markdown
Copy code

## Technologies Used
- Python
- Flask
- HuggingFace Transformers
- mBART-50 multilingual model
- SentencePiece tokenizer
- HTML/CSS

## Installation

### 1. Clone the repository
git clone https://github.com/Larapraneeth/Multilingual-NLP-MBART.git
cd Multilingual-NLP-MBART

shell
Copy code

### 2. Install dependencies
pip install -r requirements.txt

powershell
Copy code

## Running the Application
Start the Flask server:
python app.py

css
Copy code

Open a browser and go to:
http://localhost:5001

pgsql
Copy code

You can enter text, choose a source language, choose a target language, and get the translated output.

## Supported Languages (Examples)
| Language | Code |
|----------|------|
| English  | en_XX |
| Hindi    | hi_IN |
| Telugu   | te_IN |
| Tamil    | ta_IN |
| French   | fr_XX |
| Chinese  | zh_CN |
| Japanese | ja_XX |

mBART-50 supports a total of 50 languages.

## Translation Workflow
1. User enters text in the UI.
2. Text is sent to the Flask backend.
3. Text is tokenized into subword units using SentencePiece.
4. Tokens are passed to the mBART-50 model.
5. The model generates translated token IDs.
6. Tokens are decoded back to natural text.
7. Output is displayed on the webpage.





## License
This project is open-source and available under the MIT License.
