import subprocess
import math
import sys
import os

def process_video_segments(input_file, output_file):
    """
    Processes a video file using FFmpeg, creating jump-blackout effect
    by segmenting and concatenating.
    """
    temp_dir = None  # Initialize temp_dir to None
    try:
        # Get video duration and resolution
        ffprobe_cmd = [
            "ffprobe",
            "-v",
            "error",
             "-select_streams", "v:0", # Select only the first video stream
            "-show_entries",
            "format=duration,stream=width,height",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            input_file,
        ]
        ffprobe_output = subprocess.run(
            ffprobe_cmd, check=True, capture_output=True, text=True
        )
        ffprobe_lines = ffprobe_output.stdout.strip().split("\n")
        
        if len(ffprobe_lines) < 3:
           print("Error: Could not get video duration, width, or height from ffprobe. Check the input file or format.")
           return

        total_duration = float(ffprobe_lines[0])
        width = int(ffprobe_lines[1])
        height = int(ffprobe_lines[2])

        segment_duration = 5
        black_duration = 10
        interval_duration = segment_duration + black_duration
        num_segments = math.ceil(total_duration / interval_duration)

        # Create temporary directory
        temp_dir = "temp_segments"
        os.makedirs(temp_dir, exist_ok=True)
        
        concat_list_path = os.path.join(temp_dir, 'concat_list.txt')
        with open(concat_list_path, 'w') as f:
        
            for i in range(num_segments):
                start_time = i * interval_duration
                segment_output = os.path.join(temp_dir, f"segment_{i}.mp4")
                black_output = os.path.join(temp_dir, f"black_{i}.mp4")

                # Trim video segment
                trim_cmd = [
                    "ffmpeg",
                     "-y", # overwrite existing files
                    "-i", input_file,
                     "-ss", str(start_time),
                     "-t", str(segment_duration),
                    "-c", "copy", segment_output
                ]
                subprocess.run(trim_cmd, check=True, capture_output=True, text=True)

                 # Generate black screen
                black_cmd = [
                    "ffmpeg",
                     "-y",  # overwrite existing files
                    "-f", "lavfi",
                    "-i", f"nullsrc=duration={black_duration}:size={width}x{height}:rate=1,format=yuv420p,color=black",
                    black_output
                 ]
                subprocess.run(black_cmd, check=True, capture_output=True, text=True)
                
                # Add the segment and black video to the text file to be used for concat
                f.write(f"file '{segment_output}'\n")
                f.write(f"file '{black_output}'\n")

        # Concatenate the segments using ffmpeg concat demuxer.
        concat_cmd = [
            "ffmpeg",
             "-y",
            "-f",
            "concat",
            "-safe", "0",
            "-i",
            concat_list_path,
            "-c", "copy", # do not re-encode.
            output_file
        ]

        subprocess.run(concat_cmd, check=True, capture_output=True, text=True)
        print("Video processed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"Error processing video: {e}")
        print("FFmpeg output (stderr):")
        print(e.stderr)
    except ValueError as e:
        print(f"Error with duration calculation: {e}")
    finally:
        # Clean up temporary directory and files (if temp_dir was created)
        if temp_dir and os.path.exists(temp_dir):
             for item in os.listdir(temp_dir):
                 file_path = os.path.join(temp_dir,item)
                 if os.path.isfile(file_path):
                     os.remove(file_path)
             os.rmdir(temp_dir)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
    else:
        input_video = sys.argv[1]
        output_video = sys.argv[2]
        process_video_segments(input_video, output_video)