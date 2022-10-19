from enum import Enum
import socket

import server.object as object


class HttpController:
    """Controler that coordinates request processing."""
    def __init__(self, object_repo: object.ObjectRepo):
        self._object_repo = object_repo

    def process_request(self, connection: socket.SocketType):
        """Processes a request to a connection back to client."""
        resp = HttpResponse()
        try:
            raw_req = connection.recv(1024).decode('utf-8')
            req = HttpRequest(raw_req)
            object = self._object_repo.find_by_name(req.url[1:])
            resp = HttpResponse(object)
        except ValueError:
            resp.status = HttpStatus.BAD_REQUEST.value
        except Exception:
            resp.status = HttpStatus.INTERNAL_SERVER_ERROR.value
        finally:
            connection.send(str(resp).encode())
            connection.close()


class HttpRequest:
    """Represents incoming request, constructor parses raw
       html request into this object."""
    def __init__(self, request: str):
        self._parse(request)
        self.request = request

    def _parse(self, request: str):
        lines = request.splitlines()

        if len(lines) == 0:
            raise ValueError('Empty request.')

        req_line = lines[0].split()
        if len(req_line) != 3:
            raise ValueError('Bad request line format.')

        self.url = req_line[1]


class Status:
    """Represents web status's used in Http Response"""
    def __init__(self, code: int, phrase: str):
        self.code = code
        self.phrase = phrase


class HttpStatus(Enum):
    """Enum of possible web status codes and phrases."""
    OK = Status(200, 'OK')
    NOT_FOUND = Status(404, 'Not Found')
    BAD_REQUEST = Status(400, 'Bad Request')
    INTERNAL_SERVER_ERROR = Status(500, 'Internal Server Error')


class HttpResponse:
    """Represents Html response, with requested object."""
    def __init__(self, object: object.Object = None,
                 version: str = 'HTTP/1.0'):
        self.version = version
        self.status = HttpStatus.NOT_FOUND.value
        self.object = object
        if self.object is not None:
            self.status = HttpStatus.OK.value

    def __str__(self):
        """Translates response into raw text html to be sent."""
        content_length_line = ''
        content_type_line = ''
        content = ''
        connection = 'Connection: close'

        if self.status.code == 200:
            c_len = len(self.object.content)
            content_length_line = "Content-Length: %d" % c_len
            content_type_line = "Content-Type: %s" % self.object.type.value
            content = self.object.content

        status_line = '%s %d %s' % (self.version,
                                    self.status.code,
                                    self.status.phrase)

        response = "%s\r\n%s\r\n%s\r\n%s\r\n\r\n%s" % (status_line,
                                                       connection,
                                                       content_length_line,
                                                       content_type_line,
                                                       content)

        return response
