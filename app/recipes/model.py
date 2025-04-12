import sqlalchemy
from sqlalchemy import orm
from base.database import Base


class Recipe(Base):
    __tablename__ = 'recipes'

    recipe_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name_recipe = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=False, default='')
    look = sqlalchemy.Column(sqlalchemy.JSON, default=None)

