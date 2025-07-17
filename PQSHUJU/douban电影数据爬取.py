import requests
from bs4 import BeautifulSoup
import csv

url = "https://movie.douban.com/top250?start={}&filter="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

movies = []
for i in range(0, 250, 25):
    response = requests.get(url.format(i), headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        movie_items = soup.find_all('div', class_='item')
        
        for item in movie_items:
            title = item.find('span', class_='title').text
            rating = item.find('span', class_='rating_num').text
            link = item.find('a')['href']
            movies.append([title, rating, link])
    else:
        print(f"Failed to retrieve page {i // 25 + 1}") 

# Save to CSV
with open('douban_top250_movies.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Rating', 'Link'])
    writer.writerows(movies)

print("Data scraping completed. Saved to douban_top250_movies.csv")
# This script scrapes the top 250 movies from Douban and saves the data to a CSV file.
