#This file is part of Tryton. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from flask.globals import (_request_ctx_stack, current_app,
    request, _lookup_object, session, g, LocalProxy)


def _find_cache():
    """The application context will be automatically handled by
    _find_app method in flask
    """
    try:
        from flask.globals import _find_app
        app = _find_app()
    except ImportError:
        # Flask < 0.9
        app = _lookup_object('app')
    return app.cache

cache = LocalProxy(_find_cache)
