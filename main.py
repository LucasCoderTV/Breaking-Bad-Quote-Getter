import requests
# For the non coders out there, this goes to a page that returns (Gives you) a json file of breaking bad quotes
response = requests.get("https://api.breakingbadquotes.xyz/v1/quotes")
# It's time for the moment youve been waiting  for! "Getting It to look nice!!!"
daquote = response.json()[0]['quote']
theauthor = response.json()[0]['author']
# Prints it out
print("Quote: " +  daquote)
print("But who said it?")
print("Heres Who: " + theauthor)

