from aip import AipOcr
APP_ID = '11394681'
API_KEY = 'UV8a1KOWokF4kYx4AiD4V9NX'
SECRET_KEY = 'uNwhkOv56NaIlz9DDVZHn8fAV8oxN9Tg'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content('Picture.png')
info = []
sum = client.basicGeneral(image)['words_result']
for i in range(len(sum)):
    result = sum[i]['words']
    info.append(result)

# result = client.basicGeneral(image)['words_result'][1]['words']
# result = list(map(lambda x:int(x),list(client.basicGeneral(image)['words_result'][0]['words'])))
results = print(''.join(info))