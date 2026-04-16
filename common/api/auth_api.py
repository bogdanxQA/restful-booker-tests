import requests

class Auth():
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get_auth_token():

        auth_url = "https://restful-booker.herokuapp.com/auth"

        auth_json = {
                    "username" : "admin",
                    "password" : "password123"
                    }
        
        res = requests.post(url=auth_url, json=auth_json, headers=Auth.headers, cookies=Auth.cookie)
        token = res.json().get("token")
        return token
    

        


