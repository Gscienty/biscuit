from mongoengine import (
    Document,
    StringField,
    BooleanField,
    EmailField,
    ReferenceField
)


class User(Document):
    username = StringField(
        max_length=64,
        required=True,
        unique=True,
    )
    password = StringField(required=True)
    is_available = BooleanField(required=True)
    email = ReferenceField('UserEmail')


class UserEmail(Document):
    email = EmailField(required=True, unique=True)
    user = ReferenceField('User')
