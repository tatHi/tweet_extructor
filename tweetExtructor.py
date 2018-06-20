from requests_oauthlib import OAuth1Session
import json
import itertools
import pickle
from time import sleep
CK = 'xxx' # Consumer Key
CS = 'xxx' # Consumer Secret
AT = 'xxx' # Access Token
AS = 'xxx' # Accesss Token Secert
 
session = OAuth1Session(CK, CS, AT, AS)
 
url = 'https://api.twitter.com/1.1/statuses/lookup.json'

def getTweets(tweetIds):
    tweetIds = ','.join(list(map(str,tweetIds)))
    res = session.get(url, params = {'id':tweetIds})
     
    if res.status_code != 200:
        print ("Twitter API Error: %d" % res.status_code)
        sys.exit(1)
     
    resText = json.loads(res.text)
    data = {rt['id']:rt['text'] for rt in resText}
    return data

def extruct():
    anno = [list(map(int, line.strip().split(','))) for line in open('tweets_open.csv')]
    alldata = []

    for i,batch in enumerate(itertools.zip_longest(*[iter(anno)]*100)):
        print('%d/%d'%(i+1,len(anno)//100))
        batch = [b for b in batch if b is not None]
        tweets = getTweets([line[2] for line in batch])

        for line in batch:
            data = {'id':line[0],
                    'topic':line[1],
                    'status':line[2],
                    'label':line[3:],
                    'text':tweets[line[2]] if line[2] in tweets else ''
                   }
            alldata.append(data)

        # sleep
        sleep(1)
    pickle.dump(alldata, open('twitterJSA_data.pickle','wb'))
    json.dump(alldata, open('twitterJSA_data.json','w'))

extruct()
