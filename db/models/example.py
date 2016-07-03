from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Example(Base):
    __tablename__ = 'examples'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, id_, name):
        self.id = id_
        self.name = name

    def __repr__(self):
        return "<Example(%s, %s)>" % (self.id, self.name)
