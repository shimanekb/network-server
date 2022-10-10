from enum import Enum
import server.object as object


class HttpRequest:
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
    def __init__(self, code: int, phrase: str):
        self.code = code
        self.phrase = phrase


class HttpStatus(Enum):
    OK = Status(200, 'OK')
    NOT_FOUND = Status(404, 'Not Found')
    BAD_REQUEST = Status(400, 'Bad Request')
    INTERNAL_SERVER_ERROR = Status(500, 'Internal Server Error')


class HttpResponse:
    def __init__(self, object: object.Object = None, version: str = 'HTTP/1.0'):
        self.version = version
        self.status = HttpStatus.NOT_FOUND.value
        self.object = object
        if self.object != None:
            self.status = HttpStatus.OK.value
        
    def __str__(self):
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

        response = "%s\r%s\r%s\r%s\r\r%s" % (status_line,
                                             connection,
                                             content_length_line,
                                             content_type_line,
                                             content)
        
        return response
