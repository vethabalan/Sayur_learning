# compare my movie list and friend's movie list 

my_list = [ "vikram" , "ram" , "maari" , "baskaran" , "ok kanmani" ]
friend_list = [ "vikram" , "maatran", "maari" , "24" , "baskaran"]
mutual_list = [ ]
my_only_watched_movies = [ ]
friend_only_watched_movies = [ ]
for movies in range(0,len(my_list)):
    for flim in range (0,len(friend_list)):
        if((my_list[movies]) == (friend_list[flim])):
            mutual_list.append (my_list[movies])
print("same movies watched: ",mutual_list)
for movies in range(0,len(my_list)):
    for flim in range (0,len(friend_list)):
        if((my_list[movies]) != (friend_list[flim])):
            my_only_watched_movies.append(my_list[movies])
        elif( (friend_list[flim]) != (my_list[movies])):
            friend_only_watched_movies.append(friend_list[flim])
        else:
            print("no movies watched")
print("my only watched movies: ", my_only_watched_movies)
print("friend watched movies: ",friend_only_watched_movies)