## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python
The goal of this first script was to scrape the 5-day weather forecast from the National Weather Service website. It extracts information listed in one class using BeautifulSoup, a common library for webscraping. It takes a user input latitude and longitude value to create a URL. From this URL, it prints an output of a well formatted five day forecast. 

In previous research, specifically with the geography program at Clark University, I had to extract weather data as part of my researching on tree cooling. While this was all done manually, being able to use a python code like this is something I could see using. Taking a series of lat/long values from an excel sheet to generate if not a full five day forecast, but weather conditions that are required variables to simulate different heating or cooling urban models, would be a code that could be helpful to future research along these lines. Additionally, because this script takes multiple elements from one class, it is a code that will be helpful in future cases to extract more than one piece of information from each class. 

## Final Project: Script 2
### Web-scrapping Internet Archive's Wayback Machine
For my second script, I followed and modified the webscrapping tool created here: https://medium.com/analytics-vidhya/the-wayback-machine-scraper-63238f6abb66 by Abhi Kumbar. The purpose of this code was to take a compiled set of URLs using the Wayback Machine API and then scrape information such as an article summary, title and URL from each of those compiled URLs for a given website. 

My code uses the same example Wayback Machine API compiled URL for archived NBC news articles that this code used. For my code, I made a few changes so that the code takes a user input of a "keyword" and searches through each of these URL webpages to then output article titles and URLs containing that keyword. First, the code breaks down the compiled URL package to create a URL that loads a page of the Wayback Machine. From that page, it extracts the URL and article title from the div tags. Finally, it places this information into an empty list. Next, using the user input code word, the code separates out the article title into individual words to get if it contains the keyword. If so, it prints the Article title and URL. This code would be helpful for research projects looking at how different news organizations have reporter on a certain issue over time. For example, you could use it to compare how many articles NYT or NBC or Fox News created about the Times Up movement, or about the capital insurection prior to Biden's inauguration.

## Reflection: Details, Difficulties and Debugging
Initially, I found this script very challenging and ended up switching projects from an attempt to automate excel spreadsheet analysis into this project. This is partially because I found even looking for help difficult to understand -- a lot of the language or assumed knowledge on coding pages or help pages were something that challenged me during this lab. On the other hand, the Wayback Machine is one of my favorite websites -- I think it's a very cool project and has a lot of information that could be really interesting to analyze or look at, so I did end up getting really excited about my new project!

Following along with the Medium tutorial code was challenging with syntax or functions that I had never seen before playing a key role; I relied on Stackoverflow and python's own dictionaries to look up any coding language I didn't recognize to understand what they did. Similarly, API's were a concept that I was familiar with -- I used the Wayback Machine's documentation page and the linked GitHub repository for the API I ended up using in order or understand what it did and how it worked. However, the most helpful tool for this project was the previous colab documents I had from class lectures or notes I had taken in the book. It helped me adjust me syntax and by using the technique of building and testing the code in small pieces, slowly, one at a time, I was able to personalize and experiment with Abhi Kumbar's Wayback Webscrapper code. 

dditionally, you should describe the process of writing the script: was it easy, hard, what challenges or errors did you face and how did you resolve them? If you use any resources to help write your code (e.g. Stackoverflow.com; the text book; etc.), please link to them in the body of your text. E.g. “After repeated syntax errors, I checked Stackoverflow.com to find that…” Use Markdown to format your text and link to a specific online resources that you used.

