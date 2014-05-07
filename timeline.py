#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json


CK = 'IIYi64unS83JiVKdoGPCkxGn1'                        # Consumer Key
CS = 'VKBaYnXLTJKvnI8W3kQCfb7A22kYaGYGW3h7L3rwHaqkz4Wl8x'         # Consumer Secret
AT = '2444891454-yKFZn1Vimp9lfJkTCNsLtJEM2DqsPGQXGLZKLME' # Access Token
AS = 'i6OYZulcubb2npwKqGwaDayXTY2LyQePgQpY2fTlnnLIQ'         # Accesss Token Secert


# タイムライン取得用のURL
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

# とくにパラメータは無い
params = {}

# OAuth で GET
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.get(url, params = params)

if req.status_code == 200:
    # レスポンスはJSON形式なので parse する
    timeline = json.loads(req.text)
    # 各ツイートの本文を表示
    for tweet in timeline:
        print(tweet["text"])

else:
    # エラーの場合
    print ("Error: %d" % req.status_code)
