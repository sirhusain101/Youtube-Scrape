from bs4 import BeautifulSoup
from tabulate import tabulate
import requests
import re
import os
from video_ids import video_id_date_dict



# Clears any text from Results.html, which was left after previous operation
open("Results.html", "w", encoding="utf-8").close()

# Table header
with open("Results.html", "a", encoding="utf-8") as file:
    file.write(tabulate([["S. No.", "Thumbnail", "Date", "Title", "Description"]], tablefmt='html'))

for id, date in video_id_date_dict.items():
    # Clears any text from python console window.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Displays whichever video id is being being scraped
    print("(" + str(list(video_id_date_dict).index(id) + 1) + "/" + str(len(video_id_date_dict)) + ") | Scraping: https://www.youtube.com/watch?v=" + id)

    # Sends request for scraping
    soup = BeautifulSoup(requests.get("https://www.youtube.com/watch?v=" + id).content, "html.parser")

    # Scrapes title with regex
    title_pattern = re.compile('(?<=title><meta name="title" content=").*(?="><meta name="description" content=)')
    title = title_pattern.findall(str(soup))[0].replace('\\n','\n')

    # Scrapes description with regex
    description_pattern = re.compile('(?<=meta name="description" content=").*(?="><meta name="keywords" content=)')
    description = description_pattern.findall(str(soup))[0].replace('\\n','\n')

    # Saves scrapped data in table format
    with open("Results.html", "a", encoding="utf-8") as file:
            file.write(tabulate([[str(list(video_id_date_dict).index(id) + 1),
                                 "<img src=\"thumbnails/" + id + ".jpg\" height=150 width=200>",
                                 date,
                                 "<a href=\"https://www.youtube.com/watch?v=" + id + "\" target=\"_blank\">" + title + "</a>",
                                 description]], tablefmt='unsafehtml'))

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

# Clears any text from python console window.
os.system('cls' if os.name == 'nt' else 'clear')
# Displays a message on python console once the process is done.
print("All the videos were searched successfully! Please check Results.html file.")
# Stop python console from closing automatically.
input("Press ENTER key to exit!")
