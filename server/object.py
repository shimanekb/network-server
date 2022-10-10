from enum import Enum


class ContentType(Enum):
    TEXT_HTML = 'text/html',
    TEXT_CSS = 'text/css',
    APPLICATION_JAVASCRIPT = 'application/javascript'


class Object:
    def __init__(self, type: ContentType, content: str):
        self.type = type
        self.content = content
