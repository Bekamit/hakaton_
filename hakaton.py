# import requests
# from bs4 import BeautifulSoup
# import csv

# URL = 'https://www.link.kg/catalog/1/'

# def write_to_csv(data):
#     with open('link.csv','a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['titles'],data['price_c'],data['price_d']])

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BeautifulSoup(html,'lxml')
#     list_comp = soup.find_all('tr',class_ = 'r1')
#     list_comp = soup.find_all('tr',class_ = 'r2')

#     for comp in list_comp:
#         title_ = comp.find_all('td')
#         price_c = comp.find('td',class_ = 'tp').text.strip(' ').strip('*')  


#         dict_ = {'titles':title_[1].text,'price_c':price_c,'price_d':title_[3].text}

#         write_to_csv(dict_)


# print(get_data(get_html(URL)))

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import requests
# from bs4 import BeautifulSoup
# import csv

# URL = 'https://www.mashina.kg/search/all/?page=1'

# def write_to_csv(data):
#     with open('link.csv','a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['model'],data['price'],data['image'],data['des']])

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BeautifulSoup(html,'lxml')
#     list_car = soup.find_all('div',class_ = 'list-item list-label')


#     for car in list_car:
#         model = car.find('h2',class_ = 'name').text.replace(' ','')
#         price = car.find('p').text.replace(' ','')
#         image = car.find('div',class_ = 'thumb-item-carousel').find('img', class_='lazy-image').get('data-src')
#         description = car.find('div',class_ = 'block info-wrapper item-info-wrapper').text.replace(' ','')

#         print(car)

#         dict_ = {'model':model,'price':price,'image':image,'des':description}


#         write_to_csv(dict_)


# print(get_data(get_html(URL)))




