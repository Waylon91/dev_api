from httpbin.api import BaseApi


class ApiHttpbinGet(BaseApi):
    url = "http://httpbin.org/get"
    method = "GET"
    params = {}
    headers = {"accept": "application/json"}


class ApiHttpbinPost(BaseApi):
    url = "http://httpbin.org/post"
    method = "POST"
    params = {}
    headers = {"accept": "application/json"}
    data = "abc=123"
    json = {"abc": 123}


class ApiHttpbinGetCookies(BaseApi):
    url = "http://httpbin.org/cookies"
    method = "GET"
    params = {}
    headers = {"accept": "application/json"}
