import os
from bs4 import BeautifulSoup as bs

folder_name = 'html_pages'
df_list = []

for html_file in os.listdir(folder_name):
    if os.path.isfile(folder_name+'/'+html_file):
        f = os.path.join(folder_name,html_file)
        with open(f, encoding='utf-8') as html_doc:
            soup = bs(html_doc, 'html5lib')
            df_list.append(
                {
                'Quote': soup.find('h5').text[1:-1],
                'Category': soup.find('h5',class_='value_on_red').text,
                'Author': soup.find('p').text
                }
            )
# xlsxwriter enine is used due to the existence of Unicode characters
df = pd.DataFrame(df_list, columns=['Quote','Category','Author'])
df = df.applymap(lambda x: x.encode('unicode_escape').
                 decode('utf-8') if isinstance(x, str) else x)

df.to_csv('quotes.csv', encoding='UTF-8')
# Encoding: UTF-8 - is the most popular encoding of web pages
print('DONE')