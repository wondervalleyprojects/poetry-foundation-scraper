from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime

# === SETUP BROWSER ===
options = Options()
options.add_argument('--headless')  # Run headless
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# === OPEN INITIAL PAGE ===
driver.get("https://www.poetryfoundation.org/categories/coming-of-age")
sleep(3)  # Wait for page to fully load

poems = set()
current_page = 1

# === PAGINATION LOOP ===
while True:
    print(f"Scraping page {current_page}...")

    # Find all poem links
    poem_tags = driver.find_elements(By.CLASS_NAME, "link-underline-on")

    for tag in poem_tags:
        try:
            title = tag.text.strip()
            link = tag.get_attribute("href")
            if title and link and "poems" in link:
                poems.add((title, link))
        except Exception as e:
            print(f"Skipping a tag due to error: {e}")
            continue

    # Try to find the "Next Page" button
    try:
        next_button = driver.find_element(By.XPATH, '//button[@aria-label="Next Page"]')
        next_button.click()
        sleep(2)  # Wait for next page content to load
        current_page += 1
    except Exception as e:
        print(f"No more pages or error: {e}")
        break

# === WRITE RESULTS TO FILE ===
output_file = "poems.txt"
with open(output_file, "w") as f:
    f.write("Coming-of-Age Poems from Poetry Foundation\n")
    f.write(f"Scraped on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    for title, link in sorted(poems):
        f.write(f"{title} — {link}\n")

print(f"\n✅ Done! Scraped {len(poems)} unique poems.")
print(f"Results saved to {output_file}")
driver.quit()
