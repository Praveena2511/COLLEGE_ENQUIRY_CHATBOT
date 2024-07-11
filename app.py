from flask import Flask , render_template , jsonify , request
from chat import get_response
import os
import nltk


nltk.download('punkt')
app = Flask(__name__)

@app.get('/')
def index_get():
    return render_template('base.html')

@app.post('/predict')
def predict():
    data = request.get_json().get("message")
    response = get_response(data)
    message={"answer":response}
    return jsonify(message)


if __name__ == "__main__":
    #app.run(debug=True,port=5000)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)



    