from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome

import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event

# Fetch the page content

driver = Chrome(service=Service(ChromeDriverManager().install()))

#driver.maximize_window()

wait = WebDriverWait(driver, 60)

url = "https://andersraum.de/aktuelles/#kalender"

driver.get(url)

# Get the HTML response (page source)
response = driver.page_source

soup = BeautifulSoup(response, "html.parser")

# Create a new calendar
cal = Calendar()

# Find calendar data (adjust the selectors as needed)
calendar_table = soup.find_all("table", class_="fc-scrollgrid-sync-table")  # Replace with actual class or tag

for entry in calendar_entries:
    print(entry)
    # Extract date and event details (adjust as per actual HTML structure)
    date = entry.find("span", class_="date").text.strip()  # Replace with the correct tag/class
    event_title = entry.find("span", class_="event-title").text.strip()  # Replace with the correct tag/class
    
    # Create an event
    event = Event()
    event.name = event_title
    event.begin = date  # Ensure date is in 'YYYY-MM-DD' format or adjust parsing
    
    # Add the event to the calendar
    cal.events.add(event)

# Save the calendar to an .ics file
with open("calendar.ics", "w", encoding="utf-8") as file:
    file.writelines(cal)

print("Calendar saved as 'calendar.ics'")



