from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# Declare a Mapping
Base = declarative_base()


# Console Table
class Console(Base):
    __tablename__ = 'console'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=True)
    games = relationship("Game", back_populates="console")

    def __repr__(self):
        return "name = '%s'; manufacturer = '%s'" % (
            self.name, self.manufacturer)


# Game Table
class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(550), nullable=True)
    console_id = Column(Integer, ForeignKey('console.id'))
    console = relationship("Console", back_populates="games")

    def __repr__(self):
        return "name = '%s'; description = '%s'; console = '%s'" % (
            self.name, self.description, self.console)


# connecting
engine = create_engine('sqlite:///videogames_db')

# persisting our table
Base.metadata.create_all(engine)


