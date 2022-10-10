from enum import Enum
import os
from typing import Optional


class ContentType(Enum):
    TEXT_HTML = 'text/html',
    TEXT_CSS = 'text/css',
    APPLICATION_JAVASCRIPT = 'application/javascript'


class Object:
    def __init__(self, type: ContentType, content: str):
        self.type = type
        self.content = content


class ObjectRepo:
    def __init__(self, obj_path: str = 'resources'):
        location = os.path.dirname(os.path.realpath(__file__))
        self._obj_path = os.path.join(location, obj_path)

    def find_by_name(self, obj_name: str) -> Optional[Object]:
        file_path = os.path.join(self._obj_path, obj_name)
        if not os.path.exists(file_path):
            return None

        with open(file_path) as fin:
            content = fin.read()
            extension = obj_name.split('.')[-1]
            type = None
            if extension == 'html':
                type = ContentType.TEXT_HTML
            elif extension == 'css':
                type = ContentType.TEXT_CSS
            elif extension == 'js':
                type = ContentType.APPLICATION_JAVASCRIPT

            return Object(type, content)
