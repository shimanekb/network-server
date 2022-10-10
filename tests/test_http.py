from textwrap import dedent

import pytest

import server.http as http


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
                      GET /foo/stuff.html\r
                      Host: www.localhost:9090\r
                      Connection: close\r
                      User-agent: Chrome\r
                      Accept-language: en\r"""
        raw_request = dedent(raw_request)

        # When
        http.HttpRequest(raw_request)


def test_http_response_str_not_found():
    # Given
    raw_resp = """\
        HTTP/1.0 404 Not Found\r
        Connection: close\r\r\r\r
        """
    raw_resp = dedent(raw_resp).replace('\n', '')

    response = http.HttpResponse()

    # When
    result = str(response)

    # Then
    assert result == raw_resp
