# Shaadi.com Success Story Web Scraper

This is a Python web scraper that extracts the success stories of couples from the Shaadi.com website. The scraper uses Selenium for browser automation, BeautifulSoup for HTML parsing, and Pandas for data manipulation.

## Prerequisites

Before running the scraper, make sure you have the following prerequisites installed:

- Python 3.x
- Google Chrome (or any other compatible web browser)
- ChromeDriver (make sure it's compatible with your Chrome version and operating system)

## Installation

1. Clone the repository or download the source code.
```
git clone https://github.com/sonisumit7904/Shaadi_Success_Story_Web_Scrapper.git
```
2. Install the required Python packages by running the following command:
```
pip install -r requirements.txt
```
3. Download the appropriate ChromeDriver for your operating system and Chrome version from the official website: https://chromedriver.chromium.org/downloads
4. Extract the ChromeDriver executable and place it in a directory included in your system's `PATH` environment variable.

## Usage

1. Open the Python script `scraper.py` in a text editor.
2. Modify the script as needed, such as Changing the `Chrome Driver Path`
3. Save the changes to the script.
4. Run the script from the command line:
```
python scraper.py
```

The scraper will launch a Chrome browser instance, navigate to the Shaadi.com website, and extract the success stories of couples. The extracted data will be stored in a CSV file or processed as specified in the script.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.