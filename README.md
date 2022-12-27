# Quotes-Webscraping
In this project I've gathered over 2500 quotes from passiton.com/inspirational-quotes
using requests, BeautfulSoup, and html5lib parser.
One challenge was that the website consists of 77 pages about quotes
Each page of the 77 pages contains 33 quotes each stored in subpage

## First, I've downloaded main pages the 77 pages
See main.ipynb file to see all steps undertaken in this project
Notice: main.py contain only the final step or what to do after all
the downloading and parsing html files work.
## Then, I've downloaded sub pages containing the quotes I need 
about 33*77 equals approximately **2541 pages** but might be less as 
33 subpages per main page was just the maximum number of subpages

## At last, I've parsed each subpage to collect three information:
Quote, category, and author which are gathered from each subpage
and appended to a list containing a dictionary
This list, at the end, is converted into a pandas.DataFrame.
## Finally, I've stored the quotes in a csv file using pandas - quotes.csv


# Who am I?

I am Shehab Soliman from Alexandria Egypt.
I am a chemical engineering fresh graduate
I'm also a junior data analyst and a student in Udacity as a part of mutliple scholarships
