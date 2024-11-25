from pytube import Playlist
import os
import requests

def download_thumbnails(playlist_url):
    playlist = Playlist(playlist_url)
    for video in playlist.videos:
        try:
            video_title = video.title.replace("/", "-").replace(":", "-").replace("?", "-").replace("!", "-").replace("'", "-").replace('"', "-")
        except Exception as e:
            video_title = "Unknown_Title"
            print(f"Error accessing video title: {e}")
        
        try:
            thumbnail_url = video.thumbnail_url
            thumbnail_path = os.path.join("assets", "img", f"{video_title}.jpg")
            os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)
            with open(thumbnail_path, "wb") as f:
                f.write(requests.get(thumbnail_url).content)
            print(f"Thumbnail for '{video_title}' downloaded successfully.")
        except Exception as e:
            print(f"Error downloading thumbnail for '{video_title}': {e}")

if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PL6i60qoDQhQGaGbbg-4aSwXJvxOqO6o5e"
    download_thumbnails(playlist_url)
