import sqlalchemy
from sqlalchemy import orm
from base.database import Base


class Pages(Base):
    __tablename__ = 'pages'

    page_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    url = sqlalchemy.Columm(sqlalchemy.String, default='')
    information = sqlalchemy.Column(sqlalchemy.JSON, default=None)


class Images(Base):
    __tablename__ = 'images'

    image_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    url = sqlalchemy.Columm(sqlalchemy.String, default='')


class Texts(Base):
    __tablename__ = 'texts'

    text_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.JSON, default=None)