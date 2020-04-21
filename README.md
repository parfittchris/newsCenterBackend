# News Center Backend - Webscraper and API for news articles on popular news sites





### NOTE: This API no longer serves the News Center Frontend. I built a new API using Scrapy instead of Selenium and the app is getting its info from that. The link for the scrapy backend is here: https://github.com/parfittchris/newsCenterAPI.





## Background and Overview
This app(used to) serves as the backend api for my News Center app (https://github.com/parfittchris/newscenter_app). It was built in Flask and features a scheduling feature that automatically re-scrapes the news sites every 3hours to keep content up-to-date. The webscraping itself is done using Selenium.


## Features

### Web Scraper
Uses Selenium to scrape Cnn, Fox News, Huffington Post, NBC, and NY Times home pages for their front page news articles and links. The results are sent back to the main app file where they are stored in the SQL database.

```
def get_cnn():
    driver = webdriver.Chrome('/usr/local/chromedriver')
    url = "http://www.cnn.com"
    driver.get(url)

    section = driver.find_element_by_id("homepage1-zone-1")
    headlines = section.find_elements_by_tag_name("article")

    results = []
    counter = 0

    for headline in headlines:
        url = headline.find_elements_by_tag_name("a")
        title = headline.text

        if len(title) > 0 and len(url) > 0:

            obj = {
                'site': 'CNN',
                'title': title,
                'url': url[0].get_attribute("href"),
                'number': counter
                }
                
            counter += 1
        results.append(obj)

    driver.close()
    return results
 ```
 
 
### Flask API
Main app and api built using Flask. Features a scheduler that calls the scraping methods every 3 hours and a function that stores those results in the SQL database.

```
def add_article(obj, organization):
    for article in obj:
        site = article['site']
        title = article['title']
        url = article['url']
        number = article['number']

        current = Article.query.filter(
            Article.number == number, Article.site == organization).first()

        if current:
            current.site = site
            current.title = title
            current.url = url
            current.number = number
            db.session.commit()
        else:
            new_article = Article(site, title, url, number)
            db.session.add(new_article)
            db.session.commit()
   ```
   
   ## Future Updates
   * Add more websites for front end feature that allows user to choose specific news organizations to look at



 
