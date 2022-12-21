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
for line in open('MovieSummaries/character.metadata.tsv','r') :
    s = line.split('\t') # split line on TAB character

    name, gender = s[8], s[5] # Wikipedia actor name, gender

    if gender : # if name field is not ""
        d[name].add(gender)

out = open('ScriptOutput/actor-gender.tsv','w')
for ID in d :
    print(ID, d[ID], sep = '\t', file=out)
out.close()
