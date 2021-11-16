# ----------------------------- Home Rent automation using Magcibricks -----------------------------------
from capture import DataSearch
from data import SoupData
from sender import SendData

# ------------------google form url here----------
GOOGLE_FORM_URL = "google-form-link"
SEARCH_LOCATION = "Pune"
MAX_BUDGET = "20000"

data_search = DataSearch()
data_search.search(location=SEARCH_LOCATION, budget=MAX_BUDGET)

soup_data = SoupData(url=data_search.get_url())

my_title_list = soup_data.title_search()
my_price_list = soup_data.price_search()

# my_link_list = soup_data.link_search()
# print(my_link_list)

send_data = SendData(sheet_url=GOOGLE_FORM_URL)

for index in range(len(my_title_list)):
    send_data.send_address(my_title_list[index])
    send_data.send_price(my_price_list[index])
    send_data.send()

