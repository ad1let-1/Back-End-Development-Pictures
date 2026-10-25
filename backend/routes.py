from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
with open(json_url, encoding="utf-8") as source:
    data: list = json.load(source)

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    return jsonify(data), 200

######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    picture = next((item for item in data if item["id"] == id), None)
    if picture is None:
        return jsonify(message=f"picture with id {id} not found"), 404
    return jsonify(picture), 200


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    picture = request.get_json(silent=True)
    if not isinstance(picture, dict) or not isinstance(picture.get("id"), int):
        return jsonify(message="A JSON picture with an integer id is required"), 400
    if any(item["id"] == picture["id"] for item in data):
        return jsonify(Message=f"picture with id {picture['id']} already present"), 302
    data.append(picture)
    return jsonify(picture), 201

######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    picture = request.get_json(silent=True)
    if not isinstance(picture, dict):
        return jsonify(message="A JSON picture is required"), 400
    for index, item in enumerate(data):
        if item["id"] == id:
            updated = {**item, **picture, "id": id}
            data[index] = updated
            return jsonify(updated), 200
    return jsonify(message=f"picture with id {id} not found"), 404

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    for index, item in enumerate(data):
        if item["id"] == id:
            data.pop(index)
            return "", 204
    return jsonify(message=f"picture with id {id} not found"), 404
