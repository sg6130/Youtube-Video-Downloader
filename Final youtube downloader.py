import re
from pytube import YouTube

regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')
file=open("C:/Users/SHUBHAM GUPTA/AppData/Local/Google/Chrome/User Data/Default/Bookmarks",encoding="utf8")

for line in file:
    if re.findall(r'[^"]*youtube[^"]*',line):
        m=re.split(r'"url":',line)
        print(m[1][2:-2])
        match1=regex.match(str(m[1][2:-2]))
           
        if match1 != None :
            print(match1.group(0))
            YouTube(match1.group(0)).streams.first().download('G:/Youtube videos')
            print("yes")


