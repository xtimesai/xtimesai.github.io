#!/bin/bash

# Directory containing your 2024 posts
POSTS_DIR="content/en/post/2024"

# Create a log file
echo "Starting conversion at $(date)" > conversion_log.txt

# Go to posts directory
cd "$POSTS_DIR" || exit

# Process each .md file
for file in *.md; do
    if [ -f "$file" ]; then
        # Get filename without extension
        filename="${file%.*}"
        
        # Create a URL-friendly directory name (replace spaces with hyphens)
        dirname=$(echo "$filename" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g')
        
        # Create directory
        mkdir -p "$dirname"
        
        # Move .md file as index.md
        mv "$file" "$dirname/index.md"
        
        # Log the conversion
        echo "Converted: $file -> $dirname/index.md" >> ../../conversion_log.txt
    fi
done

echo "Conversion completed at $(date)" >> ../../conversion_log.txt