from textwrap import dedent

import pytest

import server.http as http
import server.object as obj


def test_http_request_parse_url_from_valid_request():
    # Given
    raw_request = """\
                  GET /foo/stuff.html HTTP/1.0\r
                  Host: www.localhost:9090\r
                  Connection: close\r
                  User-agent: Chrome\r
                  Accept-language: en\r"""
    raw_request = dedent(raw_request)

    # When
    http_req = http.HttpRequest(raw_request)

    # Then
    assert http_req.url == '/foo/stuff.html'


def test_http_request_empty_request():
    with pytest.raises(ValueError):
        # Given
        raw_request = ''

        # When
        http.HttpRequest(raw_request)


def test_http_request_invalid_request_line():
    with pytest.raises(ValueError):
        # Given
        raw_request = """\
                      GET /foo/stuff.html\r\n
                      Host: www.localhost:9090\r\n
                      Connection: close\r\n
                      User-agent: Chrome\r\n
                      Accept-language: en\r\n"""
        raw_request = dedent(raw_request)

        # When
        http.HttpRequest(raw_request)


def test_http_response_str_200():
    # Given
    content = """\
        <!DOCTYPE html>
        <html>
        <body>
        <h1>My First Heading</h1>
        <p>My first paragraph.</p>
        </body>
        </html>
        """
    content = dedent(content).replace('\n', '')

    raw_resp = """\
        HTTP/1.0 200 OK\r
        Connection: close\r
        Content-Length: 92\r
        Content-Type: text/html\r\r
        <!DOCTYPE html>
        <html>
        <body>
        <h1>My First Heading</h1>
        <p>My first paragraph.</p>
        </body>
        </html>
        """
    raw_resp = dedent(raw_resp).replace('\n', '').replace('\r', '\r\n')
    ob = obj.Object(obj.ContentType.TEXT_HTML, content)

    response = http.HttpResponse(ob)

    # When
    result = str(response)

    # Then
    assert result == raw_resp


def test_http_response_str_server_error():
    # Given
    raw_resp = """\
        HTTP/1.0 500 Internal Server Error\r
        Connection: close\r\r\r\r
        """
    raw_resp = dedent(raw_resp).replace('\n', '').replace('\r', '\r\n')

    response = http.HttpResponse()
    response.status = http.HttpStatus.INTERNAL_SERVER_ERROR.value

    # When
    result = str(response)

    # Then
    assert result == raw_resp


def test_http_response_str_not_found():
    # Given
    raw_resp = """\
        HTTP/1.0 404 Not Found\r
        Connection: close\r\r\r\r
        """
    raw_resp = dedent(raw_resp).replace('\n', '').replace('\r', '\r\n')

    response = http.HttpResponse()

    # When
    result = str(response)

    # Then
    assert result == raw_resp
