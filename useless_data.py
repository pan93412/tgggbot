'''
這裡放置一些已經廢棄的程式碼，如果您有需要您可以
從這個 useless_data 倉庫取走可能對你而言有用的程
式碼。

您可以標註借用此處代碼，或者不標註。但若您標註了
，我將因此而開心。

當你決定開始取用此處的程式碼時，本資料庫不擔保程式
碼皆可使用，使用前請測試，而非盲目直接套用（除非你
只是打算用來增加程式碼行數，而不是實際拿來使用）。
'''

# 預計移除
"""
    def answerInlineQuery(self, getUpdates, results):
        '''
        如果不是 Inline 訊息，回傳 False。
        若是，回傳 True 並發送 results 陣列。
        
        getUpdates
            botHandler.getUpdates() 得到的內容

        results
            InlineQueryResult 的陣列，請參閱 TG Bot API
        '''
        if len(getUpdates) != 0:
            if 'inline_query' in getUpdates[-1]:
                print("[INFO] 發送 results！")
                requests.get(
                    self.url + "answerInlineQuery",
                    params={
                        'inline_query_id': getUpdates[-1]['inline_query']['id'],
                        'results': results
                        }
                )
                return True
            else:
                print("[INFO] 不是 Inline 訊息！")
        return False
""" 

# 預計移除
'''
# 變數
aiq_InlineQueryResult = {
    'type': 'InputTextMessageContent',
    'id': 'gogo',
    'title': '咕咕咕',
    'input_message_content': {
        'message_text': randomText()
    }
}
'''
