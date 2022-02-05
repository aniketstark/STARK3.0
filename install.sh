red='\033[1;31m'
white='\033[1;37m'
green='\033[1;32m'

printf "$green"
echo "INSTALLING IMPORTANT PACKAGES"
apt-get -y --allow-unauthenticated install pv ruby  git curl php python python2 wget termux-api zip libcurl mpv
gem install colorize
pip install lolcat
pip2 install beautifulsoup4
pip2 install termcolor
pip2 install argparse
pip2 install request
pip2 install pysocks
printf "$green"
echo "You Need to install Termux API APP For some
commands" | pv -qL 10

FILE=~/STARK3.0/modules.zip
printf "$green"
echo "cheking module.zip file is exist or not........"
if test -f "$FILE"; then
    echo "$FILE ok files exist."
else 
    printf "$red"
    echo "$FILE does not exist."
    echo "INSTALLING modules.zip"
    printf "$green"
    echo "The Modules file size 50.mb 
    After Extraction it will only 100.mb" | pv -qL 10
    wget https://www.dropbox.com/s/72khp3yvrc9de7t/SecretServer.zip
    unzip SecretServer.zip
    rm -rf SecretServer.zip
    mv Secret modules/
    rm -rf modules.zip
    rm -rf modules/SCANNER-INURLBR/output/save.txt
fi

