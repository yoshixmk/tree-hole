from scholarly import scholarly

search_query = scholarly.search_author('Steven A Cholewiak')
# search_query = scholarly.search_keyword('Haptics')
author = scholarly.fill(next(search_query))
# scholarly.pprint(next(search_query))
print(author)

# Print the titles of the author's publications
print([pub['bib']['title'] for pub in author['publications']])

# Take a closer look at the first publication
pub = scholarly.fill(author['publications'][0])
print(pub)

# Which papers cited that publication?
print([citation['bib']['title'] for citation in scholarly.citedby(pub)])
