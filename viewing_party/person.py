class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.watchlist = []
        self.watched = []

    def add_friend(self, new_friend):
        if new_friend not in self.friends:
            self.friends.append(new_friend)
    
    def add_movie(self, movie):
        if movie not in self.watchlist:
            self.watchlist.append(movie)


    def move_from_watchlist_if_watched(self, movie):
        if movie not in self.watched:
            self.watched.append(movie)
            if movie in self.watchlist:
                self.watchlist.remove(movie)