from flask import Flask, request, redirect, render_template
import base64
import hashlib

app = Flask(__name__)

url_database = {}  # In-memory storage for long URLs and their corresponding short codes


def generate_short_code(url):
    # Generate a unique short code using Base64 encoding
    hashed = hashlib.sha256(url.encode()).digest()
    return base64.urlsafe_b64encode(hashed)[:6].decode()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form.get('long_url')
        if long_url:
            short_code = generate_short_code(long_url)
            url_database[short_code] = long_url
            short_url = f'/{short_code}'
            return render_template('index.html', short_url=short_url)
    return render_template('index.html', short_url=None)


@app.route('/<code>', methods=['GET'])
def redirect_to_long_url(code):
    long_url = url_database.get(code)
    if long_url:
        return redirect(long_url, code=302)
    else:
        return render_template('error.html', error='Short URL not found'), 404


if __name__ == '__main__':
    app.run(debug=True)

