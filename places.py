import pandas as pd
from googlemaps import Client, places

client = Client(key='AIzaSyAIBuIyasYc7wVw9FmcNyP7e3PABRPrwvQ')


# returns names of state parks in california?
def get_names(url):
    table = pd.read_html(url)[0]
    names = table['Park Name'].values
    return [n for n in names]


def place_details(query):
    res = places.places(client, query=query, location='43.980196, -120.852188')['results']
    try:
        return {
            'name': res[0]['name'],
            'rating': res[0]['rating'],
            'num_reviews': res[0]['user_ratings_total'],
            'formatted_address': res[0]['formatted_address'],
            'location': res[0]['geometry']['location'],
        }
    except (IndexError, KeyError, ValueError):
        print('No results found for: ', query)
        return


output = []
parks = get_names('https://en.wikipedia.org/wiki/List_of_Oregon_state_parks')
for p in parks:
    details = place_details(p)
    if details:
        print(details)
        output.append(details)

output = sorted(output, key=lambda o: o['rating'])

for o in output:
    if o['rating'] >= 4.8 and o['num_reviews'] > 30:
        print(o)
