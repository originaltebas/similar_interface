from flask_graphql import GraphQLView
 
from app.app import app
from app.schema import schema
 
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)
 
if __name__ == '__main__':
    app.run()