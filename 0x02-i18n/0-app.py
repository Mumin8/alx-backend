#!/usr/bin/env python3
"""A simple flask app
"""


from flask import Flask
from helloword_bp import hello_world_bp

app = Flask(__name__)
app.register_blueprint(hello_world_bp)


if __name__ == '__main__':
    app.run(debug=True)
