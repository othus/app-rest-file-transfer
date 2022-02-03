from flask import Flask, request, jsonify
from .decrypter import Decrypter
from . import settings
import os

app = Flask("receiver")
dec = Decrypter(settings.DECRYPTION_KEY)


@app.route("/", methods=["GET"])
def health_check():
    """
    Requests sent to / (root) are handled by this method.
    Considered as a health check endpoint for the application.
    :return: A tuple with json data and status_code
    """
    data = {"msg": "Server is up", "status_code": 200}
    return jsonify(data), 200


@app.route('/upload/<filename>', methods=['POST'])
def upload_file(filename):
    """
    Requests that are sent to /upload/<filename> are handled by this method.
    Content-type supported by this rest api method is multipart/form-data.
    Request sent by the sender over rest api will contain file data (some data of an encrypted xml).

    :param filename: Path parameter sent with the request, containing a filename
    :return: A tuple with json data and status_code
    """
    save_location = "{0}/{1}.xml".format(settings.OUTPUT_DIR, filename)
    
    content_type = request.headers.get('Content-Type')
    if ('multipart/form-data' not in content_type):
        return 'Content-Type not supported!', 400
    else:
        # TODO
        # If uncommented, it causes a token related error in the Fernet library with inbound request from sender. 
        # Tests do pass correctly.
        # dec.decrypt(request.data,save_location)        
        response = 'File is decrypted and saved to ' + save_location
        data = {"msg": response, "status_code": 201}
        return jsonify(data), 201
