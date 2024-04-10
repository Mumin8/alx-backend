from flask import Blueprint, render_template

hello_world_bp = Blueprint('helloworld', __name__, template_folder='templates')

@hello_world_bp.route('/')
def hello_world():
    """_summary_
    """
    return render_template("index.html")
