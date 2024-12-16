import os
import sys
from pytube import YouTube
import subprocess

def download_youtube_audio(url, output_path=None):
    """
    Download audio from a YouTube video and save as MP3 using FFmpeg.
    
    Args:
    url (str): YouTube video URL
    output_path (str, optional): Directory to save the MP3. 
                                 Defaults to current directory.
    
    Returns:
    str: Path to the downloaded MP3 file
    """
    try:
        # Create output directory if not specified
        if output_path is None:
            output_path = os.getcwd()
        else:
            os.makedirs(output_path, exist_ok=True)
        
        # Download the YouTube video
        yt = YouTube(url)
        
        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Generate a safe filename
        safe_title = "".join(x for x in yt.title if x.isalnum() or x in [' ', '-', '_']).rstrip()
        temp_file = os.path.join(output_path, f"{safe_title}_temp{os.path.splitext(audio_stream.default_filename)[1]}")
        mp3_path = os.path.join(output_path, f"{safe_title}.mp3")
        
        # Download the audio stream
        print(f"Downloading audio from: {yt.title}")
        audio_stream.download(output_path=output_path, filename=os.path.basename(temp_file))
        
        # Convert to MP3 using FFmpeg
        try:
            subprocess.run([
                'ffmpeg', 
                '-i', temp_file, 
                '-vn',  # Ignore video
                '-acodec', 'libmp3lame',  # Use MP3 codec
                '-q:a', '2',  # High quality
                mp3_path
            ], check=True)
            
            # Remove the temporary file
            os.remove(temp_file)
            
            print(f"Audio downloaded successfully: {mp3_path}")
            return mp3_path
        
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg conversion error: {e}")
            return None
        except FileNotFoundError:
            print("FFmpeg not found. Please install FFmpeg:")
            print("macOS (Homebrew): brew install ffmpeg")
            print("Windows: Download from ffmpeg.org")
            print("Linux: sudo apt-get install ffmpeg")
            return None
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Check if URL is provided as a command-line argument
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    else:
        video_url = input("Enter YouTube video URL: ")
    
    download_youtube_audio(video_url)