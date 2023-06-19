import requests
from datetime import datetime

def check_social_media(username, platform, url_template):
    response = requests.get(url_template.format(username))
    if response.status_code == 200:
        return f"{platform}: {url_template.format(username)}"
    else:
        return None

def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.write(data + "\n")

# Get local and public IP addresses
local_ip = requests.get("https://api.ipify.org").text
public_ip = requests.get("https://api.ipify.org?use-https=true").text

# Write IP addresses with date to the log file
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
write_to_file("iplog.txt", f"Date: {current_time}")
write_to_file("iplog.txt", f"Local IP: {local_ip}")
write_to_file("iplog.txt", f"Public IP: {public_ip}\n")

username = input("Please enter your username: ")

# Social media platform URLs for checking
social_media_urls = {
    "Instagram": "https://instagram.com/{}",
    "Facebook": "https://facebook.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Twitter": "https://twitter.com/{}",
    "GitHub": "https://github.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Medium": "https://medium.com/@{}",
    "YouTube": "https://www.youtube.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "WordPress": "https://{}.wordpress.com/",
    "Gmail": "https://mail.google.com/{}",
    "Dailymotion": "https://www.dailymotion.com/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Vimeo": "https://vimeo.com/{}",
    "VK": "https://vk.com/{}",
    "About.me": "https://about.me/{}",
    "SlideShare": "https://www.slideshare.net/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Canva": "https://www.canva.com/{}",
    "Wikipedia": "https://en.wikipedia.org/wiki/User:{}"
}

# Check the username on social media platforms
found_links = []
for platform, url_template in social_media_urls.items():
    link = check_social_media(username, platform, url_template)
    if link:
        found_links.append(link)

# Write found links to the file
if found_links:
    write_to_file("users.txt", f"Username: {username}")
    for link in found_links:
        write_to_file("users.txt", link)
else:
    print("Username not found.")

print("Process completed.")