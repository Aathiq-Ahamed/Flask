from flask import Flask
from flask_cors import CORS, cross_origin
from helperFunction import *
from datetime import datetime


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/member")
@cross_origin()
def print_name():
      expectedData = [
        "name",
        "email",
        "date",
    ]
    receivedData = request.get_json()

    try:
        userType = receivedData["userType"]
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        print("[SERVER] - Required Data Could Not Be Extracted from POST data!")
        return server_response(status=500)

    columns = list(receivedData.keys())
    values = list(receivedData.values())

      try:
        if userType == "lecturer":
            insert_into_table("lecturers", columns, values)
        elif userType == "student":
            insert_into_table("students", columns, values)
        else:
            raise Exception("InvalidUserType")
    except:
        return server_response(status=500)

    name = "Aathiq"
    # return {"name": ["Aathiq"]}
    # return server_response(status=200, json={"userSessionKey": userSessionCode})
    return {"name": name}, 200


print(__name__)
if __name__ == "__main__":
    app.run(debug=True)
