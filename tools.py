import os
import time

os.system('clear')
time.sleep(1)
os.system('figlet Tools')
print
print "============================="
print "Author : Fajar Khairul Ikhsan"
print "Facebook : Fajar Khairul Ikhsan"
print "Github : Kepo Lu Monyet"
print "============================="
print
time.sleep(1)
print "[!] Pilih Tools [!]"
print "==================="
print "1. Dark Fb"
print "==================="
print "2. Dark Fb Premium"
print "==================="
print "3. Hack CCTV v3.7"
print "==================="
print "4. Hack FB Target"
print "==================="
print "5. Prank Spammer"
print "==================="
print "9. Install Bahan"
print "==================="
print
pilih = raw_input('[?] Pilih : ')
if pilih == "1":
	os.system('clear')
	os.system('git clone https://github.com/B4N954N2-ID/Dark')
	print "[+] Selanjutnya Ketik $ cd Dark"
	print "[+] Lalu Ketik $ python2 darkfb.py"
elif pilih == "2":
	os.system('clear')
	os.system('git clone https://github.com/B4N954N2-ID/DarkPremium')
	print "[+] Selanjutnya Ketik $ cd DarkPremium"
	print "[+] Lalu Ketik $ python2 darkpremium.py"
elif pilih == "3":
	os.system('clear')
	os.system('git clone https://github.com/storiku/HackCCTV')
	print "[+] Selanjutnya Ketik $ cd HackCCTV"
	print "[+] Lalu Ketik $ python2 HCCTV.py"
elif pilih == "4":
	os.system('clear')
	os.system('git clone https://github.com/storiku/fbtarget')
	print "[+] Selanjutnya Ketik $ cd fbtarget"
	print "[+] Lalu Ketik $ python2 target.py"
elif pilih == "5":
	os.system('clear')
	os.system('git clone https://github.com/B4N954N2-ID/spam-call')
	print "[+] Selanjutnya Ketik $ cd spam-call"
	print "[+] Lalu Ketik $ python2 Call.sh"
elif pilih == "9":
	os.system('pkg install git')
	os.system('pkg install bash')
	os.system('pkg install python2')
	os.system('clear')
	print "[!] Install Bahan Is Done [!]"
