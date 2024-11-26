import asyncio
import json
from crawl4ai import AsyncWebCrawler
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def main():
    try:
        # Create output directory
        output_dir = "nbc_news_crawl"
        os.makedirs(output_dir, exist_ok=True)
        
        # Crawl the NBC News page
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(url="https://www.nbcnews.com/news/world/israel-hezbollah-move-closer-cease-fire-rcna181631")
            
            # Save full result as JSON
            json_path = os.path.join(output_dir, "business_news.json")
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(result.model_dump(), f, indent=2, ensure_ascii=False)
            
            # Save key information as Markdown
            markdown_path = os.path.join(output_dir, "business_news.md")
            with open(markdown_path, "w", encoding="utf-8") as md_file:
                md_file.write(f"# Crawl Results for {result.url}\n\n")
                md_file.write(f"**Success:** {result.success}\n\n")
                md_file.write(f"**Status Code:** {result.status_code}\n\n")
                md_file.write(f"## Metadata\n")
                for key, value in result.metadata.items():
                    md_file.write(f"- **{key.capitalize()}:** {value}\n")
                
                md_file.write("\n## Extracted Links\n")
                for link_type, links in result.links.items():
                    md_file.write(f"### {link_type.capitalize()} Links:\n")
                    for link in links:
                        md_file.write(f"- {link}\n")
            
            # Log important information
            logging.info("\n--- Crawl Results ---")
            logging.info(f"JSON saved to: {json_path}")
            logging.info(f"Markdown saved to: {markdown_path}")
            logging.info(f"URL: {result.url}")
            logging.info(f"Success: {result.success}")
            logging.info(f"Status Code: {result.status_code}")
            
            # Print out key metadata and links
            logging.info("\n--- Metadata ---")
            for key, value in result.metadata.items():
                logging.info(f"{key}: {value}")
            
            logging.info("\n--- Extracted Links ---")
            for link_type, links in result.links.items():
                logging.info(f"{link_type.capitalize()} Links:")
                for link in links:
                    logging.info(f"  - {link}")

    except Exception as e:
        logging.error(f"An error occurred during crawling: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
