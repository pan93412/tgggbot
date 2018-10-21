#!/usr/bin/env python3
'''
咕咕機器人 (實做)

請在 config.py 設定好 token 再啟動，
並確保已經在 @BotFather 關閉了 Privary 設定：

/setprivary  -> 設定 Disable

接著私訊您的機器人，或者是放到您的群組即可。
'''

import config as c
import strings as s    # 匯入字串
from libs import botHandler, randomText
import time, sys, random

# 相關參數

# 設定 botHandler
bot = botHandler(c.token)
botInf = bot.getMe()["result"]

print(botInf)
# 若未設定 token 憑證或 bot 使用者名稱
if c.token == "":
  raise Exception(s.tokenNotSet)
if "username" not in botInf:
  raise Exception(s.tokenInvaild)

# 機器人初始完成顯示之訊息
print(s.initFinished.format(botInf))

# while 迴圈
while True:
  try:
    updates = bot.getUpdates() # 抓取機器人收到的更新
    if updates == None: # 若沒有更新
      continue
          
    if 'message' in updates[-1] and 'text' in updates[-1]['message']: # 如果接收到的訊息是文字訊息
      msg = updates[-1]['message']['text']
    else:
      continue
      
    thechat = updates[-1]['message']['chat']['id'] # 傳送者聊天室 ID
      
    if 'username' not in updates[-1]['message']['from']:
      updates[-1]['message']['from']['username'] = s.noUsername # 如果傳送訊息之使用者沒有設定 ID
      
    # 訊息記錄
    print(s.receivedMsgInfo.format(
      updates[-1]['message']['from']['username'],
      msg,
      time.strftime(s.timeFormat, time.localtime(updates[-1]['message']['date']))
    ))

    # 指令列表
    if c.detectHelp:
      if msg == "/help" or msg == "/help" + botInf["username"]:
        bot.sendMessage(thechat, helptxt) # 傳送說明
        continue
      
    choicePhotoOrTxt = random.choice(range(0, 3)) # 抽籤決定要傳送的訊息
       
    # 若訊息包含 c.detectText 中的文字
    for i in c.detectText:
      if msg.find(i) != -1:
        if choicePhotoOrTxt == 0:
          bot.sendMessage(thechat, randomText(c.randTxt))
        elif choicePhotoOrTxt == 1:
          bot.sendDocument(thechat, c.sendPhoto1)
        else:
          bot.sendDocument(thechat, c.sendPhoto2)
        break
    
    if c.detectStart:
      if msg == "/start" or msg == "/start@" + botInf["username"]:
        if msg.find(i) != -1:
          if choicePhotoOrTxt == 0:
            bot.sendMessage(thechat, randomText(c.randTxt))
          elif choicePhotoOrTxt == 1:
            bot.sendDocument(thechat, c.sendPhoto1)
          else:
            bot.sendDocument(thechat, c.sendPhoto2)
 
  except KeyboardInterrupt:
    raise sys.exc_info()[1] # 如果使用者輸入 Ctrl-C
  except:
    print(s.mainHappenErr.format(sys.exc_info())) # 顯示錯誤訊息
