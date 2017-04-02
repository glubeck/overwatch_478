import json

def to_file(file, data, key, comma=True):
	if key in data:
		file.write(str(data[key]))
	else:
		file.write('?')

	if comma:
		file.write(',')

def is_valid(data):
	valid = True
	valid = valid and 'us' in data
	valid = valid and data['us'] is not None
	valid = valid and 'stats' in data['us']
	valid = valid and data['us']['stats'] is not None
	valid = valid and 'competitive' in data['us']['stats']
	valid = valid and data['us']['stats']['competitive'] is not None
	valid = valid and 'overall_stats' in data['us']['stats']['competitive']
	valid = valid and data['us']['stats']['competitive']['overall_stats'] is not None
	valid = valid and 'tier' in data['us']['stats']['competitive']['overall_stats']
	valid = valid and data['us']['stats']['competitive']['overall_stats']['tier'] is not None
	return valid


output = open('overwatch_stats.arff', 'a')

with open('overwatch_data.json', 'r') as f:
	iteration = 1
	for line in f:
	    print 'iteration:', iteration
	    data = json.loads(line[:-2])
	    # print json.dumps(data)
	    if is_valid(data):
	        output.write('\n')
	        comp_data = data['us']['stats']['competitive']['average_stats']
	        to_file(output, comp_data, 'final_blows_avg')
	        to_file(output, comp_data, 'objective_time_avg')
	        to_file(output, comp_data, 'objective_kills_avg')
	        to_file(output, comp_data, 'eliminations_avg')
	        to_file(output, comp_data, 'time_spent_on_fire_avg')
	        to_file(output, comp_data, 'melee_final_blows_avg')
	        to_file(output, comp_data, 'healing_done_avg')
	        to_file(output, comp_data, 'damage_done_avg')
	        to_file(output, comp_data, 'deaths_avg')
	        to_file(output, comp_data, 'solo_kills_avg')
	        output.write(data['us']['stats']['competitive']['overall_stats']['tier'])
	    iteration+=1

output.close()
        
    