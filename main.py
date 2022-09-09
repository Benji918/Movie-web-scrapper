from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.imdb.com/chart/top'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.select('td.titleColumn')
year = [year.text.strip('()') for year in soup.select('td.titleColumn span')]
title = [title.getText() for title in soup.select('td.titleColumn a')]
ratings = [rating.getText() for rating in soup.find_all(name='strong')]
poster_image = [poster.get('src') for poster in soup.select('td.posterColumn img')]

# Create emtpy list to house the dictionary data
list_data = []

# Loop through the movies to add each list item to the dictionary
for index in range(len(movies)):
    data = {
        'title': title[index],
        'year': year[index],
        'rating': ratings[index],
        'poster-link': poster_image[index]

    }
    list_data.append(data)
# Then create a csv file to insert the given data!
field_names = ['title', 'year', "rating", "poster-link"]
with open('Top 250 movies.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    for movie in list_data:
        writer.writerow(movie)
    print('Successful')
