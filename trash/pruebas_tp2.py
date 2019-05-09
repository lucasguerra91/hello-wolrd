import csv

tweets = []

with open('tweets.csv', 'r') as f:
    archivo_scv = csv.reader(f)
    print(archivo_scv)
    for tweet in archivo_scv:
        tweets.append(t)

print(tweets)
