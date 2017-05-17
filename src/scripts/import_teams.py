from bs4 import BeautifulSoup
import requests

teams_and_leagues_resource = 'https://www.easports.com/fifa/news/2016/fifa-17-leagues-and-teams'
r = requests.get(teams_and_leagues_resource)
soup = BeautifulSoup(r.text, 'html.parser')

def get_all_leagues():
    return soup.find('div', class_="eas-b2")


if __name__ == '__main__':
    leagues = get_all_leagues()
    for team in leagues.find_all_next("p"):
        blockquote_parent = team.find_parent("blockquote")
        if blockquote_parent is not None:
            #print(blockquote_parent.previous_sibling)
            print(team.get_text())
