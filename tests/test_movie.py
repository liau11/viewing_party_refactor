import pytest
from viewing_party.movie import Movie

def test_create_movie_initializes_attributes():
    # Arrange/Act
    movie = Movie("Up!", "family", 5)

    # Assert
    assert movie.name == "Up!"
    assert movie.genre == "family"
    assert movie.rating == 5