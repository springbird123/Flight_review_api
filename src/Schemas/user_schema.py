from main import ma
from Models.user import User
from marshmallow.validate import Length

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("password",)

    username = ma.String(required=True, validate=Length(min=1))
    email = ma.Email(required=True)
    password = ma.String(required=True, validate=Length(min=8), load_only=True) # Exclude from output
    

# Initialize the UserSchema instances
user_schema = UserSchema()
users_schema = UserSchema(many=True)