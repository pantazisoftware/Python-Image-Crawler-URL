#Importa modulele necesare
# import pandas as pd
import urllib.request


def url_to_jpg(i):

    urlgen = 'http://eduardpantazi.com/crawler/test-{}.png'.format(i)
    filename = 'test6-{}.jpg'.format(i)
    full_path = '{}{}'.format('imagini/', filename) #save in "imagini/" with the name of "image-1.jpg" and so on...
    urllib.request.urlretrieve(urlgen, full_path) #acces the url based on i value and download file

    print('#{} - Original URL: {} // saved at: {}'.format(i, urlgen, full_path))

    return None



# urls = pd.read_csv(FILENAME)
# print(urls)
print('Numar start:')
fromNum = int(input())
print('Numar final:')
toNum = int(input())

for i in range(fromNum,toNum):
    url_to_jpg(i)




