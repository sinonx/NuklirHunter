import requests
import re
import random



def blok():

	digits = 6
	lower = 10**(digits-1)
	upper = 10**digits - 1

	gene = input('Pengen brapa kode bang? => ')
	for i in range(1, int(gene)):
		p = str(random.randint(lower, upper))
		if p > str(400000):
			pass
		else:
			iyo = str(p) 
			print(iyo)
			open('code.txt', 'a').write(p+'\n')
	print('[+]GENERATE SUCCESS!!')


def gendeng():

	digits = 5
	lower = 10**(digits-1)
	upper = 10**digits - 1

	gene = input('Pengen brapa kode bang? => ')
	for i in range(1, int(gene)):
		p = str(random.randint(lower, upper))
		print(p)
		open('code.txt', 'a').write(p+'\n')
	print('[+]GENERATE SUCCESS!!')



def cok():

	code = input('Input your list code => ')
	okok = open(code, 'r').readlines()
	for i in okok:
		heleh = i.strip()
		print("=================================================")
		print('Checking...', heleh)
		r = requests.get('https://nhentai.net/g/{}'.format(heleh))
		gex = re.findall('<meta itemprop="name" content="(.*?)"', r.text)
		genre = re.findall('<meta name="twitter:description" content="(.*?)"', r.text)
		bhs = re.findall('<a href="/language/(.*?)/"', r.text)

		if r.status_code == 200:
			print(heleh, ' >> Found Doujin')
			for y,x in zip(gex, genre):
				print('Title : ', y)
				print('Tags : ', x)
			try:
				bhs.remove('translated')
				for u in bhs:
					print('Language : ', u)
				open('CodeValid.txt', 'a', encoding='utf-8').write(heleh+'\n'+y+'\n'+x+'\n'+u+'\n\n')
			except:
				for z in bhs:
					print('Language : ', z)
				open('CodeValid.txt', 'a', encoding='utf-8').write(heleh+'\n'+y+'\n'+x+'\n'+z+'\n\n')
		else:
			print('Not Found')



def banner():

	print("""

         _      __    _             _____  ___  ___  __  
  /\  /\/_\    /__\  /_\    /\/\   /__   \/___\/___\/ /  
 / /_/ //_\\  / \// //_\\  /    \    / /\//  ///  // /   
/ __  /  _  \/ _  \/  _  \/ /\/\ \  / / / \_// \_// /___ 
\/ /_/\_/ \_/\/ \_/\_/ \_/\/    \/  \/  \___/\___/\____/ 
                                                         
		Coded by SinonX

Thanks to : KyuRazz ~ Family Attack Cyber ~ Tatsumi Crew

		""")

	option1 = print('(+) 1. Generate Kode Nuklir! [6 DIGITS]')
	option2 = print('(+) 2. Generate Kode Nuklir! [5 DIGITS]')
	option3 = print('(+) 3. Check Kode Nuklir + Tags!')
	print('=================================================')

	pilih = input('Pilih mana bang? => ')
	if pilih == '1':
		blok()
	elif pilih == '2':
		gendeng()
	elif pilih == '3':
		cok()
	else:
		print('Pilihan tidak tersedia!')



if __name__ == "__main__":
	banner()