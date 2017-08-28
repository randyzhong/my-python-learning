# -*- coding: utf-8 -*-
# http://wlkt.ustc.edu.cn/ (USTC CERNET IP Only)
# Public course only
# If online course is set to private or restricted for Xiaonei only, you have to run this downloader from USTC CERNET IP, or you'll not get the real video source URL.
# Reference: https://www.zhihu.com/question/20799742/answer/99491808

import requests
import urllib
from bs4 import BeautifulSoup

s = requests.Session() 
link = "http://wlkt.ustc.edu.cn/video/detail_3752_0.htm" # This is a public video
req = s.get(link)
html = req.content
soup = BeautifulSoup(html, "html.parser")
videourl1 = soup.find(id="videourl1")['value']
htopicid = soup.find(id="htopicid")['value']
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
           'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
           'X-Requested-With': 'XMLHttpRequest',
           'Host': 'wlkt.ustc.edu.cn',
           'Origin': 'http://wlkt.ustc.edu.cn',
           'Referer': 'http://wlkt.ustc.edu.cn/video/detail_3752_0.htm'}
payload = urllib.urlencode({'videourl1': videourl1,'hid_topicid': htopicid})
url = requests.post("http://wlkt.ustc.edu.cn/ajaxprocess.php?menu=getvideourl",data=payload, headers=header)
print ("The real video URL is： http://wlkt.ustc.edu.cn/mp4.php?file=" + url.content[14:])
