from mongoengine import (
    Document,
    StringField,
    BooleanField
)


class User(Document):
    username = StringField(
        max_length=64,
        required=True,
        unique=True,
    )
    password = StringField(required=True)
    is_available = BooleanField(required=True)
