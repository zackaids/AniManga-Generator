import requests

query = '''
query ($genre: String) {
  Page(page: 1, perPage: 10) {
    media(genre: $genre, type: ANIME) {
      id
      title {
        romaji
        english
      }
      description
      genres
      averageScore
    }
  }
}
'''

url = 'https://graphql.anilist.co'

def fetch_anime_data(genre):
    response = requests.post(url, json={'query': query, 'variables': {'genre': genre}})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed to run by returning code of {response.status_code}. {query}")
