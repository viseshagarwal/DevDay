from flask import Flask, request, render_template
import requests, uuid, json

app = Flask(__name__)

# Function to call Azure Translator
def translate_text(text, to_lang):
    subscription_key = '0c1cf144382d40d8bbcadeff2e88da76'
    endpoint = 'https://api.cognitive.microsofttranslator.com/'
    
    path = '/translate?api-version=3.0'
    params = '&to=' + to_lang
    constructed_url = endpoint + path + params
    
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    
    body = [{'text': text}]
    print
    response = requests.post(constructed_url, headers=headers, json=body)
    translation = response.json()[0]['translations'][0]['text']
    print(translation)
    return translation

# Route for translating text
@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        text_to_translate = request.form['text']
        target_language = request.form['target_language']
        print(text_to_translate, target_language)
        translated_text = translate_text(text_to_translate, target_language)
        
        return render_template('index.html', original=text_to_translate, translated=translated_text)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()