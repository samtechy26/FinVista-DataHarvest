import time
from celery import shared_task
from .scrapers import scrape

@shared_task
def scrape_dev_to():
    URL = "https://dev.to/search?q=django"
    scrape(URL)
    return

