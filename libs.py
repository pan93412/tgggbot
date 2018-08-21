'''
咕咕機器人所使用的各項函式。

建議不要修改此處的任何程式碼，
若修改很有可能發生問題，除非您
十分清楚目的。

若要用於您的程式，請標註作者 pan93412
和此 GitHub 庫網址。
'''
import requests
import random

# 機器人函式
# 需要的元件：requests
class botHandler:
    '''
    bot 機器人處理 class

    bot_token
        bot 機器人 token (@BotFather)
    '''
    def __init__(self, bot_token):
        self.url = "https://api.telegram.org/bot{}/".format(bot_token)
    def getMe(self):
        '''取得 bot 資訊'''
        return requests.get(self.url + "getMe").json()
    def getUpdates(self, clean_prev_msg = True):
        '''
        取得 bot 抓取到的訊息

        clean_prev_msg
            是否清除過往訊息
        '''
        result = requests.get(self.url + "getUpdates").json()['result']
        if len(result) != 0:
            print("[INFO] 接收到訊息！")
            if clean_prev_msg == True:
                print("[INFO] 已清空接收到的訊息！")
                requests.get(self.url + "getUpdates", params={'offset': result[-1]['update_id'] + 1}).json()
            return result
        else:
            return False

    def sendMessage(self, getUpdates, msg):
        '''
        如果不是訊息，回傳 False。
        若是，回傳 True 並發送 msg 訊息。
        
        getUpdates
            botHandler.getUpdates() 得到的內容

        msg
            欲傳送訊息
        '''
        if len(getUpdates) != 0:
            if 'message' in getUpdates[-1]:
                print("[INFO] 發送 msg！")
                requests.get(
                    self.url + "sendMessage",
                    params={
                        'chat_id': getUpdates[-1]['message']['chat']['id'],
                        'text': msg
                        }
                )
                print("[INFO] 發送完成")
                return True
            else:
                print("[INFO] 不是訊息！")
        return False
    
    def sendPhoto(self, getUpdates, url):
        '''
        如果不是訊息，回傳 False。
        若是，回傳 True 並發送 url 圖片。
        
        getUpdates
            botHandler.getUpdates() 得到的內容

        url
            欲傳送圖片之網址
        '''
        if len(getUpdates) != 0:
            if 'message' in getUpdates[-1]:
                print("[INFO] 發送 url 圖片！")
                requests.get(
                    self.url + "sendPhoto",
                    params={
                        'chat_id': getUpdates[-1]['message']['chat']['id'],
                        'photo': url
                        }
                )
                print("[INFO] 發送完成")
                return True
            else:
                print("[INFO] 不是訊息！")
        return False

    def sendDocument(self, getUpdates, doc):
        '''
        如果不是訊息，回傳 False。
        若是，回傳 True 並發送 doc 文件。
        
        getUpdates
            botHandler.getUpdates() 得到的內容

        doc
            欲傳送文件之網址
        '''
        if len(getUpdates) != 0:
            if 'message' in getUpdates[-1]:
                print("[INFO] 發送 doc 文件！")
                requests.get(
                    self.url + "sendDocument",
                    params={
                        'chat_id': getUpdates[-1]['message']['chat']['id'],
                        'document': doc
                        }
                )
                print("[INFO] 發送完成")
                return True
            else:
                print("[INFO] 不是訊息！")
        return False

# 隨機產生同個文字的不同長度
# 所需函式：random
def randomText(text = "咕", ranCount = range(1, 25)):
    '''
    隨機產生同文字不同長度的字串

    text
        要產生的文字
    
    range
        產生文字數範圍。
    '''
    return text * random.choice(ranCount)