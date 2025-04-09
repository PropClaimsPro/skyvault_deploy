from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ SkyVault Deployed Successfully (Flask Server Live)"

@app.route('/test')
def test():
    return "Test route active"
    
