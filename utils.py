import time
import os
from io import BytesIO
import requests
from PIL import Image

def download(url):
    for i in range(3):
        try:
            with requests.get(url) as response:
                return Image.open(BytesIO(response.content))
        except Exception as e:
            print(f"{i}/3 Could not download Image '{url}'...")
            time.sleep(1)

def setBG(p, filename):
    if p == "feh":
        os.system(f"feh --bg-max {filename}")
    elif p == "nitrogen":
        os.system(f"nitrogen {filename}")
    elif p == "gsettings":
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file:{filename}")
        os.system("gsettings set org.gnome.desktop.background picture-options 'scaled'")
    elif p == "windows":
        os.system('reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d  wallpaper_path /f')
        os.system('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameter')
    elif p == "osascript":
        os.system(f"/bin/bash apple_set_bg.sh")
    elif p == "apple_defaults":
        os.system('''defaults write com.apple.desktop Background '{defaults = {ImageFilePath = "'''+str(filename)+'''"; };}';''')
    
    #set the Ubuntu Lock screen
    #os.system(f"sudo ./ubuntu-gdm-set-background --image {filename}")

#function to make Black box around Image
def make_border(image, width,height):
    old_im=image
    old_size = old_im.size
    new_size=(width,height)

    new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
    box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
    new_im.paste(old_im, box)
    return new_im


def combine(image1:Image,image2:Image,widht ,height):
    goldenratio=1/1.618
    new_size=(widht,height)
    new_Image=Image.new("RGB",new_size)
    pos1=(-1*int(image1.size[0]/2),int(new_Image.size[1]/2)-int(image1.size[1]/2))
    pos2=(int(new_Image.size[0]*goldenratio)-int(image2.size[0]/2),int(new_Image.size[1]/2)-int(image2.size[1]/2))
    new_Image.paste(image1,pos1)
    new_Image.paste(image2,pos2)
    new_Image.save("combi.png")
