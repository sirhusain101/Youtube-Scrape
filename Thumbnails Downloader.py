import urllib.request
import os.path
from video_ids import video_id_date_dict    # Check comments in create_video_date_dict.py for more info

# Youtube saves thumbnails like this = https://i.ytimg.com/vi/VIDEO-ID/hqdefault.jpg

# create thumbnails folder
while True:
    try:
        thumbnail_folder = "thumbnails"
        os.mkdir(thumbnail_folder)
    except FileExistsError:
        break

# download thumbnails
for id, date in video_id_date_dict.items():
    if os.path.isfile(os.path.join("./thumbnails/" + id + ".jpg")) is True:
        continue
    urllib.request.urlretrieve("https://i.ytimg.com/vi/" + id + "/hqdefault.jpg", os.path.join("./thumbnails", id + ".jpg"))

    # Clears any text from python console window.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Displays whichever thumbnail is being downloaded
    print("(" + str(list(video_id_date_dict).index(id) + 1) + "/" + str(
        len(video_id_date_dict)) + ") | Downloading: " + id + ".jpg")

# Clears any text from python console window.
os.system('cls' if os.name == 'nt' else 'clear')
# Displays a message on python console once the process is done.
print("All the videos were downloaded successfully! Please check thumbnails folder.")
# Stop python console from closing automatically.
input("Press ENTER key to exit!")