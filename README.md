# Twitter日本語評判分析データセットのためのツイートダウンローダ  

Twitter日本語評判分析データセットに含まれるツイートデータをダウンロードするためのスクリプトです．

## 使い方
### データセットCSVのダウンロード
http://bigdata.naist.jp/~ysuzuki/data/twitter/  
上記サイトにて配布されているtweets_open.csvファイルをダウンロード．

### TwitterAPPの登録
twitterAPIを用いるため，適当なアプリをtwitter appに登録し，
Consumer Key, Consumer Secret, Access Token, Accesss Token Secertを取得してください．  
https://apps.twitter.com/  

取得したキーはtweetExtructor.py内の以下のxxxに書き込んでください．  
```
CK = 'xxx' # Consumer Key
CS = 'xxx' # Consumer Secret
AT = 'xxx' # Access Token
AS = 'xxx' # Accesss Token Secert
```
  

### 実行
tweetExtructor.pyと同じ場所にcsvファイルをおいて，以下を実行してください．  
アノテーション情報と，対応するツイートのテキストがjson形式とpickle形式で吐き出されます．  
```
$ python tweetExtructor.py
```

あるいは，--csvPathの引数でcsvファイルの場所を指定することもできます．  

```
$ python tweetExtructor.py --csvPath hoge/tweet_open.csv
```

API制限の関係で，1秒あたりに100ツイートのみの取得となります．  
データセットに含まれるツイート数から単純に計算して，全てのデータをダウンロードするのに2時間弱必要になります．  

### 注意
twitterにてユーザが投稿をすでに削除している場合，あるいは非公開アカウントにしている場合はテキストが得られないことがあります．  
2018/06/20現在で，アノテーション済み534,962件のうち352,554件がアクセス可能です．
