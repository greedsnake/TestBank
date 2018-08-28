# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 00:17:32 2018

@author: linzino
"""
import requests #引入函式庫
from bs4 import BeautifulSoup
import re
import json
import feedparser


def udn_news():
    '''
    抓最新前三篇新聞
    
    回傳是一個dict
    '''
    rss_url = 'https://udn.com/rssfeed/news/2/6644/7239?ch=news'
 
    # 抓取資料
    rss = feedparser.parse(rss_url)
    
    cards = []    
    for index in range(0,3):
        # 抓文章標題
        title = rss['entries'][index]['title']
        # 抓文章連結
        link = rss['entries'][index]['link']
        # 處理摘要格式
        summary =  rss['entries'][index]['summary']
        
        if 'img' in summary:
            soup = BeautifulSoup(summary, 'html.parser')
            p_list = soup.find_all('p')
            # 抓文章摘要 限制只有60個字
            text = p_list[1].getText()[:50]
            # 抓文章圖片
            image = p_list[0].img['src']
        else:
            # 沒有圖片
            text = summary[:50]
            image = 'https://i.imgur.com/vkqbLnz.png'
        
        card = {'title':title,
                'link':link,
                'summary': text,
                'img':image
                }
        cards.append(card)
        
    return cards


def google():
    '''
    抓到最新google map資料
    '''
    pretext = ')]}\''
    
    # 爬下com南港分行
    url = 'https://www.google.com.tw/maps/preview/reviews?authuser=0&hl=zh-TW&gl=tw&pb=!1s0x3442ab5ed8270bf5%3A0xca5639af83a88adc!2i0!3i10!4e3!7m4!2b1!3b1!5b1!6b1'
    resp = requests.get(url)
    text = resp.text.replace(pretext,'')
    soup = json.loads(text)
    
    # 抓第一篇
    first = soup[0][0]
    # 整理資料 
    username = first[0][1]
    time = first[1]
    mesg = first[3]
    star = first[4]
    
    # 爬下com東湖分行2
    url2 = 'https://www.google.com.tw/maps/preview/reviews?authuser=0&hl=zh-TW&gl=tw&pb=!1s0x3442acbde079d169%3A0x8810bd0a963d1727!2i0!3i10!4e3!7m4!2b1!3b1!5b1!6b1'
    resp2 = requests.get(url2)
    text2= resp2.text.replace(pretext,'')
    soup2 = json.loads(text2)
    
    # 抓第一篇
    first2 = soup2[0][0]
    # 整理資料 
    username2 = first2[0][1]
    time2 = first2[1]
    mesg2 = first2[3]
    star2 = first2[4]
	
	# 爬下com3
    url3 = ''
    resp3 = requests.get(url3)
    text3= resp3.text.replace(pretext,'')
    soup3 = json.loads(text3)
    
    # 抓第一篇
    first3 = soup3[0][0]
    # 整理資料 
    username3 = first3[0][1]
    time3 = first3[1]
    mesg3 = first3[3]
    star3 = first3[4]
	
	# 爬下com4
    url4 = ''
    resp4 = requests.get(url4)
    text4= resp4.text.replace(pretext,'')
    soup4 = json.loads(text4)
    
    # 抓第一篇
    first4 = soup4[0][0]
    # 整理資料 
    username4 = first4[0][1]
    time4 = first4[1]
    mesg4 = first4[3]
    star4 = first4[4]
	
	# 爬下com5
    url5 = ''
    resp5 = requests.get(url5)
    text5= resp5.text.replace(pretext,'')
    soup5 = json.loads(text5)
    
    # 抓第一篇
    first5 = soup5[0][0]
    # 整理資料 
    username5 = first5[0][1]
    time5 = first5[1]
    mesg5 = first5[3]
    star5 = first5[4]
	
	# 爬下com6
    url6 = ''
    resp6 = requests.get(url6)
    text6= resp6.text.replace(pretext,'')
    soup6 = json.loads(text6)
    
    # 抓第一篇
    first6 = soup6[0][0]
    # 整理資料 
    username6 = first6[0][1]
    time6 = first6[1]
    mesg6 = first6[3]
    star6 = first6[4]
	
	# 爬下com7
    url7 = ''
    resp7 = requests.get(url7)
    text7= resp7.text.replace(pretext,'')
    soup7 = json.loads(text7)
    
    # 抓第一篇
    first7 = soup7[0][0]
    # 整理資料 
    username7 = first7[0][1]
    time7 = first7[1]
    mesg7 = first7[3]
    star7 = first7[4]
	
	# 爬下com8
    url8 = ''
    resp8 = requests.get(url8)
    text8= resp8.text.replace(pretext,'')
    soup8 = json.loads(text8)
    
    # 抓第一篇
    first8 = soup8[0][0]
    # 整理資料 
    username8 = first8[0][1]
    time8 = first8[1]
    mesg8 = first8[3]
    star8 = first8[4]
	
	# 爬下com9
    url9 = ''
    resp9 = requests.get(url9)
    text9= resp9.text.replace(pretext,'')
    soup9 = json.loads(text9)
    
    # 抓第一篇
    first9 = soup9[0][0]
    # 整理資料 
    username9 = first9[0][1]
    time9 = first9[1]
    mesg9 = first9[3]
    star9 = first9[4]
	
	# 爬下com10
    url10 = ''
    resp10 = requests.get(url10)
    text10= resp10.text.replace(pretext,'')
    soup10 = json.loads(text10)
    
    # 抓第一篇
    first10 = soup10[0][0]
    # 整理資料 
    username10 = first10[0][1]
    time10 = first10[1]
    mesg10 = first10[3]
    star10 = first10[4]
	
	# 爬下com11
    url11 = ''
    resp11 = requests.get(url11)
    text11= resp11.text.replace(pretext,'')
    soup11 = json.loads(text11)
    
    # 抓第一篇
    first11 = soup11[0][0]
    # 整理資料 
    username11 = first11[0][1]
    time11 = first11[1]
    mesg11 = first11[3]
    star11 = first11[4]
	
	# 爬下com12
    url12 = ''
    resp12 = requests.get(url12)
    text12= resp12.text.replace(pretext,'')
    soup12 = json.loads(text12)
    
    # 抓第一篇
    first12 = soup12[0][0]
    # 整理資料 
    username12 = first12[0][1]
    time12 = first12[1]
    mesg12 = first12[3]
    star12 = first12[4]
	
	# 爬下com13
    url13 = ''
    resp13 = requests.get(url13)
    text13= resp13.text.replace(pretext,'')
    soup13 = json.loads(text13)
    
    # 抓第一篇
    first13 = soup13[0][0]
    # 整理資料 
    username13 = first13[0][1]
    time13 = first13[1]
    mesg13 = first13[3]
    star13 = first13[4]
	
	# 爬下com14
    url14 = ''
    resp14 = requests.get(url14)
    text14= resp14.text.replace(pretext,'')
    soup14 = json.loads(text14)
    
    # 抓第一篇
    first14 = soup14[0][0]
    # 整理資料 
    username14 = first14[0][1]
    time14 = first14[1]
    mesg14 = first14[3]
    star14 = first14[4]
    
    string = '%s \n %s \n於 %s 將您評為 %s顆星 \n留言：%s \n %s \n %s \n於 %s 將您評為 %s顆星 \n留言：%s '% ('南港分行',username,time,star,mesg,'東湖分行',username2,time2,star2,mesg2,'新湖分行',username3,time3,star3,mesg3,'營業部',username4,time4,star4,mesg4,'建國分行',username5,time5,star5,mesg5,'文德分行',username6,time6,star6,mesg6,'瑞湖分行',username7,time7,star7,mesg7,'復興分行',username8,time8,star8,mesg8,'內湖分行',username9,time9,star9,mesg9,'永春分行',username10,time10,star10,mesg10,'北投分行',username11,time11,star11,mesg11,'石牌分行',username12,time12,star12,mesg12,'忠誠分行',username13,time13,star13,mesg13,'蘭雅分行',username14,time14,star14,mesg14,'天母分行',username15,time15,star15,mesg15,'建成分行',username16,time16,star16,mesg16,'中山分行',username17,time17,star17,mesg17,'西門分行',username18,time18,star18,mesg18,'士林分行',username19,time19,star19,mesg19,'大直分行',username20,time20,star20,mesg20,'景美分行',username21,time21,star21,mesg21,'敦化分行',username22,time22,star22,mesg22,'和平分行',username23,time23,star23,mesg23,'文昌分行',username24,time24,star24,mesg24,'館前分行',username25,time25,star25,mesg25,'安和分行',username26,time26,star26,mesg26,'古亭分行',username27,time27,star27,mesg27,'大同分行',username28,time28,star28,mesg28,'南門分行',username29,time29,star29,mesg29,'萬華分行',username30,time30,star30,mesg30,'中崙分行',username31,time31,star31,mesg31,'南內湖分行',username32,time32,star32,mesg32,'仁愛分行',username33,time33,star33,mesg33,'城東分行',username34,time34,star34,mesg34,'西松分行',username35,time35,star35,mesg35,'忠孝分行',username36,time36,star36,mesg36,'信義分行',username37,time37,star37,mesg37,'光復分行',username38,time38,star38,mesg38,'中正分行',username39,time39,star39,mesg39,'八德分行',username40,time40,star40,mesg40,'臨沂分行',username41,time41,star41,mesg41,'信安分行',username42,time42,star42,mesg42,'慶城分行',username43,time43,star43,mesg43,'台北分行',username44,time44,star44,mesg44,'大安分行',username45,time45,star45,mesg45,'東門分行',username46,time46,star46,mesg46,'新生分行',username47,time47,star47,mesg47,'敦南分行',username48,time48,star48,mesg48,'世貿分行',username49,time49,star49,mesg49,'文山分行',username50,time50,star50,mesg50,'華山分行',username51,time51,star51,mesg51,'民生分行',username52,time52,star52,mesg52,'光華分行',username53,time53,star53,mesg53,'永平分行',username54,time54,star54,mesg54,'南京東路分行',username55,time55,star55,mesg55,'民權分行',username56,time56,star56,mesg56,'松江分行',username57,time57,star57,mesg57,'松山分行',username58,time58,star58,mesg58,'敦北分行',username59,time59,star59,mesg59,'三民分行',username60,time60,star60,mesg60,'宜蘭分行',username61,time61,star61,mesg61,'連城分行',username62,time62,star62,mesg62,'大坪林分行',username63,time63,star63,mesg63,'福和分行',username64,time64,star64,mesg64,'北新分行',username65,time65,star65,mesg65,'永貞分行',username66,time66,star66,mesg66,'永和分行',username67,time67,star67,mesg67,'新店分行',username68,time68,star68,mesg68,'中和分行',username69,time69,star69,mesg69,'雙和分行',username70,time70,star70,mesg70,'花蓮分行',username71,time71,star71,mesg71,'幸福分行',username72,time72,star72,mesg72,'淡水分行',username73,time73,star73,mesg73,'丹鳳分行',username74,time74,star74,mesg74,'林口分行',username75,time75,star75,mesg75,'新泰分行',username76,time76,star76,mesg76,'重新分行',username77,time77,star77,mesg77,'正義分行',username78,time78,star78,mesg78,'三重分行',username79,time79,star79,mesg79,'新莊分行',username80,time80,star80,mesg80,'北三重分行',username81,time81,star81,mesg81,'蘆洲分行',username82,time82,star82,mesg82,'二重分行',username83,time83,star83,mesg83,'新樹分行',username84,time84,star84,mesg84,'汐止分行',username85,time85,star85,mesg85,'基隆分行',username86,time86,star86,mesg86,'樹林分行',username87,time87,star87,mesg87,'板東分行',username88,time88,star88,mesg88,'學府分行',username89,time89,star89,mesg89,'新板分行',username90,time90,star90,mesg90,'板橋分行',username91,time91,star91,mesg91,'埔墘分行',username92,time92,star92,mesg92,'後埔分行',username93,time93,star93,mesg93,'土城分行',username94,time94,star94,mesg94,'華江分行',username95,time95,star95,mesg95,'大甲分行',username96,time96,star96,mesg96,'苗栗分行',username97,time97,star97,mesg97,'豐北分行',username98,time98,star98,mesg98,'西屯分行',username99,time99,star99,mesg99,'崇德分行',username100,time100,star100,mesg100,'沙鹿分行',username101,time101,star101,mesg101,'文華簡易型分行',username102,time102,star102,mesg102,'大雅分行',username103,time103,star103,mesg103,'豐原分行',username104,time104,star104,mesg104,'清水分行',username105,time105,star105,mesg105,'五權分行',username106,time106,star106,mesg106,'中港分行',username107,time107,star107,mesg107,'南投分行',username108,time108,star108,mesg108,'彰泰分行',username109,time109,star109,mesg109,'文心分行',username110,time110,star110,mesg110,'市政分行',username111,time111,star111,mesg111,'南屯分行',username112,time112,star112,mesg112,'秀水分行',username113,time113,star113,mesg113,'彰美分行',username114,time114,star114,mesg114,'大里分行',username115,time115,star115,mesg115,'員林分行',username116,time116,star116,mesg116,'彰化分行',username117,time117,star117,mesg117,'篤行分行',username118,time118,star118,mesg118,'中台中分行',username119,time119,star119,mesg119,'水湳分行',username120,time120,star120,mesg120,'東台中分行',username121,time121,star121,mesg121,'國光分行',username122,time122,star122,mesg122,'健行分行',username123,time123,star123,mesg123,'太平分行',username124,time124,star124,mesg124,'潭子分行',username125,time125,star125,mesg125,'台中分行',username126,time126,star126,mesg126,'西台中分行',username127,time127,star127,mesg127,'南崁分行',username128,time128,star128,mesg128,'桃興分行',username129,time129,star129,mesg129,'竹城分行',username130,time130,star130,mesg130,'北中壢分行',username131,time131,star131,mesg131,'香山分行',username132,time132,star132,mesg132,'竹北分行',username133,time133,star133,mesg133,'同德分行',username134,time134,star134,mesg134,'中壢分行',username135,time135,star135,mesg135,'桃園分行',username136,time136,star136,mesg136,'新竹分行',username137,time137,star137,mesg137,'北桃園分行',username138,time138,star138,mesg138,'竹科分行',username139,time139,star139,mesg139,'屏東分行',username140,time140,star140,mesg140,'台東分行',username141,time141,star141,mesg141,'左營分行',username142,time142,star142,mesg142,'岡山分行',username143,time143,star143,mesg143,'大昌分行',username144,time144,star144,mesg144,'四維分行',username145,time145,star145,mesg145,'明誠分行',username146,time146,star146,mesg146,'高雄分行',username147,time147,star147,mesg147,'東高雄分行',username148,time148,star148,mesg148,'鳳山分行',username149,time149,star149,mesg149,'苓雅分行',username150,time150,star150,mesg150,'前金分行',username151,time151,star151,mesg151,'新興分行',username152,time152,star152,mesg152,'前鎮分行',username153,time153,star153,mesg153,'南高雄分行',username154,time154,star154,mesg154,'斗六分行',username155,time155,star155,mesg155,'新營分行',username156,time156,star156,mesg156,'臨安分行',username157,time157,star157,mesg157,'嘉泰分行',username158,time158,star158,mesg158,'台南分行',username159,time159,star159,mesg159,'嘉義分行',username160,time160,star160,mesg160,'永康分行',username161,time161,star161,mesg161,'東台南分行',username162,time162,star162,mesg162,'成功分行',username163,time163,star163,mesg163,'善化分行',username164,time164,star164,mesg164)
    
    return string

def Dcard():
    '''
    在Dcard 上某個關鍵字最新的文章
    '''
    url = 'https://www.dcard.tw/search/general?query=%E5%9C%8B%E6%B3%B0%E4%B8%96%E8%8F%AF'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    atags = soup.find_all('a', re.compile('PostEntry_root_'))
    
    pre_url = 'https://www.dcard.tw/'
    
    string = '最新4篇Dcard貼文：\n'
    for  item in atags[:4]:
        string += pre_url+item['href']+'\n'
    
    return string
    
