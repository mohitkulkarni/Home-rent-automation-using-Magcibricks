import requests
from bs4 import BeautifulSoup


class SoupData:
    def __init__(self, url):
        response = requests.get(url)
        page_source = response.text
        self.soup = BeautifulSoup(page_source, "html.parser")

    def title_search(self):
        title_list = []
        all_titles = self.soup.find_all('span', class_="m-srp-card__title")

        title_unsorted = [title.get_text() for title in all_titles]
        for sort in title_unsorted:
            sorted_title_list = sort.split()
            del sorted_title_list[:6]
            main_title = ""
            for string in sorted_title_list:
                main_title += f"{string} "
            title_list.append(main_title)
        return title_list

    def price_search(self):
        all_prices = self.soup.find_all('div', class_='m-srp-card__price')
        price_list_unsorted = [price.get_text() for price in all_prices]

        price_list = []
        for sort in price_list_unsorted:
            sorted_price_list = sort.split()
            price_list.append(sorted_price_list[1])
        return price_list

    # def link_search(self):
    #     al_links =
