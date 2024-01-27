import requests
from math import radians, cos, sin, asin, sqrt

'''Signature of location finders'''


def firstloc():
    key = ''  #Enter your MapQuestAPI Key
    url = 'http://www.mapquestapi.com/geocoding/v1/address?key='
    loc = input('Enter your first location :')
    main_url = url + key + '&location=' + loc
    print(main_url)

    r = requests.get(main_url)
    data = r.json()['results'][0]
    location = data['locations'][0]
    # print(location)

    city = location['adminArea5']  # key
    state = location['adminArea3']
    country = location['adminArea1']
    zipcode = location['geocodeQualityCode']
    lat = location['latLng']['lat']
    lon = location['latLng']['lng']

    print('Location :', loc)
    print('City :', city)
    print('State :', state)
    print('Country :', country)
    # print('Postal Code :',zipcode)
    print('Latitude :', lat)
    print('Longitude :', lon)
    print('\n\n')
    return lat, lon, loc


def secondloc():
    key = ''  #Enter your MapQuestAPI Key
    url = 'http://www.mapquestapi.com/geocoding/v1/address?key='
    loc = input('Enter your second location :')
    main_url = url + key + '&location=' + loc
    # print(main_url)

    r = requests.get(main_url)
    data = r.json()['results'][0]
    location = data['locations'][0]
    # print(location)

    city = location['adminArea5']
    state = location['adminArea3']
    country = location['adminArea1']
    zipcode = location['geocodeQualityCode']
    lat = location['latLng']['lat']
    lon = location['latLng']['lng']

    print('Location :', loc)
    print('City :', city)
    print('State :', state)
    print('Country :', country)
    # print('Postal Code :',zipcode)
    print('Latitude :', lat)
    print('Longitude :', lon)
    print('\n\n')
    return lat, lon, loc


def distance(lat1, lat2, lon1, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return c * r


def time(time):
    # time = float(input("Input time in seconds: "))
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    print("ETA=d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


'''main'''
print("==================-------------------=====================")
print("==================DISTANCE CALCULATOR=====================")
print("==================-------------------=====================\n\n")
lat1, lon1, loc1 = firstloc()
lat2, lon2, loc2 = secondloc()
print("Aerial Distance:", distance(lat1, lat2, lon1, lon2), "K.M")
road_d = distance(lat1, lat2, lon1, lon2)
road = road_d + road_d * 0.3
print("Road Distance:", road, "K.M\n")

print("Select Your mode of Transport\n")
print("1. Walk \n2.Motorcycle\n3.Car\n4.Train\n5.Aeroplane")
n = int(input("Enter Your Choice:"))
if n == 1:
    T = road / 9
    T = T * 3600
    time(T)

elif (n == 2):
    T = road / 60
    T = T * 3600
    time(T)

elif (n == 3):
    T = road / 80
    T = T * 3600
    time(T)

elif (n == 4):
    T = road / 110
    T = T * 3600
    time(T)

elif (n == 5):
    T = road_d / 700  # road_d = areial
    T = T * 3600
    time(T)

else:
    print("Enter a correct Choice--")
