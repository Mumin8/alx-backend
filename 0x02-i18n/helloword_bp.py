#!/usr/bin/env python3
"""A simple flask app
"""

from flask import Blueprint, render_template

hello_world_bp = Blueprint('helloworld', __name__, template_folder='templates')


@hello_world_bp.route('/')
def hello_world():
    """_summary_
    """
    return render_template("0-index.html")
