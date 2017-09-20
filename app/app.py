# -*- coding: utf-8 -*-

from bottle import route, run, default_app

@route("/")
def hello():
    return "Hello world!"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
else:
    application = default_app()

