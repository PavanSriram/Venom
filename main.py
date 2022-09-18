import urllib.request as req
import re

#starting url
seed = 'https://en.wikipedia.org/wiki/Main_Page'

#visited urls
visited_urls = []

#url queue
urls = ['https://en.wikipedia.org/wiki/Main_Page', '']

#depths
curr_depth = 0
max_depth = 2

while(curr_depth <= max_depth):
    curr_url = urls.pop(0)
    if(curr_url == ''):
        curr_depth += 1
        urls.append('')
        print('\n')
        continue
    
    if(curr_url in visited_urls):
        continue

    print(curr_url)
    visited_urls.append(curr_url)

    #scraping the website
    try:
        page = req.urlopen(curr_url)
        if(page):
            html = page.read().decode('utf8')
            lines = html.split('\n')
            for line in lines:
                # print(line)
                match = re.search(".href=\"(.[^\"])*\"", line)
                # if(match):
                #     print(match.group(0))
                if(match):
                    link = match.group(0)[7:-1]
                    print(link)
                    urls.append(link)
    except:
        print('I dont know what i am doing')



