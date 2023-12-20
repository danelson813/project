from utils.util import get_soup, send_to_sqlite3, read_the_sqlite3
from utils.logging_module.utils.log_module import logger
import pandas as pd


url = "https://www.nfl.com/stats/player-stats/category/passing/2023/reg/all/passingyards/desc"

soup = get_soup(url)

players = soup.select_one("tbody").select('tr')
logger.info(f"There are {len(players)} players")

results = []
for player in players:
    name = player.select_one('a.d3-o-player-fullname').text.strip()
    # logger.info(name)
    player_info = [td.text.split() for td in player.find_all('td')[1:]]
    result = {
        'Name': name,
        'Pass Yrds': player_info[0][0],
        'Yds/Att': player_info[1][0],
        'Att': player_info[2][0],
        'Cmp': player_info[3][0],
        'Cmp%': player_info[4][0],
        'TD': player_info[5][0],
        'INT': player_info[6][0],
        'Rating': player_info[7][0],
        '1st': player_info[8][0],
        '1st%': player_info[9][0],
        '20+': player_info[10][0],
        '40+': player_info[11][0],
        'Lng': player_info[12][0],
        'Sck': player_info[13][0],
        'SckY': player_info[14][0],
    }
    results.append(result)

df = pd.DataFrame(results)

df['Pass Yrds'] = df['Pass Yrds'].astype(int)
df['Yds/Att'] = df['Yds/Att'].astype(float)
df['Att'] = df['Att'].astype(int)
df['Cmp'] = df['Cmp'].astype(float)
df['Cmp%'] = df['Cmp%'].astype(float)
df['TD'] = df['TD'].astype(int)
df['INT'] = df['INT'].astype(int)
df['Rating'] = df['Rating'].astype(float)
df['1st'] = df['1st'].astype(int)
df['1st%'] = df['1st%'].astype(float)
df['20+'] = df['20+'].astype(int)
df['40+'] = df['40+'].astype(int)
df['Lng'] = df['Lng'].astype(int)
df['Sck'] = df['Sck'].astype(int)
df['SckY'] = df['SckY'].astype(int)

df.to_csv('data/rusults.csv', index=False)
logger.info("The dataframe has been saved as a 'csv file'")
send_to_sqlite3(df)
result = read_the_sqlite3('data/football.db')
print(result.info())
logger.info("program is done")
