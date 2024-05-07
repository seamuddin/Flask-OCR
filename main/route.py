from flask import Blueprint, jsonify,Flask, render_template
route = Blueprint('bscic_api_service', __name__)


@route.route("/", methods=["GET"])
def get_token_route():
    return render_template("form.html")

@route.route("", method=["POST"])
def uplaod_pdf()
    