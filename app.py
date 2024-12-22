from flask import Flask, jsonify

from flask_cors import CORS
app =Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello Perros</p>"

@app.route("/things")
def hello():
    return jsonify({
        "payload":["foo","echo","bar","baz"]
    })

if __name__ =="__main__":
    app.run(debug=True)