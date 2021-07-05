from bs4 import  BeautifulSoup
import requests
import time

if __name__ == '__main__':
    while True:
        url = 'https://www.bundesliga.com/en/bundesliga/table'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'lxml')
        team_name_cells = soup.find_all('td', class_='team')
        with open('data.txt', 'a', encoding='utf8') as file:
            for team_name_cell in team_name_cells:
                file.write(team_name_cell.find('span', class_='d-lg-inline').text)
                file.write('\n')
            file.write('\n')
        time.sleep(60)