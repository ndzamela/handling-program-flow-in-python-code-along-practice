# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

#print(data) 
 
# Code starts here

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
first_innings_deliveries = data['innings'][0]['1st innings']['deliveries']

count_deliveries = 0
for faced in first_innings_deliveries:
    for delivery_number, delivery_info in faced.items():
        if delivery_info['batsman'] == 'SC Ganguly':
            count_deliveries += 1
print("The deliveries faced by SC Ganguly were : ", count_deliveries)
#  Who was man of the match and how many runs did he scored ?
man_of_the_match = data['info']['player_of_match']
print("Player of the match is: ", man_of_the_match[0])

runs_scored = 0
for runs in first_innings_deliveries:
    for delivery_number, delivery_info in runs.items():
        if delivery_info['batsman'] == 'BB McCullum':
            runs_scored += delivery_info['runs']['batsman']

print("Total runs scored by " + man_of_the_match[0] + " is : " , runs_scored)

#  Which batsman played in the first inning?
batsman = []
for all_batsman in first_innings_deliveries:
    for delivery_number, delivery_info in all_batsman.items():
        batsman.append(delivery_info['batsman'])
print("All the batsman who played in first inning are: ", set(batsman))

# Which batsman had the most no. of sixes in first inning ?
most_sixes = []
for sixes in first_innings_deliveries:
    for delivery_number, delivery_info in sixes.items():
        if delivery_info['runs']['batsman'] == 6:
            most_sixes.append(delivery_info['batsman'])
most_sixes_list = list(set((most_sixes)))
print("Batsman that had most no of sixes in the first inning: ", most_sixes_list)

from collections import Counter

def get_batsman_who_had_most_sixes(sixes):
    
    try:
        cnt = Counter(sixes)
    except:
        return "there was no sixes"
    return cnt
print("Batsman that had the most sixes : ", get_batsman_who_had_most_sixes(most_sixes))

print("Player with most sixes:" , get_batsman_who_had_most_sixes(most_sixes).most_common(1)[0][0])

# Find the names of all players that got bowled out in the second innings.
second_innins_deliveries = data['innings'][1]['2nd innings']['deliveries']

bowled_players = []
for bowled_out in second_innins_deliveries:
    for delivery_number, delivery_info in bowled_out.items():
        try:
            if delivery_info['wicket']['kind'] == 'bowled':
                bowled_players.append(delivery_info['wicket']['player_out'])
        except:
            pass
            
bowled_players


# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
extras_1st_innings = []
for delivery_1st in first_innings_deliveries:
    for delivery_number, delivery_info in delivery_1st.items():
        if 'extras' in delivery_info:
            extras_1st_innings.append(delivery_1st)
extras_2nd_innings = []
for delivery_2st in second_innins_deliveries:
    for delivery_number, delivery_info in delivery_2st.items():
        if 'extras' in delivery_info:
            extras_2nd_innings.append(delivery_2st)


def get_extras(innings_deliveries):
    extras_innings = []
    for delivery in innings_deliveries:
        for delivery_number, delivery_info in delivery.items():
            if 'extras' in delivery_info:
                extras_innings.append(delivery)

    return extras_innings


extras_1st_innings = get_extras(first_innings_deliveries)
extras_2nd_innings = get_extras(second_innins_deliveries)


difference = len(extras_1st_innings) - len(extras_2nd_innings)
print("2nd innings had ", abs(difference), " more extras than 1st innings")

#Code ends here


