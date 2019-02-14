from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_request import Console, Game

# connecting
engine = create_engine('sqlite:///videogames_db', echo=True)


# session
Session = sessionmaker(bind=engine)
session = Session()

"""Insert Section"""


# inserting some Games in database
fifa_19 = Game(name='FIFA 19', description='Jeu du moment')
pes_19 = Game(name='PES 19', description='Concurrent de FIFA')
mario_kart = Game(name='Mario kart', description='Jeu familial')

# inserting some Consoles in database
ps4 = Console(name='Ps4', manufacturer='Sony')
ps4.games = [fifa_19]
session.add(ps4)


xbox_one = Console(name='Xbox One', manufacturer='Windows')
xbox_one.games = [pes_19]
session.add(xbox_one)


wii = Console(name='Wii', manufacturer='Sony')
wii.games = [mario_kart]
session.add(wii)
session.commit()
