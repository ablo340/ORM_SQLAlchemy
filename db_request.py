from database import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


"""Console request functions"""

# print all consoles
def allConsole():
    consoles = session.query(Console).all()
    for console in consoles:
        print("Id: {} - Nom: {} - Fabricant: {}".format(console.id, console.name, console.manufacturer))


# insert one console
def insertConsole(console):
    console.games = []
    session.add(console)
    session.commit()


# update one console
def updateConsole(id, name, manufacturer):
    session.query(Console).filter(Console.id == id).update(
        {"name": name, "manufacturer": manufacturer}, synchronize_session='fetch')
    session.commit()


# delete one console
def deleteConsole(console_id):
    # select the console
    query = session.query(Console).filter(Console.id == console_id)
    console = query.one()

    # delete the games associated
    for game in console.games:
        session.query(Game).filter(Game.id == game.id).delete()
        session.commit()

    # delete the console
    session.query(Console).filter(Console.id == console_id).delete()
    session.commit()


def searchConsole(name):
    query = session.query(Console).filter(Console.name == name)
    console = query.one()
    return console


def dropConsoleTable():
    Console.__table__.drop(engine)


"""Game request functions"""

# print all games
def allgames():
    games = session.query(Game).all()
    for game in games:
        print("Id: {} - Nom: {} - Description: {} - Console: {}".format(game.id, game.name,game.description,
                                                                        game.console.name))


# insert one game
def insertGame(name, description, console_id):

    # game
    game = Game(name=name, description=description)

    # game's console
    query = session.query(Console).filter(Console.id == console_id)
    console = query.one()
    console.games.append(game)

    session.add(console)
    session.commit()


# update one game
def updateGame(game_id, name, description, console_id):
    session.query(Game).filter(Game.id == game_id).update(
        {"name": name, "description": description, "console_id": console_id}, synchronize_session='fetch')
    session.commit()


# delete one game
def deleteGame(id):
    session.query(Game).filter(Game.id == id).delete()
    session.commit()


def searchGame(name):
    query = session.query(Game).filter(Game.name == name)
    game = query.one()
    return game


def dropGameTable():
    Game.__table__.drop(engine)
