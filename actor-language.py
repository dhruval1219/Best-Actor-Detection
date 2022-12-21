import sys
from collections import defaultdict, Counter

# test a dictionary
def test_dict(d) :

    for key in d :
        print(key, d[key], sep = '\t')
        
# build mapping from actor -> movies
def actor_movies() :

    d = defaultdict(set) # keep a set of (unique) movie
    for line in open('MovieSummaries/character.metadata.tsv','r') :
        s = line.split('\t') # split line on TAB character

        ID, name = s[0], s[8] # Wikipedia movie ID, actor name

        if name : # if name field is not ""
            d[name].add(ID) # add to set of movie IDs for name

    return d

# build mapping from movie -> language
def movie_language() :

    d = {}
    for line in open('MovieSummaries/movie.metadata.tsv','r') :
        s = line.split('\t') # split on TAB
        ID, language = s[0], s[6] # movie ID, language

        if language and language != '{}' :
            language = language.split(':')[-1].rstrip('}')
            language = language.replace('"','')
            language = language.replace('Language','')
            language = language.strip()
            
            d[ID] = language

    return d

# Main

movies = actor_movies()
language = movie_language()

out = open('ScriptOutput/actor-language.tsv', 'w')
for actor in movies :
    languages = []

    for movie in movies[actor] :

        if movie in language :
            languages.append(language[movie])
    
    if languages :
        lang, _ = Counter(languages).most_common()[0]
        print(actor, lang, sep = '\t', file=out)
out.close()