import pandas as pd
import requests
from bs4 import BeautifulSoup

def extract_article_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.select_one('h1').get_text()  # selector for the title
        # print(title)
        article_text=soup.find('div',{"class":"td-post-content"}).get_text()  
        # article_text=soup.select_one('div.td-post-content')
        # result_text=""
        # for p_tag in article_text.find_all('p'):
        #     result_text+=p_tag.get_text+ ' '

        # print(result_text)
        # article_text = soup.select_one('.article-content').get_text()  
        
        # for data in soup.select('title'):

            # print(data.get_text())
            # Example selector for the article text

        return title, article_text
    except Exception as e:
        # print(f"Error extracting information from {url}: {e}")
        return None, None

def process_input_xlsx(input_file):
    df = pd.read_excel(input_file)

    for index, row in df.iterrows():
        print(index, row)
        url = row['URL']
        # print(url)
        #  'NoneType' object has no attribute 'get_text'

        title,article_text = extract_article_info(url)

        if title is not None and article_text is not None:
            # Save the title and article text in a text file
            output_filename = f"{row['URL_ID']}.txt"  # Adjust the filename as per your requirement
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(f"Title: {title}\n\n{article_text}")

if __name__ == "__main__":
    input_xlsx_file = 'Input.xlsx'
    process_input_xlsx(input_xlsx_file)
