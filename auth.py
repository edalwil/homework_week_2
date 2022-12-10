from flask import Flask, request, after_this_request
from flask_api import status
import datetime
import jwt

app = Flask(__name__)


@app.route("/login")
def login():

    payload = {
        "id": request.headers["uuid"],
        "exp": datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow(),
    }

    token = jwt.encode(payload, "secret", algorithm="HS256").decode("utf-8")

    # return response
    @after_this_request
    def add_cookie(response):
        response.set_cookie('jwt', token)
        return response

    response = {'jwt': token}
    return response


@app.route("/auth")
def auth():
    try:
        token = request.cookies.get('jwt')
        payload = jwt.decode(token, 'secret', algorithm='HS256')
 # type: ignore
        if payload['id'] != request.headers['uuid']:
            return {'authenticated': False}, status.HTTP_401_UNAUTHORIZED

    except jwt.ExpiredSignatureError:
        return {'authenticated': False}, status.HTTP_401_UNAUTHORIZED

    return {'authenticated': True}, status.HTTP_200_OK


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9001, debug=True)
