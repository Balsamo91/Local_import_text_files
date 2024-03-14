def add_movie(movie_list):
  movie_name = input("Type your movie")
  movie_list.append(movie_name)
  print(f"Movie '{movie_name}' added!")
  return movie_list


def display_movies(movies_list):
  if not movies_list:
    print("The movie list is empty")

  else:
    print("Fav movies:")
    for movie in movies_list:
      print(f"- {movie}")

def save_movie(movie_list, filename):
    try:
        with open(filename, 'w') as file:
            for movie in movie_list:
                file.write(movie + '\n')
                print("Movies saved successfully!")

    except Exception as e:
      print(f"Error saving movie: {e}")

def load_movies(filename):
    try:
        with open(filename, "r") as file:
            """
            movie_list = []
            For line in file.readlines():
                movie_list.append(line.strip())
            """

            movie_list = [line.strip() for line in file.readlines()]
            print("Movies Loaded successfully")
            return movie_list
    except Exception as e:
      print(f"Error loading movie: {e}")
      return []
