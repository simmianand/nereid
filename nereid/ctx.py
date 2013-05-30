#This file is part of Tryton. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from flask.ctx import _RequestGlobals, RequestContext as RequestContextBase
from flask.ctx import has_request_context



class RequestContext(RequestContextBase):
    """The request context contains all request relevant information.  It is
    created at the beginning of the request and pushed to the
    `_request_ctx_stack` and removed at the end of it.  It will create the
    URL adapter and request object for the WSGI environment provided.
    """

    def __init__(self, app, environ):
        super(RequestContext, self).__init__(app, environ)
        self.transaction = None
        self.cache = app.cache
