# -*- coding: utf-8 -*-
"""
    wsgi
    ~~~~
    entrypoint wsgi script
"""

import app

application = app.create_app()
