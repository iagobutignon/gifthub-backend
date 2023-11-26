from flask import Blueprint, request


profile_blueprint = Blueprint("profile", __name__)


class ProfileController():
    @profile_blueprint.put("/put_picture")
    def put_picture(self):
        data = request.get_json()

        return data, 200

    @profile_blueprint.put("/save_profile")
    def save_profile():
        data = request.get_json()

        return data, 200