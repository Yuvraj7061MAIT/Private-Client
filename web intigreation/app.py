from flask import Flask, render_template, request, jsonify
from transformers import MBart50TokenizerFast, MBartForConditionalGeneration

app = Flask(__name__)

# Load the model (only once)
model_name = "SnypzZz/Llama2-13b-Language-translate"
model = MBartForConditionalGeneration.from_pretrained(model_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        # Load the tokenizer for each translation request
        tokenizer = MBart50TokenizerFast.from_pretrained(model_name, src_lang="en_XX")

        text = request.json['text']
        inputs = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"])
        translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        return jsonify(translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
