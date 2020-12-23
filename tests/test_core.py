from httpbin.api import BaseApi


def test_version():
    from httpbin import __version__
    assert isinstance(__version__, str)


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


def test_httpbin_get():
    ApiHttpbinGet().run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().url", "http://httpbin.org/get") \
        .validate("json().headers.Accept", "application/json")


def test_httpbin_get_with_parms():
    ApiHttpbinGet() \
        .set_params(abc=123, xyz=456) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().url", "http://httpbin.org/get?abc=123&xyz=456") \
        .validate("json().headers.Accept", "application/json")


def test_httpbin_post():
    ApiHttpbinPost() \
        .set_data({"abc": 456}) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().url", "http://httpbin.org/post") \
        .validate("json().headers.Accept", "application/json")
