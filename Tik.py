# Creator : Xenzi Ganz
# Janggan lupa subs

###----------[ ANSII COLOR STYLE ]---------- ###
Z2 = "\x1b[0;90m"     # Hitam
M2 = "\x1b[38;5;196m" # Merah
H2 = "\x1b[38;5;46m"  # Hijau
K2 = "\x1b[38;5;226m" # Kuning
B2 = "\x1b[38;5;44m"  # Biru
U2 = "\x1b[0;95m"     # Ungu
O2 = "\x1b[0;96m"     # Biru Muda
P2 = "\x1b[38;5;231m" # Putih
J2 = "\x1b[38;5;208m" # Jingga
A2 = "\x1b[38;5;248m" # Abu-Abu
###----------[ ANSII COLOR STYLE 2 ]---------- ###
P1 = "\033[37;7;1m"
M1 = "\033[31;7;1m"
H1 = "\033[32;7;1m"
K1 = "\033[33;7;1m"
B1 = "\033[34;7;1m"
U1 = "\033[35;7;1m"
O1 = "\033[36;7;1m"
A1 = "\033[0m"
L1 = "\033[4m"
###----------[ ANSII COLOR STYLE 3 ]---------- ###
Z = "\x1b[1;90m"
M = "\x1b[1;91m"
H = "\x1b[1;92m"
K = "\x1b[1;93m"
B = "\x1b[1;94m"
U = "\x1b[1;95m"
O = "\x1b[1;96m"
P = "\x1b[1;97m"
import os,sys
try:
        import requests
except ImportError as e:
        print (f" {M}• {P}Sedang intall bahan {H}{e.name}, {P}Mohon Tunggu...")
        os.system(f"python -m pip install {e.name} &> /dev/null")
try:
        import bs4
except ImportError as e:
        print (f" {M}• {P}Sedang intall bahan {H}{e.name}, {P}Mohon Tunggu...")
        os.system(f"python -m pip install {e.name} &> /dev/null")

import time, os, requests, json, random, bs4
xyz = requests.Session()
war = random.choice([O,U,K])
banner = f"""{war}

  ____________  ___                  __             __
 /_  __/_  __/ / _ \___ _    _____  / /__  ___ ____/ /
  / /   / /   / // / _ \ |/|/ / _ \/ / _ \/ _ `/ _  /
 /_/   /_/   /____/\___/__,__/_//_/_/\___/\_,_/\_,_/

   {M}• {P}Author {M}: {P}Xenzi Ganz
   {M}• {P}Github {M}: {K}/Aldi098 - /Xenzi-XN1
   {M}• {P}Team   {M}: {H}Team Xenzi, XTC | Code Team, Dark Club

 {M}• {P}Masukan Link Video Tiktok {M}({H}https://vt.tiktok.com/balablaba{M})"""

path = "/storage/emulated/0/Download-video-tiktok"
try:
        os.mkdir(path)
except:
        pass


class Logo:
	def __init__(self):
		pass

	def logo(self):
		os.system('clear')
		print (banner)

class Main:
	def __init__(self):
		pass

	def dow_tt(self, tk_vid, id_vid, nama_vid):
		nm_vid = f"tiktok_download_{nama_vid}"
		try:
			print (f' {M}• {P}Sedang Mendownload Video {M}....')
			run = xyz.get(f'https://tikmate.app/download/{tk_vid}/{id_vid}.mp4?hd=1').content
			with open(f"{path}/{nm_vid}.mp4", "wb") as sv:
				sv.write(run)
				print (f'\n {M}• {P}Tersimpan di {M}: {H}{path}/{nm_vid}.mp4')
		except KeyError:
			exit(f' {M}• {P}Url/Video Eror XD')
	def get_dat(self, url):
		data = {"url": url}
		try:
			data = requests.post('https://api.tikmate.app/api/lookup',data=data).text
			resp = json.loads(data)
			if 'true' in data:
				tk_vid = resp['token']
				id_vid = resp['id']
				at_vid = resp['author_name']
				tl_cm_vid = resp['comment_count']
				tl_lk_vid = resp['like_count']
				tl_sh_vid = resp['share_count']
				tll_up_vid = resp['create_time']
				print (f'\n {M}• {P}Nama Creator {M}: {H}{at_vid}')
				print (f' {M}• {P}id Video {M}: {H}{id_vid}')
				print (f' {M}• {P}Tanggal Upload Video {M}: {H}{tll_up_vid}')

				print (f'\n {M}• {P}Total Komen {M}: {H}{tl_cm_vid}')
				print (f' {M}• {P}Total Like  {M}: {H}{tl_lk_vid}')
				print (f' {M}• {P}Total Share {M}: {H}{tl_sh_vid}')
				gas = input(f'\n {M}• {P}Inggin Download Video {M}[{H}Y/T{M}]:{H} ')
				if gas in ['Y','y']:
					nama_vid = input(f'\n {M}• {P}Masukan Nama Video {M}[{P}OUTPUT{M}]{M}:{H} ')
					self.dow_tt(tk_vid, id_vid, nama_vid)
				else:
					exit(f' {M}• {P}Thanks udah pake tools aing >_')

			else:
				exit(f' {M}• {P}Url/Video Eror XD')

		except KeyError:
			exit(f' {M}• {P}Url/Video Eror XD')
	def mulai(self):
		Logo().logo()
		url = input(f' {M}• {P}Link {M}:{H} ')
		if url in ['']:
			exit(f' {M}• {P}Masukan link Dengan Benar -_-')
		else:
			self.get_dat(url)
Main().mulai()
