from flask import Flask
from skyvault_core.engine import roi_engine  # Import backend logic

app = Flask(__name__)
app.register_blueprint(roi_engine)

@app.route('/')
def home():
    return "✅ SkyVault Deployed Successfully (Flask Server Live)"

@app.route('/test')
def test():
    return "Test route active"
