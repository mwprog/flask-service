# -*- coding: utf-8 -*-
from flask_service import create_app


if __name__ == '__main__':
    app = create_app()
    app.run()