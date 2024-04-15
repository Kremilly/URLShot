from io import BytesIO

from flask import Flask, request, send_file

from urlshot.screenshot import Screenshot

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def take_screenshot():
    url = request.args.get('url')
    
    width = int(
        request.args.get('width', 1024)
    )
    
    height = int(
        request.args.get('height', 768)
    )

    screenshot = Screenshot.take(url, width, height)
    
    return send_file(
        BytesIO(screenshot), mimetype='image/png'
    )

if __name__ == '__main__':
    app.run(debug=True)
