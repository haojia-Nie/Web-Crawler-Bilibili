# Bilibili_scrapying_basic
A basic and straight-forward scraping for bilibili, good for beginners


The website used could be find by inspect the source code of the website https://space.bilibili.com, 
and we could find the user information in the network section under XHR, the data is provided in the 
form of a dictionary, and we just analyse it. 


Note: only can be used for you to scrap a small amout of data, anything more than that require multiprocessing
      and using headers and different proxies 
      
A small demo of the data I got:

![Screen Shot 2019-08-12 at 12 22 52 PM](https://user-images.githubusercontent.com/52882728/62845662-74457400-bcfc-11e9-82e3-6dadb0e339f8.png)


Also, I use matplotlib and pandas for data visualisation

The result is kind of interesting: 

GENDER

Among the 1000 data, 
the ratio of male : female = 2.2 : 1




LEVEl & VIP:

most of the people are in below level 1, 
the higher the level, the higher the ratio of vip. 

![level_users](https://user-images.githubusercontent.com/52882728/62911815-47ef2d80-bdb8-11e9-91c9-0fae8fbf23ee.png)



FOLLOWER:

The 3 most popular user:
user id: 2000621 name: 叫我三木  home: https://space.bilibili.com/2000621  follower: 11168
user_id: 2000587 name: 馥夜闻笛  home: https://space.bilibili.com/2000587  follower: 6759
user id: 2000133 name: 津岛纸箱  hoem: https://space.bilibili.com/2000133  follower: 5066











