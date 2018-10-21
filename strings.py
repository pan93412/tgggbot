'''
咕咕機器人所使用的字串。
'''

LANG = "zh_TW.UTF-8" # 定義語言。雖此變數沒有實質作用，但
                     # 仍建議定義

'''[優先！] 機器人字串'''
# 機器人字串: 使用者輸入 /help 時出現之文字
helpTxt = """[咕咕機器人 使用說明]
/help: 顯示說明
/((咕|g)+|/start(.+))/: 發送不定長度的咕或 g。"""

'''main.py 字串'''
# main.py: 空 username 的替代字串
noUsername = "未知"

# main.py: 時間格式化
timeFormat = "%Y年 %m月 %d日 %p %I時 %M分 %S秒" # ex. 2018年 10月 21日 下午 7時 07分 35秒

# main.py: while 迴圈: 當接收到訊息時顯示之文字。
# {0:s}: str 型態。傳送者。
# {1:s}: str 型態。傳送時間。
# {2:s}: str 型態。傳送訊息。
receivedMsgInfo = """I: 接收到訊息！
   傳送用戶： @{0:s}
   傳送時間：  {1:s}
   傳送訊息：  {2:s}
"""

# main.py: while 迴圈: 發生錯誤時。
# {}: 錯誤資訊。
mainHappenErr = """W: 傳送訊息或接收訊息時發生錯誤。

   如果此錯誤沒有再次發生，您能直接忽略。
   如果此錯誤仍再次發生，請回報以下錯誤訊息至開發者們：

   {}
"""

# main.py: 初始訊息: 當機器人成功初始化時
# {}: libs.py 中 getMe() 回傳資訊。
initFinished = """I: 您的機器人成功初始化！

   機器人資訊：{}

   開始接收訊息！"""
# main.py: 錯誤訊息: 如果未設定 Token
tokenNotSet = "E: 您未設定 Token。"

# main.py: 錯誤訊息: 如果 Token 設定無效
tokenInvaild = "E: Token 無效。"

'''libs.py 字串'''
# libs.py: getUpdates(): 當接收到訊息時
# {0:s}: str 型態。發送者。
receivedMessage = "I: 接收到來自 @{0:s} 的訊息！"

# libs.py: getUpdates(): 當完成 received
# (接收後向遠端發送已讀訊息) 功能後顯示之文字。
receivedDone = "I: 成功將遠端訊息標為已讀。"

# libs.py: sendMessage(): 當發出傳送訊息請求之後顯示之文字。
sendMsgRequested = "I: 發送訊息請求完成。"



