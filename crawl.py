
import requests
from time import sleep 
from bs4 import BeautifulSoup
from GoogleTTS import GoogleTTS
import effect
from alive_progress import alive_bar


tts = GoogleTTS()
global so_luong_chu 
global times_lap
global list_ss

so_luong_chu =500
list_ss= []
def get_data (ten_truyen,chuong='1') :
    req = requests.get(ten_truyen +" /chuong-"+ str(chuong) )
    soup  = BeautifulSoup(req.text,'html.parser') 
    data = soup.find_all('textarea')
    tilename = str(soup.find_all('div','chapter-title'))
    tilename = tilename.replace(tilename[-7:],'')
    tilename = tilename.replace('\n','')
    data = str(data) 
    lenght = len(data) - 140
    data=data.replace("”“",' ')
    data=data.replace("“",' ')
    data=data.replace("”",' ')
    data=data[31:lenght]+'.Hết chương '
    global times_lap
    times_lap =int(lenght/so_luong_chu) +1

    #chunks = [content[i:i + max_chars_per_file] for i in range(0, len(content), max_chars_per_file)]

    for ti in range(0,times_lap):
        start =ti*so_luong_chu
        end =(ti+1)*so_luong_chu
        list_ss.append(data[start:end])
    
    return data[31:lenght] ,list_ss,tilename[150:],lenght

def conver_mp3(list_ss) :
    hight = 10
    with alive_bar(hight,calibrate=50,title='Converting') as bar :
        # process item
        i =0
        list_file =[]
        for k in list_ss  :
            i=i+1
            data_byte =tts.tts(k)
            if (data_byte == None):
                while (data_byte == None ):
                    data_byte =tts.tts(k)
                    sleep(1)
                list_file.append(data_byte)
            else :
                list_file.append(data_byte)
                
            bar()
        
        if (len(list_file) !=0 ) :
            f= open('test3.mp3','ab')
            for dta in list_file :
                f.write(dta)
            f.close()
        
         
    list_file.clear()
    list_ss.clear()
        
