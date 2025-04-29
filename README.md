# Poetry Foundation Scraper 📝

This project is a Python 3.11+ web scraper that collects all "Coming-of-Age" poems from [The Poetry Foundation](https://www.poetryfoundation.org/categories/coming-of-age).

It handles **JavaScript-based pagination** using Selenium and ChromeDriver and writes the poem titles and links to a timestamped `poems.txt` file.

---

## ✨ Features

- Scrapes poem titles and URLs across 28 dynamically loaded pages
- Navigates complex JavaScript pagination (no static URLs)
- Handles ChromeDriver setup, errors, and duplicates
- Produces clean, readable output
- Built for extensibility: can be expanded to scrape full poem content, authors, etc.

---

## 🛠 Requirements

- Python 3.11+
- Google Chrome (latest version)
- Matching [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/)
- Selenium

Install dependencies:
```bash
pip install selenium
brew install chromedriver
