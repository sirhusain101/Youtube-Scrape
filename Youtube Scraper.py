from bs4 import BeautifulSoup
from tabulate import tabulate
import requests
import json
import os
from video_ids import video_id_list     # Check video_ids.py

# Clears any text from Results.html, which was left after previous operation
open("Results.html", "w", encoding="utf-8").close()

# Adds CSS to output file for better display
with open("Results.html", "a", encoding="utf-8") as file:
    file.write("""<style>
body {
  background-color: grey;
}
table, th, td {
  padding: 10px;
  font-size: 30px;
  border: 3px solid black;
  border-collapse: collapse;
  text-align: center;
}
</style>""")

# Table header
with open("Results.html", "a", encoding="utf-8") as file:
    file.write(tabulate([["S. No.", "Thumbnail", "Date", "Title", "Description"]], tablefmt='html'))

# Main loop
for index, id in enumerate(video_id_list):
    # Clears any text from python console window.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Displays whichever video id is being being scraped
    print("(" + str(index + 1) + "/" + str(len(video_id_list)) + ") | Scraping: https://www.youtube.com/watch?v=" + id)

    # Sends request for scraping
    soup = BeautifulSoup(requests.get("https://www.youtube.com/watch?v=" + id).content, "lxml")

    # Scrapes date | https://www.youtube.com/watch?v=XVv6mJpFOb0
    date = soup.find('meta', itemprop="datePublished")['content']
    # Scrapes title
    title = soup.title.string
    # Scrapes description | https://www.youtube.com/watch?v=QNLBBGWEQ3Q | https://jsonformatter.org | https://jsonformatter.org/json-parser
    description_json = soup.find_all('script')[45].text.strip()[20:-1]
    description = json.loads(description_json)['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']['attributedDescription']['content']

    # Saves scrapped data in table format
    with open("Results.html", "a", encoding="utf-8") as file:
            file.write(tabulate([[str(index + 1), "<img src=\"thumbnails/" + id + ".jpg\" height=150 width=200>",
                                 date[:10],
                                 "<a href=\"https://www.youtube.com/watch?v=" + id + "\" target=\"_blank\">" + title + "</a>",
                                 description]], tablefmt='unsafehtml'))

# Clears any text from python console window.
os.system('cls' if os.name == 'nt' else 'clear')
# Displays a message on python console once the process is done.
print("All the videos were scraped successfully! Please check Results.html file.")
# Stop python console from closing automatically.
input("Press ENTER key to exit!")
