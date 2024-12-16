from flask import Flask, jsonify, request
from transformers import pipeline
from utils import preprocess_text  # Import your custom preprocessing function
import pickle

# Load the model and tokenizer
model_filename = '/home/maria/Documents/code/NLPsummariser/summarizer.sav'  # my local model path

with open("/home/maria/Documents/code/NLPsummariser/summarizer.sav", "rb") as f:
    summarizer = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize_review():
    # Get the review text from the request
    data = request.json
    review_text = data.get("text", "")

    # Preprocess the text using your utility function
    review_text = preprocess_text(review_text)

    # Summarize the text
    summary = summarizer(review_text, max_length=50, min_length=10, do_sample=False)
    return jsonify({"summary": summary[0]['summary_text']})

if __name__ == "__main__":
    app.run(debug=True)
