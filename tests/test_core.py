from httpbin.httpbin import ApiHttpbinGet, ApiHttpbinPost, ApiHttpbinGetCookies 


def test_version():
    from httpbin import __version__
    assert isinstance(__version__, str)


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


def test_httpbin_parameters_extract():
    user_id = "abc123"
    ApiHttpbinGet() \
        .set_params(user_id=user_id) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().url", "http://httpbin.org/get?user_id={}".format(user_id)) \
        .validate("json().headers.Accept", "application/json") 

    ApiHttpbinPost() \
        .set_json({"user_id": user_id}) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().url", "http://httpbin.org/post") \
        .validate("json().headers.Accept", "application/json")
    

def test_httpbin_extrace():
    resp = ApiHttpbinGet().run()
    status_code = resp.extract('status_code')
    assert status_code == 200

    server = resp.extract('headers.server')
    assert server == "gunicorn/19.9.0"

    accept = resp.extract('json().headers.Accept')
    assert accept == 'application/json' 


def test_httpbin_parameters_extrace():
    freeform = ApiHttpbinGetCookies().set_cookie('freeform', '123').run().extract("json().cookies.freeform")
    assert freeform == '123'


def  test_httpbin_get_cookie():
    app_run = ApiHttpbinGetCookies()\
                .set_cookie('freeform1', "123")\
                .set_cookie('freeform2', "456")\
                .run()
    freeform1 = app_run.extract("json().cookies.freeform1")
    freeform2 = app_run.extract("json().cookies.freeform2")
    assert freeform1 == "123"
    assert freeform2 == "456"