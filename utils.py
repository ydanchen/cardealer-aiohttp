import json

from aiohttp import web


def json_response(data, status=200) -> web.Response:
    return web.Response(
        body=json.dumps(data, default=lambda x: x.__dict__, indent=2, sort_keys=True),
        status=status,
        content_type='application/json')
