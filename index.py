import os 
import crawl
import crawl_ok
from GoogleTTS import GoogleTTS

cwd = os.getcwd()
tts = GoogleTTS()
CYELLOW2 = '\33[93m'
CEND      = '\33[0m'



def dow ():
    print(CYELLOW2 + 'Tên truyện cần tải'+ CEND)
    ten_truyen = input()
    print(CYELLOW2 + 'bắt đầu từ chương : '+ CEND)
    chap_st = input()
    print(CYELLOW2 + 'đến chương : '+ CEND)
    chap_end = input()
    for i in range(int(chap_st),int(chap_end)+1):

        data = crawl_ok.get_text_from_url(ten_truyen+f"/chuong-{i}")
        list_ss =crawl_ok.split_text_into_chunks(data)
    #-----------------prosscess main ------------------#  13212
        print(f'\n'+'\x1b[6;30;42m' + 'Start downloading chapter--'+'\x1b[0m') 
        crawl.conver_mp3(list_ss)
dow()
print('\x1b[6;30;42m' + '\nSuccess! '+ '\x1b[0m'+'\n')

#connect.check_file()
#connect.creat_main_file(times_lap+1,tilename)


         







