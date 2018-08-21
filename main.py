#!/usr/bin/env python3
'''
咕咕機器人 (實做)

請在 config.py 設定好 token 再啟動，
並確保已經在 @BotFather 關閉了 Privary 設定：

/setprivary  -> 設定 Disable

接著私訊您的機器人，或者是放到您的群組即可。
'''

import config
from libs import botHandler, randomText
import time, sys, random

# 相關參數
infomsg = """[INFO] -----
[INFO] 發送者：{0:s}
[INFO] 訊息：{1:s}
[INFO] 時間：{2:s} (電腦時區)
[INFO] -----"""

helptxt = """《咕咕機器人教學》
只要訊息包含「g」或「咕」，皆會觸發機器人：

[其他用法]
「/start」 (如果訊息是 /start)
「/help」 (觸發本說明)"""

errtxt = """[ERR] 接收訊息時發生問題，正在重試…
[ERR] 若您持續碰到這個問題，請發送一個 issue 並附加以下文字：
[ERR] {}
[ERR] 也建議先檢查自己的 token 是否設定錯誤。"""

# 設定 botHandler
bot = botHandler(config.token)
botInf = bot.getMe()

# 若未設定 token 憑證或 bot 使用者名稱
if config.token == "":
    raise Exception("[ERR] 您未設定 Token。")
if 'result' not in botInf:
    raise Exception("[ERR] 您機器人的 Token 設定無效。")

botUsername = "@" + botInf['result']['username']
print(f"[INFO] 機器人 {botUsername} 成功開啟。")
print(f"[INFO] 機器人資訊：{botInf}")
print("[INFO] 開始接收訊息")

while True:
    try:
        updates = bot.getUpdates() # 抓取機器人收到的更新

        if updates == False: # 若沒有更新
            continue
        if 'message' in updates[-1] and 'text' in updates[-1]['message']: # 如果接收到的訊息是文字訊息
            msg = updates[-1]['message']['text']
        else:
            continue
        
        if 'username' not in updates[-1]['message']['from']:
            updates[-1]['message']['from']['username'] = "未知" # 如果傳送訊息之使用者沒有設定 ID
        
        # 訊息記錄
        print(infomsg.format(
            "@" + updates[-1]['message']['from']['username'],
            msg,
            time.strftime("%Y 年 %m 月 %d 日 %p %I 時 %M 分 %S 秒", time.localtime(updates[-1]['message']['date']))
        ))

        # 指令列表
        if msg == "/help" or msg == f"/help{botUsername}":
            bot.sendMessage(updates, helptxt) # 傳送說明
            continue
        
        choicePhotoOrTxt = random.choice(range(0, 3)) # 抽籤，決定要傳送的訊息
        # 若訊息包含 g、咕 或者是訊息為「/start」
        if msg.find('g') != -1 or msg.find('咕') != -1 or msg == "/start" or msg == f"/start{botUsername}":
            # 傳送隨機長度的咕
            if choicePhotoOrTxt == 0:
                bot.sendMessage(updates, randomText())
            # 傳送 GIF 1
            elif choicePhotoOrTxt == 1:
                bot.sendDocument(updates, "https://i.imgur.com/begraED.gif")
            # 傳送 GIF 2
            else:
                bot.sendDocument(updates, "https://i.imgur.com/T0LRYrG.gif")
            continue
    
    except KeyboardInterrupt:
        raise sys.exc_info()[1] # 如果使用者輸入 Ctrl-C
    except:
        print(errtxt.format(sys.exc_info())) # 傳送 Error 訊息