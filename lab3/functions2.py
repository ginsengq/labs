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

#ex1
def score(movie):
    if movie["imdb"] > 5.5:
        return True
    return False

for movie in movies:
    print("IMDB score above 5.5: {movie['name']}, {score(movie)}")


#ex2
def score(m):
    if m["imdb"] > 5.5:
        return True
    return False

for m in movies:
    if score(m):
        print(m["name"], ", ", m["imdb"])


#ex3
cat = input()
def category(m, cat):
    if m["category"] == cat:
        return True
    return False

for m in movies:
    if category(m, cat):
        print(m["name"], ", ", m["category"], '\t')


#ex4
def average(movies):
    sum = 0
    for i in movies:
       sum += float(i["imdb"]) 
    avg = sum/len(movies)
    return avg

print(average(movies))


#ex5
cat = input() 
def category(i, cat):
    return i["category"] == cat

def average(movies):
    sum = 0
    count = 0
    for i in movies:
       if category(i, cat):
        sum += float(i["imdb"]) 
        count += 1
    if count == 0:
        return 0
    
    return sum/count

print(average(movies))
