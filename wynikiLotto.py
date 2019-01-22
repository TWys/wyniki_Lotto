import requests
import bs4

link_lotto = 'https://www.lotto.pl/lotto/wyniki-i-wygrane/ostatnie-wyniki'
link_EJ = 'https://www.lotto.pl/eurojackpot/wyniki-i-wygrane'

# Pobranie strony z wynikami Lotto
html = requests.get(link_lotto)
soup = bs4.BeautifulSoup(html.text, 'html.parser')
table = soup.find('table', class_='ostatnie-wyniki-table')
row = table.find_all('tr', class_='wynik')
data_lotto = row[0].find_all('td')[2].get_text()

# Pobranie wyników Lotto
lotto = [int(w.get_text()) for w in row[0].find('div', class_='sortrosnaco').find_all('span')]

# Pobranie wyników Lotto Plus
lotto_plus = [int(w.get_text()) for w in row[1].find('div', class_='sortrosnaco').find_all('span')]

# Pobranie strony z wynikami Eurojackpot
html = requests.get(link_EJ)
soup = bs4.BeautifulSoup(html.text, 'html.parser')
table = soup.find('table', class_='ostatnie-wyniki-table')
row = table.find('tr', class_='wynik')
data_EJ = row.find_all('td')[1].get_text()
eurojackpot = [w.get_text() for w in row.find('div', class_='sortrosnaco').find_all('span')]

# Wypisanie wyników
print('Ostatnie wyniki losowań:\n')
print('Lotto z dnia {}: \t\t\t{}'.format(data_lotto, ', '.join(map(str, lotto))))
print('Lotto Plus z dnia {}: \t{}'.format(data_lotto, ', '.join(map(str, lotto_plus))))
print('Eurojackpot z dnia {}: \t{} + {}'.format(data_EJ, ', '.join(map(str, eurojackpot[0:5])),
                                                ', '.join(map(str, eurojackpot[6:8]))))
