from fuctions import add_movie, display_movies, save_movie, load_movies

movie_list = []

while True:
    print("1. Add Movies")
    print("2. Display Movies")
    print("3. Save Movies")
    print("4. Load Movies")
    print("5. Exit")

    choice = input("Select an input: ")

    if choice == "1" or choice == "Add Movie":
        movie_list = add_movie(movie_list)
        
    elif choice == "2":
     display_movies(movie_list)
    
    elif choice == "3":
       filename = input("\nProvide a filename (without extension): ")
       save_movie(movie_list, filename + ".txt")
     
    elif choice == "4":
       filename = input("\nProvide a filename (without extension): ")
       load_movies(filename + ".txt")
     
    elif choice == "5":
     print("Bye!!!!")
     break
    else:
      print("Invalide option!!")