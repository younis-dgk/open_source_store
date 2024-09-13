"""
    @ source by ---( Younis john )---
    @ Github : https://github.com/younis-dgk
    @ WhatsApp : +923194999455
    @ facebook : https://www.facebook.com/YounisDgk
    
"""
def ___fuck___():
	mix_model = requests.get('https://gist.githubusercontent.com/Nox-Naved/f0fe39c5e9ff2b70bcb39e48a3e77301/raw/413a4f26f81da4f40d51349a87facc2894bc0531/600+').text.splitlines()
	fb_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_vercode = str(random.randint(10000000, 66666666))
	ua1 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua2 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X008D;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua3 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=1.5,width=480,height=854};FBLC/pt_PT;FBRV/82651122;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00BD;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ua4 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1352};FBLC/it_IT;FBRV/203912779;FBCR/ho.;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua5= f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.778567894596777,width=1136,height=1485};FBLC/en_US;FBRV/0;FBCR/Comium;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/A21;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
	sex = random.choice([ua1,ua2,ua3,ua4,ua5])
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(mix_model)} Build/TP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ' + sex
	return ua