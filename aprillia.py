#!/usr/bin/python/sh
# encoding: utf-8
#install bahan

figlet Install Bahan | lolcat
sleep 3

pkg update && pkg upgrade
pkg install sl
pip install request mechanize

figlet selesai | lolcat
sleep 1

echo WWW.XNXX.COM/ |lolcat
sleep 5
echo WWW.PORNHUB.COM |lolcat
sleep 5

sl
cleaar
echo LOADING... | lolcat
sleep 5

toilet -f big -F gay MyProfil | lolcat
echo "<=============================================>" | lolcat
echo "[•] Author : MR-Xyaa                         
echo "[•] FB     : Xyaa Xyaa                         
echo "[•] GitHub : github.com/MR-Xyaa              
echo "<=============================================>" | lolcat

import os, sys

print ("\033[1;32mMasukan UserName&Password:)")
print ("\033[1;32mKalo Gak Tau Pm MR-Xyaa 083138613993")
print ("\033[1;32mAtau Kunjungi Github Gw")
username = 'IBNU'      
password = 'APRILLIA'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mHello Welcome To Tools MR-Xyaa", 
			sys.exit()

		else:
			print "\n\033[1;36mSalah Passwordnya Asu !!!\033[00m"
			print "Back Login\n"
			restart()

	else:
		print "\n\033[1;36mSalah Username Nya Babi !!!\033[00m"
		print "Back Login\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
	
	
