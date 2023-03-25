from main import ma
from Models.user import User

# UserSchema class inherits from ma.SQLAlchemyAutoSchema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User  # Specify the User model for the schema
        load_instance = True
        exclude = ("password",)  # Exclude the password field from the schema

# Initialize the UserSchema instances
user_schema = UserSchema()
users_schema = UserSchema(many=True)