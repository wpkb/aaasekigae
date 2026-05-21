from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# UptimeRobot用の死活監視ルート
@app.route('/ping')
def ping():
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
