# coding: utf-8
import os

def getPacket(src):
    n=100000
    res=''
    with open (src,"r") as input:
        hexx=''
        src_line=input.readline()
        while(src_line):
            src_line = src_line.strip()

            if src_line == '':
                hex_list = hexx.strip().split()
                if(len(hex_list)<14):
                    src_line=input.readline()
                    continue

                for i in range(66,len(hex_list)):
                    res = res + hex_list[i][1]
                

                hexx = ''

            else:
                hexx = hexx + ' ' + src_line

            src_line=input.readline()
    #print(res)
    right=0
    wrong=0
    tmp=0
    for i in range(n):
        compare = ''
        for j in range (len(str(i))):
            compare += res[tmp+j]
        if(int(compare) == i):
            tmp+=len(str(i))
            right+=1
        elif(int(compare) < i):
            #print(i)
            wrong+=1
            #exit(0)
        elif(int(compare) > i):
            #print(i)
            wrong+=1
            #exit(0)
        
    print(src)
    print("right: "+str(right))
    print("wrong: "+str(wrong))
            
    #with open (des,"w") as output:
        #output.write(res)
        

src_txt='/home/yxy/Desktop/data/s/'
for filename in os.listdir(src_txt):
    getPacket(src_txt+str(filename))

