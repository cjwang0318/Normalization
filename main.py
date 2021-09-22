import re
import tool_box as tb
import sqlite3

search_query = "select * FROM all_road WHERE 1 LIMIT 5"


# connect db
# con = sqlite3.connect('road.db')
# cur = con.cursor()
#
# def db_search(query):
#     for result in cur.execute(query):
#         print(result)
#     return result
#
# db_search(search_query)


def get_name(address_str, city_query):
    match = re.search(city_query, address_str)
    name = "None"
    if match:
        # print(match.group(0))
        name = match.group(0)
    return name

def dictionary_check(str, dictionary):
    result="notMatch"
    for target in dictionary:
        if target in str:
            result=target
    return result

city_query = '(\w+?[縣市])'
township_query = '(\w+?市區|\w+?鎮區|\w+?[鄉鎮市區])'
road_query = '(.+?[路街道])'

data_path = './'
address_file = 'address.txt'
dictionaryPath="location_dict/"
dictionary_list = ['city.csv', 'zone.csv', 'street.csv']
cityList=tb.read_file(data_path+dictionaryPath+dictionary_list[0], 0)
zoneList=tb.read_file(data_path+dictionaryPath+dictionary_list[1], 0)
streetList=tb.read_file(data_path+dictionaryPath+dictionary_list[2], 0)

address_str = "延平北路七段107巷36號士林區台北市"
cityName=dictionary_check(address_str, cityList)
print(cityName)

addressList=tb.read_file(data_path+address_file, 0)
print(addressList)
for add_str in addressList:
    print(add_str.strip("\n"))




# regex = re.compile(\W+?[縣市])
print(address_str)
# Get City Name
city_name = get_name(address_str, city_query)
print("City= " + city_name)
address_str = address_str.replace(city_name, "", 1)
print(address_str)
# Get Township Name
township_name = get_name(address_str, township_query)
print("Township= " + township_name)
address_str = address_str.replace(township_name, "", 1)
print(address_str)
# Get Road Name
road_name = get_name(address_str, road_query)
print("Road= " + road_name)
address_str = address_str.replace(road_name, "", 1)

print("test")