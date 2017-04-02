import urllib2
import json
import time

url_beg  = 'http://localhost:4444/api/v3/u/'
url_end = '/blob'

infile = open('output.txt', 'r')
names = infile.read().split(',')

for i in range(len(names)):

	outfile = open('overwatch_data.json', 'a')

	print 'iteration:', i, 'of', len(names)

	segs = names[i].split('#')

	b_tag = segs[0] + '-' + segs[1]

	try:

		json_string = urllib2.urlopen(url_beg + b_tag + url_end).read()

		data = json.loads(json_string)

		if data['_request']:
			del data['_request']

		for key in data.keys():
			if data[key]:
				if data[key]['achievements']:
					del data[key]['achievements']
				if data[key]['heroes']:
					if data[key]['heroes']['playtime'] and data[key]['heroes']['playtime']['quickplay']:
						del data[key]['heroes']['playtime']['quickplay']
					if data[key]['heroes']['stats'] and data[key]['heroes']['stats']['quickplay']:
						del data[key]['heroes']['stats']['quickplay']

				if data[key]['stats'] and data[key]['stats']['quickplay']:
					del data[key]['stats']['quickplay']


		data['b_tag'] = names[i]

		outfile.write(json.dumps(data))
		outfile.write(',')
		outfile.write('\n')

		outfile.close()

	except urllib2.HTTPError as err:
		outfile.close()
		continue