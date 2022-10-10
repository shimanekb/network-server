from textwrap import dedent
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
