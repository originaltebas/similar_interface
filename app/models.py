from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import DECIMAL

from app.app import app
 
db = SQLAlchemy(app)

class MovieSerieModel(db.Model):
    __tablename__ = 'tb_movies_series'
    __table_args__ = {'extend_existing': True}
 
    id_movie = db.Column(db.Integer, primary_key=True)
    tconst = db.Column(db.String(10))
    titleType = db.Column(db.String(12))
    primaryTitle = db.Column(db.String(300))
    originalTitle = db.Column(db.String(300))
    isAdult = db.Column(db.Integer)
    startYear = db.Column(db.String(4))
    endYear = db.Column(db.String(4))
    runtimeMinutes = db.Column(db.String(5))    
    genres = db.Column(db.String(50))    
    averageRating = db.Column(DECIMAL(3,1))    
    numVotes = db.Column(db.Integer)
    nombres_actores = db.Column(db.String(300))  
    nombres_directores = db.Column(db.String(200))  
    review = db.Column(db.String(25000))
    plot = db.Column(db.String(2500))
    keywords = db.Column(db.String(300))

    def __repr__(self):
        return '<Movie/Serie {} {} {}>'.format(self.originalTitle,self.genre,self.averageRating)