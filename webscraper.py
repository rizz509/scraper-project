from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def webscr(out_url):
    filename = "iteminfo.csv"
    f = open(filename, "w")
    headers = "Item_name,Item_seller,Ad_date,Item_price\n"
    f.write(headers)
    total_data = ""
    for page in range(0, 41, 20):
        #my_url = 'http://hamrobazaar.com/c2-mobile-and-accessories?catid=2&order=popularad&offset=0' + str(page)
        # my_url = 'http://hamrobazaar.com/c62-automobiles-motorcycle?catid=62&order=popularad&offset=0' + str(page)
        my_url = out_url + str(page)
        # open url,downloads page
        req_client = uReq(my_url)
        # reads page html and stores in variable
        page_html = req_client.read()
        # page_html is the raw html file
        # closing the connection
        req_client.close()
        html_soup = soup(page_html, "html.parser")
        item_name = html_soup.findAll("td", {"bgcolor": ["#F2F4F9", "#ECF0F6"], "height": "110"})
        item_date = html_soup.findAll("td", {"bgcolor": ["#F2F4F9", "#ECF0F6"], "width": "90"})
        item_price = html_soup.findAll("td", {"bgcolor": ["#F2F4F9", "#ECF0F6"], "width": "100"})
        j = 0
        for i in item_name:
            col1 = i.b.text
            y = i.findAll("a", {})
            col2 = y[1].text
            col3 = item_date[j].text
            try:
                col4 = item_price[j].b.text
            except:
                col4 = item_price[j].text
            j = j + 1
            total_data = total_data + col1.replace(",", "|") + "," + col2.replace(",", "|") + "," + col3.replace(",",
                                                                                                                 "|") + "," + col4.replace(
                ",", "|") + "\n"
            # print(col1.replace(",","|")+","+col2.replace(",","|")+","+col3.replace(",","|")+","+col4.replace(",","|")+"\n")
    f.write(total_data)
    f.close()