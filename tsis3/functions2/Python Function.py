def above_55(m):   #1
    if m["imdb"] > 5.5:
        return True
    else:
        return False

def sublist_above_55(movies):    #2
    return [movie for movie in movies if above_55(movie)]

def movies_cat(movies, cat):    #3
    return[movie for movie in movies if movie["category"] == cat]

def average_IMDB_score(movies):     #4
    qwe = sum(movie["imdb"] for movie in movies)
    avg = qwe/(len(movies))
    return avg

def category_average(movies, category):
    movie_category = movies_cat(movies, category)
    avg = average_IMDB_score(movie_category)
    return avg



movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
movies_above_55 = sublist_above_55(movies)
Romance_movies = movies_cat(movies, "Romance")
avg_score_movies = average_IMDB_score(movies)
avg_Romance_movies = category_average(movies, "Romance")

print(movies_above_55)
print(Romance_movies)
print(avg_score_movies)
print(avg_Romance_movies)
