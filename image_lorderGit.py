import csv
import requests  # http://docs.python-requests.org/en/master/
import shutil # to save it locally





import time
# example image url: https://m.media-amazon.com/images/S/aplus-media/vc/6a9569ab-cb8e-46d9-8aea-a7022e58c74a.jpg
def download_image(name ,image_url):
    try:
        request =   requests.get(image_url, timeout=5)
        print(request)
        # Check if the image was retrieved successfully
        if request.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            request.raw.decode_content = True

            file_location = f'ASI_Images/{name}.jpg'
            print(file_location, request.status_code)
            with open(file_location, 'wb') as f:
                shutil.copyfileobj(request.raw, f)
                f.close()
    except:
        fail_List=[]
        fail_List.append((name,image_url))



csv_path = 'ASI_images.csv'
csv_block = csv.reader(open(csv_path,encoding='UTF-8'))


count = 0
for item in csv_block:
    if item[0] == '﻿SKU':
        continue
    count +=1
    item_number = item[0]
    #print(item_number)
    if item[6] =='':
        continue
    product_URL = item[6]
    #print(product_URL)
    download_image(item_number,product_URL)
    print(count)

