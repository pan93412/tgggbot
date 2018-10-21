'''
咕咕機器人所使用的各項設定值，
此處的設定通常可以放心修改，除
了標記「危險」或「注意」的值。
'''

# 機器人設定
token = "" # 機器人的 Token  (必須設定！)

detectStart = True  # 是否偵測 /start
detectHelp  = True  # 是否偵測 /help
detectText = ['咕', 'g'] # 用分號隔開。要偵測的文字

sendTxt = "default" # 預設值為 "default"。若要自訂文字，請將 default 改成
                    # 您想要的文字。
randTxt = "咕"      # 欲隨機產生的字元。
                    
# 要傳送的圖片，共兩組。若要自訂圖片，請自行將連結改成您想要圖片的連結。
sendPhoto1 = "https://i.imgur.com/begraED.gif"
sendPhoto2 = "https://i.imgur.com/T0LRYrG.gif"


