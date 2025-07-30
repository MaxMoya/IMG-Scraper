IMG-Scraper


This repository contains a simple yet effective Python command-line tool for scraping and downloading images from a specified URL. The scraper is designed to be easy to use, allowing you to quickly save all image assets from a webpage to a local directory.

Key Features
URL-based Scraping: Accepts a URL as input and extracts all <img> tags.

Efficient Downloading: Uses the requests library to download images asynchronously.

Organized Output: Downloads images into a designated directory for easy access.

Minimal Dependencies: Built with common and lightweight Python libraries.

Technologies Used
Python 3

requests: For making HTTP requests to download the webpage and image files.

BeautifulSoup4: For parsing the HTML content and finding all image URLs.

Installation
Clone the repository to your local machine:

Bash

git clone https://github.com/MaxMoya/IMG-Scraper.git
cd IMG-Scraper
Install the required dependencies using pip:

Bash

pip install -r requirements.txt
Usage
To use the scraper, simply run the main.py script from your terminal and provide the URL of the website you want to scrape as an argument.

Bash

python main.py <URL_TO_SCRAPE>
Example:
To scrape all images from https://www.wikipedia.org/ and save them to a local directory, you would run:

Bash

python main.py https://www.wikipedia.org/
The scraper will create a new folder named scraped_images in the root directory of the project and download all the images into it.

File Structure
main.py: The main script that handles the web scraping and downloading logic.

requirements.txt: Lists all the necessary Python libraries for the project.

Potential Enhancements
Add command-line arguments to specify the output directory and the types of images to download.

Implement a recursive option to scrape images from linked pages as well.

Add support for scraping images from dynamic websites that use JavaScript to load content.

Include error handling for invalid URLs or failed download attempts.
