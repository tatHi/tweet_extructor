Twitter日本語評判分析データセットのためのツイートダウンローダ  

http://bigdata.naist.jp/~ysuzuki/data/twitter/  
上記サイトにて配布されているtweets_open.csvファイルを用いてツイッターからツイートを取得するスクリプトです．  

twitterAPIを用いるため，適当なアプリをtwitter appに登録し，
Consumer Key, Consumer Secret, Access Token, Accesss Token Secertを取得してください．
取得したキーはtweetExtructor.py内に書き込んでください．  

tweetExtructor.pyと同じ場所にcsvファイルをおいて，以下を実行してください．  
アノテーション情報と，対応するツイートのテキストがjson形式とpickle形式で吐き出されます．  
```
$ python tweetExtructor.py
```

twitterにてユーザが投稿をすでに削除している場合，あるいは非公開アカウントにしている場合はテキストが得られないことがあります．
2018/06/20現在で，アノテーション済み534,962件のうち352,554件がアクセス可能です．
