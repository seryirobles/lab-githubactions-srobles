import json

from lambda_function import lambda_handler

HELLO = "hello from GitHub Actions lab!"


def _body(response):
    return json.loads(response["body"])


def test_returns_200():
    response = lambda_handler({}, None)
    assert response["statusCode"] == 200


def test_says_hello():
    body = _body(lambda_handler({"rawPath": "/"}, None))
    assert body["response"] == HELLO


def test_says_hello_on_any_endpoint():
    for path in ["/", "/hello", "/foo/bar", "/anything/at/all"]:
        response = lambda_handler({"rawPath": path}, None)
        assert response["statusCode"] == 200
        assert _body(response)["response"] == HELLO


def test_supports_rest_api_event_shape():
    event = {"path": "/legacy", "httpMethod": "POST"}
    response = lambda_handler(event, None)
    assert response["statusCode"] == 200
    assert _body(response)["response"] == HELLO


def test_supports_http_api_v2_event_shape():
    event = {
        "rawPath": "/v2",
        "requestContext": {"http": {"method": "PUT"}},
    }
    response = lambda_handler(event, None)
    assert response["statusCode"] == 200
    assert _body(response)["response"] == HELLO


def test_strips_stage_prefix_from_path(caplog):
    event = {
        "rawPath": "/prod/hello",
        "requestContext": {"stage": "prod", "http": {"method": "GET"}},
    }
    with caplog.at_level("INFO"):
        response = lambda_handler(event, None)
    assert response["statusCode"] == 200
    # stage is stripped, so the logged path is "/hello", not "/prod/hello"
    assert "path: /hello" in caplog.text


def test_handles_empty_event():
    response = lambda_handler({}, None)
    assert response["statusCode"] == 200
    assert _body(response)["response"] == HELLO
