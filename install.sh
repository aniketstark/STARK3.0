red='\033[1;31m'
white='\033[1;37m'
green='\033[1;32m'

printf "$green"
echo "The Modules file size 50.mb
After Extraction it will only 100.mb" | pv -qL 10
pkg install -y pv ruby  git curl php python python2 wget termux-api zip
gem install colorize
pip install lolcat
pip2 install beautifulsoup4
pip2 install termcolor
pip2 install argparse
pip2 install request
pip2 install pysocks
pkg install mpv
pkg install libcurl
wget https://www.dropbox.com/s/geyq8mba09sromy/modules.zip
printf "$red"
unzip modules.zip
wget https://www.dropbox.com/s/72khp3yvrc9de7t/SecretServer.zip
unzip SecretServer.zip
rm -rf SecretServer.zip
mv Secret modules/
rm -rf modules.zip
rm -rf modules/SCANNER-INURLBR/output/save.txt
printf "$green"
echo "You Need to install Termux API APP For some
commands" | pv -qL 10
printf "$green"
echo "Please install Termux API from
playstore" | pv -qL 10

fi
