# coding: utf-8
import os

def getPacket(src,des):
    res=[]
    portlist=[]
    #line=0
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

                src_mac = ''
                dst_mac = ''
                for i in range(0,6):
                    dst_mac = dst_mac + hex_list[i]
                for i in range(6,12):
                    src_mac = src_mac + hex_list[i]
                if(((src_mac=='000c29d883b9')or(src_mac=='000c2938e2b8')or(src_mac=='000c29111e8e'))and(dst_mac=='000c29a5cc3b')and(hex_list[13]<>"06")):

                    '''
                    line+=1
                    if(line<3):
                        hexx=''
                        src_line=input.readline()
                        continue
                    '''

                    port=''
                    for i in range(36,38):
                        port += hex_list[i]
                    if port not in portlist:
                        portlist.append(port)
                        res.append([])
                    res[portlist.index(port)].append(hex_list)
                    
                hexx = ''

            else:
                hexx = hexx + ' ' + src_line

            src_line=input.readline()

    for k in range(len(portlist)):        
        with open (des+portlist[k]+'.txt',"w") as output:
            for i in range(2,len(res[k])):
                for j in range(len(res[k][i])):
                    output.write(" "+res[k][i][j])
                    if (j%16==15):
                        output.write("\n")
                output.write("\n")
                if(j%16<>15):
                    output.write("\n")


src_txt='/home/yxy/Desktop/s.txt'
des_txt='/home/yxy/Desktop/data/s/'
getPacket(src_txt,des_txt)

