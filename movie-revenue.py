'''

Metadata for 450,669 characters aligned to the movies above, extracted
from the Noverber 4, 2012 dump of Freebase.  Tab-separated; columns:

1. Wikipedia movie ID
2. Freebase movie ID
3. Movie release date
4. Character name
5. Actor date of birth
6. Actor gender
7. Actor height (in meters)
8. Actor ethnicity (Freebase ID)
9. Actor name
10. Actor age at movie release
11. Freebase character/actor map ID
12. Freebase character ID
13. Freebase actor ID

'''

import sys
from collections import defaultdict

d = defaultdict(set) # keep a set of (unique) actors
for line in open('MovieSummaries/movie.metadata.tsv','r') :
    s = line.split('\t') # split line on TAB character

    movie, revenue = s[0], s[4] # Wikipedia movie ID, revenue

    if revenue : # if name field is not ""
        d[movie].add(revenue)

out = open('ScriptOutput/movie-revenue.tsv','w')
for ID in d :
    print(ID, d[ID], sep = '\t', file=out)
out.close()
