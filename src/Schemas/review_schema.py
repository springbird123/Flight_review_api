from main import ma
from Models.review import Review
from marshmallow.validate import Range

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True

    rating = ma.Integer(required=True, validate=Range(min=1, max=10))

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)