from flask import Flask, request, render_template
import requests, uuid, json
import logging

app = Flask(__name__)
# Configure logging
logging.basicConfig(filename='error.log', level=logging.DEBUG)

# Function to call Azure Translator
def translate_text(text, to_lang):
    subscription_key = '23adb506265e46d48f2252d8f9314805'
    endpoint = 'https://api.cognitive.microsofttranslator.com/'
    location='southeastasia'
    
    path = '/translate'
    
    constructed_url = endpoint + path

    params = {
        'api-version':'3.0',
        'from':'en',
        'to':to_lang
    }
    
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    
    body = [{'text': text}]
    
    try:
        request = requests.post(constructed_url, params=params,headers=headers, json=body)
        request.raise_for_status()  # Raise HTTPError for bad responses
        translation = request.json()[0]['translations'][0]['text']
        print(translation)
        return translation
    except Exception as e:
        logging.error(f"Error in translate_text function: {e}")
        return None

# Route for translating text
@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        text_to_translate = request.form['text']
        print(text_to_translate)
        target_language = request.form['target_language']
        print(text_to_translate, target_language)
        translated_text = translate_text(text_to_translate, target_language)
        if translated_text is None:
            return "Translation failed. Please check logs for details."
        return render_template('index.html', original=text_to_translate, translated=translated_text)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)