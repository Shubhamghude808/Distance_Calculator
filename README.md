This program calculates the distance between two locations entered by the user. It uses the Haversine formula to calculate the aerial distance between the two locations based on their latitude and longitude. The script also calculates the road distance, which is assumed to be 30% more than the aerial distance.

The script then asks the user to select a mode of transport (Walk, Motorcycle, Car, Train, Aeroplane) and calculates the estimated time of arrival (ETA) based on the average speed of the selected mode of transport.

Please note that this script uses the MapQuest API to get the latitude and longitude of the locations, and you would need a valid API key from MapQuest to run this script. Also, this script doesn’t handle exceptions, so it might break if the user enters invalid input or if the API request fails.
