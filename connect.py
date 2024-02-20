import os
value_check =0 #value so file da chia

#----------value global------# 
cwd = os.getcwd()
#----------------------------#
print(value_check)

#---------------------# 
#   kiem tra xem conver da du so luong times_lap chua
#   neu chua se conver lai
#   tao file mp3 chinh
#   xoa file phan tu
#---------------------# 
def check_file (): 
    lisk =[] 
    for k in os.listdir():
           if (k[0:2]=='ou') :
            lisk.append(k)
            """def check file"""
    for i in range(1,value_check):
        strl = 'out%s.mp3'%(str(i))
        if (strl in lisk ) :
            print('co')   
        else :
            name = 'out%s.mp3' %(str(i))
            print(name)
            #tts.tts(list_ss[i],name)
#--------------gop cac file mp3 lai voi nhau-------#
def creat_main_file (value_check,tilename):
    listc =[]
    value_check= int(value_check)
    if (tilename+'.mp3' in os.listdir()) :
        os.remove(cwd +'\\'+tilename+'.mp3')

    mainfile = open(cwd+'\\'+tilename+'.mp3','ab+')

    for ti in range(1,value_check+1):
        name = "out%s.mp3"%str(ti)
        file = open(name,'rb')
        mainfile.write(file.read())
        file.close()

    mainfile.close()
    for k in os.listdir():
           if (k[0:2]=='ou') :
            listc.append(k)
    #---------xoa file phan tu-----------#
    if (len(listc) == value_check ):
        for k in listc :
            os.remove(cwd + '\\' +k )

def check_st (check_st_va,i): 
    lisk =[] 
    for k in os.listdir():
           if (k[0:2]=='ou') :
            lisk.append(k)
            """def check file"""
    
    strl = 'out%s.mp3'%(str(i))
    if (strl in lisk ) :
            return True   
            #tts.tts(list_ss[i],name)