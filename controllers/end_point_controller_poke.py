import requests
from flask import Flask, request



def controller_poke(headers):
    
    _url = 'http://127.0.0.1:9001/auth'
    _headers = {'uuid':headers['uuid']}
    _token = request.cookies.get('jwt')
    _response = requests.get(url=_url, headers=_headers, cookies={'jwt':_token})
 # type: ignore
    _response = _response.json()

    if not _response['authenticated']:
        return _response

    try:
        endpoint_poke_api = headers["endpoint_poke_api"]
        exists_ability_name = headers["ability_name"]
        print(endpoint_poke_api)
        ability_range = headers["ability_range"]

        ability_range = int(ability_range)

        response = requests.get(endpoint_poke_api)
        response = response.json()

        abilities = response["abilities"][ability_range]
        ability_name = abilities["ability"]["name"]

    except Exception as e:
        return {"error": e.args[0]}, 400
    else:
        if exists_ability_name == ability_name:
            return {"exists_ability_name": True}, 200
        else:
            return {"exists_ability_name": False}, 200
