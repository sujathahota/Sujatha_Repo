from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
     return "API created"

if name  == '__main__':
       app.run()