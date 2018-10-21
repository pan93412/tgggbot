'''
咕咕機器人所使用的各項函式。

建議不要修改此處的任何程式碼，
若修改很有可能發生問題，除非您
十分清楚目的。

若要用於您的程式，請標註作者 pan93412
和此 GitHub 庫網址。
'''
from urllib import request, parse
import random
import json
import strings as s

# 注意！此與 botHandler 共同運作！
def _requester(url):
  '''發送 GET 請求至 url，並回傳一個 File 類別。'''
  therequest = request.Request(url)
  response = request.urlopen(therequest)
  return response

# 機器人函式
class botHandler:
  '''
  bot 機器人處理類別
  
  bot_token: 機器人的 Token (從 @BotFather 申請)
  '''
  
  def __init__(self, bot_token):
    '''請參閱父函式說明。'''
    self.botAPI = "http://api.telegram.org/bot{}/".format(bot_token)

  def getMe(self):
    '''取得 bot 的資訊。回傳一組 Dict 類別，包含機器人資訊。'''
    getMeAPI = self.botAPI + "getMe"
    responseData = _requester(getMeAPI).read()
    return json.loads(responseData) # 回傳解析出的 Bot 資訊字典
  
  def getUpdates(self, received=True):
    '''
    取得 bot 抓取到的訊息。
    
    received: 是否將已接收到的訊息在遠端伺服器標記為
              「已接受」，以在下次 getUpdates() 時
              不再出現以前接收過的訊息。
              
              預設值：True
              可選值：True / False
              
    回傳：     如果沒有訊息，則回傳 None。如果有訊息則回傳
              接收到訊息的 JSON 內容。
    '''
    getUpdatesAPI = self.botAPI + "getUpdates"
    
    latestUpdatesRaw = _requester(getUpdatesAPI)
    latestUpdates = json.loads(latestUpdatesRaw.read())["result"]
    latestUpdatesRaw.close()
    
    if len(latestUpdates) == 0:
      return None
    else:
      print(s.receivedMessage.format(latestUpdates[-1]["message"]["from"].get("username", "unknown")))
      if received:
        theParam = {"offset": latestUpdates[-1]["update_id"] + 1}
        _requester(getUpdatesAPI + "?" + parse.urlencode(theParam))
        print(s.receivedDone)
      return latestUpdates
        
  def sendMessage(self, userID, msg):
    '''
    傳送 msg 訊息到 userID。

    userID: 傳送訊息到 ID 為 userID 的使用者、群組
            或者是頻道。
            
    msg:    訊息
    
    回傳：   僅回傳 None。
    '''
    
    sendMessageAPI = self.botAPI + "sendMessage"
    params = {"chat_id": userID, "text": msg}
    
    print(s.sendMsgRequested)
    _requester(sendMessageAPI + "?" + parse.urlencode(params))
    return None

  def sendDocument(self, userID, doc):
    '''
    傳送 doc 檔案到 userID。

    userID: 傳送訊息到 ID 為 userID 的使用者、群組
            或者是頻道。
            
    doc:    檔案連結。
    
    回傳：   僅回傳 None。
    '''
    
    sendMessageAPI = self.botAPI + "sendDocument"
    params = {"chat_id": userID, "document": doc}
    
    print(s.sendMsgRequested)
    _requester(sendMessageAPI + "?" + parse.urlencode(params))
    
    return None

def randomText(text, ranCount = range(1, 26)):
    '''
    隨機產生長度隨機產生的 text。

    text
        要產生的文字
    
    range
        產生文字數範圍。預設範圍為 1-25。
    '''
    return text * random.choice(ranCount)
