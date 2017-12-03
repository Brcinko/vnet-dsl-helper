from flask import Flask, request, jsonify, json, render_template, Response
from flask_cors import CORS, cross_origin
import settings
from pprint import pprint

app = Flask(__name__)
cors = CORS(app)


@cross_origin()
@app.route('/info', methods=['GET'])
def info():
    if request.method == 'GET':
        return "VNET DSL-XML-CREATOR beta 0.1"


@cross_origin()
@app.route('/create_dsl_request', methods=['POST'])
def create_dsl_request():
    if request.method == 'POST':
        # pprint()
        req = request.get_json()
        print req
        return "Created DSL Request successful."


if __name__ == '__main__':
    print "Starting VNET DSL Requests Creator. Running at " + str(settings.PORT) + ". Debug - " + str(settings.DEBUG)
    app.run(debug=settings.DEBUG, port=settings.PORT)
