import os, sys

print ("\033[1;32mDAH YA ANJING:)")
print ("\033[1;31;1mGAK USAH MASUK LAGI")
print ("\033[1;32mUSERNAME : MAKASIH PASSWORD : BANG")

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password :
			print "\n\033[1;34mKONTOL LU ANJING", 
			sys.exit()

		else:
			print "\n\033[1;36mSalah Anjing Keluar Aja!!!\033[00m"
			print "Ga Bakal Bisa Masuk Asu!!\n"
			restart()

	else:
		print "\n\033[1;36mSalah Anjing Keluar Aja Ngentot\033[00m"
		print "Ga Bakal Bisa Masuk asu!!\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
	
