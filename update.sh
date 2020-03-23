lg='\033[1;32m'
lr='\033[1;31m'

filecheck () {
echo CHECKING MODULE FOLDER IS EXIST OR NOT| lolcat -a -d 50
file2
}

file2 () {
if [ -d "modules" ]
  then
    rm -rf ~/STARK3.0/modules/secret
    rm -rf ~/STARK3.0/modules/login.py
    printf "$lg"
    echo "Backuping Modules"
    mv ~/STARK3.0/modules ~
    cd && wget  https://www.dropbox.com/s/g4x3v4c9nyr07di/update1.zip
    unzip -j ~/update1.zip
    rm -rf ~/update1.zip
    chmod +x ~/update1.sh
    bash ~/update1.sh
    rm -rf ~/update1.sh
  else
    printf "$lr"
    echo "Error: Oops You Don't Install Modules Run bash install.sh"
fi
}

filecheck

