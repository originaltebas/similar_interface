from graphene_sqlalchemy_filter import FilterSet
 
from app.models import MovieSerieModel
 
ALL_OPERATIONS = ['eq', 'ne', 'like', 'ilike', 'is_null', 'in', 'not_in', 'lt', 'lte', 'gt', 'gte', 'range']
 
 
class MovieSerieFilter(FilterSet):
    class Meta:
        model = MovieSerieModel
        fields = {
            'id_movie': ['eq'],
            'primaryTile': ['like','ilike'],
            'originalTitle': ['like','ilike'],
            'averageRating': ['lt', 'lte', 'gt', 'gte', 'range'],
        }