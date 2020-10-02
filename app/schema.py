import graphene
from graphene import relay, Schema, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene_sqlalchemy_filter import FilterableConnectionField

from app.models import MovieSerieModel
from app.filter import MovieSerieFilter


class MovieSerie(SQLAlchemyObjectType):
    class Meta:
        model = MovieSerieModel
        interfaces = (graphene.relay.Node,)
 
class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    # MovieSerie = SQLAlchemyConnectionField(MovieSerie, name=graphene.String())
    MovieSerie = FilterableConnectionField(connection=MovieSerie, filters=MovieSerieFilter(), sort=MovieSerie.sort_argument()) 

schema = graphene.Schema(query=Query, types=[MovieSerie])