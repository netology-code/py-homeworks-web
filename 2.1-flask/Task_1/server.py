import json
from hashlib import md5

from flask import Flask, jsonify, request
from flask.views import MethodView
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from models import Session, User
from schema import CreateUser, UpdateUser

app = Flask("app")


class HttpError(Exception):
    def __init__(self, status_code: int, message: dict | str | list):
        self.status_code = status_code
        self.message = message


def validate(json_data, schema):
    try:
        model = schema(**json_data)
        return model.dict(exclude_none=True)
    except ValidationError as err:
        error_message = json.loads(err.json())
        raise HttpError(400, error_message)


@app.errorhandler(HttpError)
def error_handler(er: HttpError):
    http_response = jsonify({"status": "error", "message": er.message})
    http_response.status_code = er.status_code
    return http_response


SALT = "jvhiuehvreyuvgresvjreviruy87vs8vosevpvsrp9"


def hash_password(password: str):
    password = f"{SALT}{password}"
    password = password.encode()
    password = md5(password).hexdigest()
    return password


def get_user(user_id: int, session: Session):
    user = session.get(User, user_id)
    if user is None:
        raise HttpError(404, "user not found")
    return user


class UsersView(MethodView):
    def get(self, users_id):
        with Session() as session:
            user = get_user(users_id, session)
            return jsonify({"id": user.id, "name": user.name})

    def post(self):
        json_data = validate(request.json, CreateUser)
        json_data["password"] = hash_password(json_data["password"])
        with Session() as session:
            new_user = User(**json_data)
            session.add(new_user)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(408, "user already exists")
            return jsonify({"id": new_user.id})

    def delete(self, user_id):
        with Session() as session:
            user = get_user(user_id, session)
            session.delete(user)
            session.commit()
            return jsonify({"status": "deleted"})

    def patch(self, user_id):
        json_data = validate(request.json, UpdateUser)
        if "password" in json_data:
            json_data["password"] = hash_password(json_data["password"])
        with Session() as session:
            user = get_user(user_id, session)
            for key, value in json_data.items():
                setattr(user, key, value)
            session.add(user)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(408, "user already exists")
            return jsonify({"status": "success"})


user_view = UsersView.as_view("users")

app.add_url_rule("/users/", view_func=user_view, methods=["POST"])
app.add_url_rule(
    "/users/<int:user_id>", view_func=user_view, methods=["GET", "PATCH", "DELETE"]
)

if __name__ == "__main__":
    app.run()