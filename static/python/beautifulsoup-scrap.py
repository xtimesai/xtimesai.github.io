import requests
from bs4 import BeautifulSoup

# URL of the article
url = "https://www.nbcnews.com/news/world/israel-hezbollah-move-closer-cease-fire-rcna181631"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

# Sending a GET request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extracting the article content
content = []
for paragraph in soup.find_all("p"):
    content.append(paragraph.text)

# Join paragraphs into a single Markdown content
markdown_content = "# Cease-Fire Deal Close Between Israel and Hezbollah\n\n" + "\n\n".join(content)

# Filepath to save the Markdown file
output_path = r"C:\Users\daily\OneDrive\Documents\GitHub\xtimesai.github.io\static\python\israel-hezbollah-ceasefire.md"

# Writing content to the Markdown file
with open(output_path, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_content)

print(f"Markdown file saved at: {output_path}")
