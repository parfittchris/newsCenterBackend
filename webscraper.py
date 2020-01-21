from selenium import webdriver


# CNN--------------------------------
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


# FOX--------------------------------
def get_fox():
    driver = webdriver.Chrome('/usr/local/chromedriver')
    url = "https://www.foxnews.com/"
    driver.get(url)

    # section = driver.find_element_by_class_name("collection-spotlight")
    headlines = driver.find_elements_by_tag_name("article")

    results = []
    counter = 0

    for headline in headlines:
        url = headline.find_elements_by_tag_name("a")
        title = headline.text

        if len(title) > 0 and len(url) > 0:

            obj = {
                'site': 'FOX',
                'title': title,
                'url': url[0].get_attribute("href"),
                'number': counter
                }

            counter += 1
        results.append(obj)
    
    driver.close()
    return results

#  NY Times ----------------------------------
def get_NYT():
    driver = webdriver.Chrome('/usr/local/chromedriver')
    url = "https://www.nytimes.com/"
    driver.get(url)

    headlines = driver.find_elements_by_tag_name("article")

    results = []
    counter = 0

    for headline in headlines:
        url = headline.find_elements_by_tag_name("a")
        title = headline.text

        if len(title) > 0 and len(url) > 0:

            obj = {
                'site': 'NYTimes',
                'title': title,
                'url': url[0].get_attribute("href"),
                'number': counter
            }

            counter += 1
        results.append(obj)

    driver.close()
    return results



# Huffington Post

def get_huff():
    driver = webdriver.Chrome('/usr/local/chromedriver')
    url = "https://www.huffingtonpost.com"
    driver.get(url)

    section_1 = driver.find_element_by_class_name(
        "front-page-top").find_elements_by_class_name("card")
    section_2 = driver.find_element_by_class_name(
        "front-page-content").find_elements_by_class_name("card")
    headlines = section_1 + section_2

    results = []
    counter = 0

    for headline in headlines:
        url = headline.find_elements_by_tag_name("a")
        title = headline.text
        
        if len(title) > 0 and len(url) > 0:
            obj = {
                    'site': 'Huffington Post',
                    'title': title,
                    'url': url[0].get_attribute("href"),
                    'number': counter
                }
            counter += 1
        results.append(obj)
    driver.close()
    return results


# NBC ---------------------------
def get_nbc():
    driver = webdriver.Chrome('/usr/local/chromedriver')
    url = "https://www.nbcnews.com/"
    driver.get(url)

    headlines = driver.find_elements_by_tag_name("article")

    results = []
    counter = 0

    for headline in headlines:
        url = headline.find_elements_by_tag_name("a")
        title = headline.text

        if len(title) > 0 and len(url) > 0:

            obj = {
                'site': 'NBC News',
                'title': title,
                'url': url[0].get_attribute("href"),
                'number': counter
            }

            counter += 1
        results.append(obj)

    driver.close()
    return results


# Washington Post
def get_post():
    driver = webdriver.Chrome('/usr/local/chromedriver')
    url = "https://www.washingtonpost.com/"
    driver.get(url)

    headlines = driver.find_elements_by_tag_name("article")

    results = []
    counter = 0

    for headline in headlines:
        url = headline.find_elements_by_tag_name("a")
        title = headline.text

        if len(title) > 0 and len(url) > 0:

            obj = {
                'site': 'NBC News',
                'title': title,
                'url': url[0].get_attribute("href"),
                'number': counter
            }

            counter += 1
        results.append(obj)

    driver.close()
    return results
