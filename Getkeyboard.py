import keyboard
from aip import AipOcr
from PIL import ImageGrab
import time
import sys
def screenShot():
    info = []
    for _ in range(sys.maxsize):
        APP_ID = '11394681'
        API_KEY = 'UV8a1KOWokF4kYx4AiD4V9NX'
        SECRET_KEY = 'uNwhkOv56NaIlz9DDVZHn8fAV8oxN9Tg'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                return fp.read()
        # 截图开始
        if keyboard.wait(hotkey='ctrl+alt+0') == None:
            # print(keyboard.wait(hotkey='ctrl+alt+0') )
            # 截图条件
            if keyboard.wait(hotkey='enter') ==None:
                # 防止获取上一张截图
                # 复制剪切板图片
                time.sleep(0.01)
                im = ImageGrab.grabclipboard()
                im.save('Picture.png')
                image = get_file_content('Picture.png')
                sum = client.basicGeneral(image)['words_result']
                for i in range(len(sum)):
                    result = sum[i]['words']
                    info.append(result)
            print(''.join(info))
        
screenShot()

