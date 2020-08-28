#Proxy list graper
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import time
print("""


🅿🆁🅾🆇🆈 🅶🆁🅰🅱                                        

----------------------------
{Auther => Ahmed alassaf}
https://www.youtube.com/channel/UCFc4g1cY6KFBN2ojYyc8tLA/videos
https://github.com/shadihh9
+-----------+
the proxy file will be saved successfully in the same directory
+-----------+
""")
try:
    time.sleep(7)# sleep for 7 (s)
    url = "https://free-proxy-list.net/" # the source
    req = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    open_url = urllib.request.urlopen(req)
    data = open_url.read()
    soup = BeautifulSoup(data,'html.parser')
    proxy_file = open("Proxyip.txt","w+")
    proxy_data = soup.find_all('tr')
    Pr_list = []
    for i in proxy_data:
        Pr = "http://{0}:{1}".format(BeautifulSoup(str(list(i)[0]),'html.parser').text,BeautifulSoup(str(list(i)[1]),'html.parser').text)
        Pr_list.append(Pr)
    Pr_list.remove(Pr_list[0])
    Pr_list.remove(Pr_list[-1])
    for p in Pr_list:
        proxy_file.write("{0}\n".format(p))
    proxy_file.close()
    print("{0} Proxy chaine was added done".format(len(Pr_list)))
except urllib.error.URLError as e:
    print(e)
except urllib.error.HTTPError as e:
    print(e)

