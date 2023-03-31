from viewing_party.person import Person
from viewing_party.movie import Movie

import pytest

def test_creating_person_initializes_instance_variables():
    # Arrange / Act
    kendall = Person("Kendall")

    # Assert
    assert kendall.name == "Kendall"
    assert kendall.friends == []
    assert kendall.watchlist == []
    assert kendall.watched == []

def test_adding_friend_multiple_times_does_not_create_duplicate():
    # Arrange
    kendall = Person("Kendall")
    simon = Person("Simon")

    # Act
    kendall.add_friend(simon)
    kendall.add_friend(simon)

    # Assert
    assert kendall.friends == [simon]
    
def test_watchlist_new_movie():
    # Arrange 
    kendall = Person("Kendall")
    movie = Movie("Up!", "family", 5)

    # Act
    kendall.add_movie(movie)

    # Assert 
    assert kendall.watchlist == [movie]

def test_watchlist_new_movie_duplicates():
    # Arrange 
    kendall = Person("Kendall")
    movie = Movie("Up!", "family", 5)

    # Act
    kendall.add_movie(movie)
    kendall.add_movie(movie)

    # Assert 
    assert kendall.watchlist == [movie]

def test_move_from_watchlist_if_watched():
    # Arrange
    kendall = Person("Kendall")
    movie = Movie("Up!", "family", 5)

    # Act
    kendall.add_movie(movie)
    kendall.move_from_watchlist_if_watched(movie)

    # Assert
    assert kendall.watchlist == []
    assert kendall.watched == [movie]

def test_did_not_modify_watchlist():
    # Arrange 
    kendall = Person("Kendall")
    movie1 = Movie("Up!", "family", 5)
    movie2 = Movie("Lion King", "family", 5)

    # Act
    kendall.add_movie(movie1)
    kendall.move_from_watchlist_if_watched(movie2)

    # Assert
    assert kendall.watchlist == [movie1]
    assert kendall.watched == [movie2]