from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptNotFound, NoTranscriptFound
import re

def get_video_id(url):
    """
    Extracts the video ID from a YouTube URL.
    :param url: YouTube video URL
    :return: Video ID as a string
    """
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL")

def has_transcript(video_url):
    """
    Checks if a YouTube video has a transcript.
    :param video_url: YouTube video URL
    :return: Boolean indicating if transcript exists
    """
    try:
        video_id = get_video_id(video_url)
        YouTubeTranscriptApi.get_transcript(video_id)
        return True
    except (TranscriptNotFound, NoTranscriptFound):
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    video_url = input("Enter a YouTube video URL: ")
    if has_transcript(video_url):
        print("The video has a transcript available.")
    else:
        print("No transcript is available for this video.")
