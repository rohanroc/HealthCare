from flask import Flask,jsonify,render_template,request
from chat import get_response
from flask_cors import CORS
app=Flask(__name__)

# @app.get("/")
# def index_get():
#     return render_template("index.html")

CORS(app)

@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    print(text)
    response=get_response(text)
    message={"answer":response}
    return jsonify(message)

    

if __name__=="__main__":
    app.run(debug=True)