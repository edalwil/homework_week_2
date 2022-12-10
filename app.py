import requests

from flask import Flask, request
from flask_api import status
from controllers.end_point_controller_poke import controller_poke
from controllers.end_point_status_ import end_point_status


app = (Flask(__name__))


@app.route("/poke")
def poke():
    response = controller_poke(request.headers)
    return response


@app.route("/status")
def statu():
    return end_point_status()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True)
