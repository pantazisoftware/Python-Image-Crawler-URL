
# Import module
import urllib.request


# Create the logic for the files to be saved
def url_to_jpg(i):

    urlgen = 'http://eduardpantazi.com/crawler/test-{}.png'.format(i)
    filename = 'test6-{}.jpg'.format(i)
    full_path = '{}{}'.format('imagini/', filename) #s
    urllib.request.urlretrieve(urlgen, full_path) 

    print('#{} - Original URL: {} // saved at: {}'.format(i, urlgen, full_path))

    return None

# Print from what number to start trough last number
print('Numar start:')
fromNum = int(input())
print('Numar final:')
toNum = int(input())

# Execute a loop with the method above based on the numbers given
for i in range(fromNum,toNum):
    url_to_jpg(i)




