from flask import Flask, request
from flask_cors import CORS, cross_origin
from helperFunction import *
from datetime import datetime


appp = Flask(__name__)
cors = CORS(appp)
appp.config["CORS_HEADERS"] = "Content-Type"


@appp.route("/member", methods=["POST"])
@cross_origin()
def print_name():
    expectedData = [
        "name",
    ]
    receivedData = request.get_json()

    try:
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        print("[SERVER] - Required Data Could Not Be Extracted from POST data!")
        return server_response(status=500)

    columns = list(receivedData.keys())
    values = list(receivedData.values())

    try:
        insert_into_table("Clients", columns, values)
    except:
        return server_response(status=500)

    name = "aathiq"
    # return {"name": ["Aathiq"]}
    # return server_response(status=200, json={"userSessionKey": userSessionCode})
    return {"name": name}, 200


print(__name__)
if __name__ == "__main__":
    appp.run(port=5000)
