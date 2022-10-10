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
