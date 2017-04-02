from bs4 import BeautifulSoup
import requests
url = 'https://overwatchtracker.com/leaderboards/pc/global/CompetitiveRank?page='
end_url = '&mode=1'

target = open('battle_tags.txt', 'w')

for i in xrange(960):
	print 'iteration:', i
	r = requests.get(url + str(i) + end_url)
	data = r.text
	soup = BeautifulSoup(data)



	for link in soup.find_all('a'):

		if '#' in str(link.contents) and 'i class' not in str(link.contents):
			try:
				target.write(str(link.contents[0]))
				target.write(',')
				print str(link.contents[0])
			except:
				continue

target.close()


#skill rating distributions:
# 0 - 1500: Bronze 1111
# 1500 - 2000: Silver 1111
# 2000 - 2500: Gold 1111
# 2500 - 3000: Plat 1111
# 3000 - 3500: Diamond 1111
# 3500 - 4000: Master 1111
# 4000 - 5000: Grandmaster 11