import pandas as pd
import requests 
from urllib.request import urlopen
import json
import time


user_list = range(2000000, 2001001)
base_url1 = 'https://api.bilibili.com/x/space/acc/info?mid='
base_url2 = 'https://api.bilibili.com/x/relation/stat?vmid='


df = pd.DataFrame(index = user_list, 
                  columns = ['user_id', 'name', 'gender', 'following', 'follower', 'level', 'vip'])


t1 = time.time()
for i in user_list:
    id_url = str(i)
    
    url1 = base_url1 + id_url
    url2 = base_url2 + id_url
    
    info_html = urlopen(url1).read().decode('utf-8')
    basic_info = json.loads(info_html)
    
    
    
    other_html = urlopen(url2).read()
    other_info = json.loads(other_html)
    
    df.loc[i, 'user_id'] = basic_info['data']['mid']
    df.loc[i, 'name'] = basic_info['data']['name']
    df.loc[i, 'gender'] = basic_info['data']['sex']
    df.loc[i, 'vip'] = basic_info['data']['vip']['type']
    df.loc[i, 'level'] = basic_info['data']['level']
   

    df.loc[i, 'following'] = other_info['data']['following']
    df.loc[i, 'follower'] = other_info['data']['follower']
        
print('Total time: %.lf s' % (time.time() - t1, ))


df.to_csv('set_1')
df.to_csv('set_1')
