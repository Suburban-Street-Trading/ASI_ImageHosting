import csv
import io
import urllib.request
import requests  # http://docs.python-requests.org/en/master/






# example image url: https://m.media-amazon.com/images/S/aplus-media/vc/6a9569ab-cb8e-46d9-8aea-a7022e58c74a.jpg
def download_image(name ,image_url):
    request =   requests.get(image_url)
    file_location = f'ASI_Images/{name}.jpg'
    print(file_location)
    with open(f'ASI_Images/{name}.jpg', 'wb') as f:
        f.write(request.content)


csv_path = 'ASI_images.csv'
csv_block = csv.reader(open(csv_path,encoding='UTF-8'))

for item in csv_block:
    if item[0] == '﻿SKU':
        continue
    item_number = item[0]
    #print(item_number)
    product_URL = item[6]
    #print(product_URL)
    download_image(item_number,product_URL)
