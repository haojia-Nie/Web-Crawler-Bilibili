# Bilibili_scrapying_basic
The most basic data scraping for bilibili


The website used could be find by inspect the source code of the website https://space.bilibili.com, 
and we could find the user information in the network section under XHR, the data is provided in the 
form of a dictionary, and we just analyse it. 


The entire scrapying is straight forward and the data is stored in a data frame, as at the time I had
no idea about sql at the time I wrote it. 


Note: only can be used for you to scrap a small amout of data, anything more than that require multiprocessing
      and using headers and different proxies 
      
Here is a small demo of the data I got

![Screen Shot 2019-08-12 at 12 22 52 PM](https://user-images.githubusercontent.com/52882728/62845662-74457400-bcfc-11e9-82e3-6dadb0e339f8.png)


Also, I did a few data visualisation just to practice the use of matplotlib and pandas






