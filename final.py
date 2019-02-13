import sys
import threading 
from bs4 import BeautifulSoup as bs
import re
import jieba.posseg as pseg
import urllib.request

headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",

}

t1='http://www.baidu.com/s?wd=李聪媛&pn=0'
t2='http://www.baidu.com/s?wd=李聪媛&pn=10'
t3='http://www.baidu.com/s?wd=李聪媛&pn=20'
t4='http://www.baidu.com/s?wd=李聪媛&pn=30'
t5='http://www.baidu.com/s?wd=李聪媛&pn=40'
t6='http://www.baidu.com/s?wd=李聪媛&pn=50'
t8='http://www.baidu.com/s?wd=李聪媛&pn=70'
t9='http://www.baidu.com/s?wd=李聪媛&pn=80'
t10='http://www.baidu.com/s?wd=李聪媛&pn=90'
t11='http://www.baidu.com/s?wd=李聪媛&pn=90'


urllist=[#'https://baike.baidu.com/item/旅游经济学/19711782',
         #'http://search.dangdang.com/author/%C0%EE%B4%CF%E6%C2_1',
         #'http://book.jd.com/writer/李聪媛_1.html',
         #'http://book.kongfz.com/13553/617459779/',
         #'http://book.kongfz.com/22076/542484083/',
         #'https://bbs.pinggu.org/thread-5125552-1-1.html',
         #'http://book.kongfz.com/21467/772341865/',

         #'http://product.dangdang.com/23794451.html',
        'http://www.wanfangdata.com.cn/details/detail.do?_type=degree&id=Y622089',
        'http://www.jarhu.com/book-1502622.html',
        'http://zhuanti.hebnews.cn/2010gk/2010-07/29/content_350615.htm',
        'http://www.cnki.com.cn/Article/CJFDTotal-PPTT201508177.htm',
         #'http://item.jd.com/11795102.html',
         #'http://www.jarhu.com/book-1502622.html',
         #'http://book.kongfz.com/267661/1106457014/',
         #'https://www.amazon.cn/图书/dp/B00BLILNB0'
         ]
content=[]
i=[]

def get_page(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12918.400')
    response=urllib.request.urlopen(url)
    html=response.read().decode('utf-8')
    print(html[0:1000])
    return html

def get_url(url):


        r = requests.get(url = url,headers = headers,allow_redirects=False)
        soup = bs(r.content,"html.parser")
        urls = soup.find_all(name='a',attrs={'href':re.compile(('.'))})
        #for i in urls:
            #print (i)

        for i in urls:
                if ('www.baidu.com/link?url=' in i['href']):
                        a = requests.get(url = i['href'],headers = headers)
                        if 'image' not in a.url:
                                if(a.url not in urllist):
                                        urllist.append(a.url)
                                        print(a.url)

                

#get_url(t1)
#get_url(t2)
#get_url(t3)
#get_url(t4)
#get_url(t5)
#get_url(t6)

#get_url(t8)
#get_url(t9)
#get_url(t10)
#get_url(t11)

def check(k,c):
    if(k.find('李聪媛')!=-1):
        
        m=k.find('李聪媛')
        v2=k[m-70:m+70]
        c.append(v2)
        k=k[m+4:]
        check(k,c)
        

for each in urllist:
        x=get_page(each)
        check(x,content)
for each in content:
        words = pseg.cut(each)
        for word,flag in words:
                if(flag=='nt'or flag=='ns'):
                    if(word not in i):
                        i.append(word)
                        print('李聪源 '+word)
        
                
        

