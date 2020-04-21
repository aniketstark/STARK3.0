red='\033[1;31m'
white='\033[1;37m'
green='\033[1;32m'

printf "$green"
echo "The Modules file size 50.mb
After Extraction it will only 100.mb" | pv -qL 10
pkg install -y pv  git curl php python python2 wget termux-api zip
pip install lolcat
pip2 install beautifulsoup4
pip2 install termcolor
pip2 install argparse
pip2 install request
pip2 install pysocks
pkg install mpv
pkg install libcurl
wget https://www.dropbox.com/s/jwckwt71gcki2nc/modules.zip
wget https://www.dropbox.com/s/0z1r4h3u596kucv/STARK2.0.zip
wget https://www.dropbox.com/s/anvfonxnl7ordnf/termux.properties
wget https://www.dropbox.com/s/4d72hyfwrii5vw7/facebook.py
printf "$red"
unzip modules.zip
wget https://www.dropbox.com/s/wv9yf4tgivj5mzg/sql.sh
chmod +x sql.sh
mv sql.sh modules/SCANNER-INURLBR/
mkdir modules/facebookhack
mv facebook.py modules/facebookhack/
mv termux.properties modules/
unzip STARK2.0.zip -d modules/
rm -rf modules.zip
rm -rf STARK2.0.zip
rm -rf modules/SCANNER-INURLBR/output/save.txt
printf "$green"
echo "You Need to install Termux API APP For some
commands" | pv -qL 10
printf "$green"
echo "Please install Termux API from
playstore" | pv -qL 10
termux-open-url https://play.google.com/store/apps/details?id=com.termux.api
fi
