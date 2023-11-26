import datetime
from dateutil.relativedelta import relativedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .models import NewsItem

def scrape(url):
    options = webdriver.FirefoxOptions()

    options.add_argument(" - incognito")

    browser = webdriver.Firefox()

    browser.get(url)

    timeout = 10

    try:
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(
            (By.XPATH, 
            "//div[@class='substories search-results-loaded']"
            )
            )
        )
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()

    # find all the elements with this class single article single-article-small-pic
        
    article_elements = browser.find_elements("xpath",
        "//article[@class='crayons-story']")
    
    

    for article in article_elements:
        if article.get_attribute('data-content-user-id') != "undefined":
            # try get the anchor tag and href
            result = article.find_element("xpath",
                ".//a[@class='crayons-story__hidden-navigation-link']")
            news_item_link = result.get_attribute('href')
            #result_title = article.find_element("xpath", ".//h3[@class='crayons-story__title']")
            # try get title
            title_result = article.find_element(By.TAG_NAME,'h3')
            news_item_title = title_result.text
            

            two_years_ago = datetime.date.today() - relativedelta(years=2)

            # try get timestamp
            timestamp_result = article.find_element(By.TAG_NAME, 'time')
            news_item_time = timestamp_result.text
            
            # try get timestamp

            # no articles older than 2 years
            

            

            # convert the news_item_time into python date object
            if "'" in news_item_time:
                # parse the year
                new_item_date = datetime.datetime.strptime(
                    news_item_time, "%b %d '%y").date()

            else:
                # the year is the current year
                new_item_date = datetime.datetime.strptime(
                    news_item_time, "%b %d")
                today = datetime.date.today()
                new_item_date = new_item_date.replace(
                    year=today.year).date()
            
            

            # if new_item_date > two_years_ago:
            NewsItem.objects.get_or_create(
                title=news_item_title,
                link=news_item_link,
                source='Dev.to',
                publish_date=new_item_date
            )
    browser.quit()


