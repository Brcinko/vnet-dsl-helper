from flask import Flask, request, jsonify, json, render_template, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__, template_folder='frontend')
cors = CORS(app, resources={r"/*": {"origins": "*",
                                    "methods": " [GET, HEAD, POST, OPTIONS, PUT, PATCH, DELETE]",
                                    "headers": "*"}})


@app.route('/info', methods=['GET'])
def info():
    if request.method == 'GET':
        return "VNET DSL-XML-CREATOR beta 0.1"

