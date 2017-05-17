from bs4 import BeautifulSoup
import requests
import mlab

teams_and_leagues_resource = 'https://www.easports.com/fifa/news/2016/fifa-17-leagues-and-teams'
r = requests.get(teams_and_leagues_resource)
soup = BeautifulSoup(r.text, 'html.parser')
db = mlab.connect()

def get_all_leagues():
    return soup.find('div', class_="eas-b2")


if __name__ == '__main__':
    leagues = get_all_leagues()
    for team in leagues.find_all_next("p"):
        blockquote_parent = team.find_parent("blockquote")
        if blockquote_parent is not None:
            #print(blockquote_parent.previous_sibling)
            result = db.teams.insert_one(
                {
                    "name" : team.get_text()
                }
            )
            print(result.inserted_id)
