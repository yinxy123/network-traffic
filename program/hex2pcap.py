# coding: utf-8

import os
import csv
csv.field_size_limit(500 * 1024 * 1024)


def hexToPcap(src_dir_path, tmp_dir_path, res_pcap_path):
    for filename in os.listdir(src_dir_path):
        src_f = open(src_dir_path+'/'+filename, 'r')
        f_hex = open(tmp_dir_path+'/'+filename, 'w')

        hexx = ''

        for src_line in src_f:
            src_line = src_line.strip()

            if src_line == '':

                hex_list = hexx.strip().split()
                # print hex_list
                offset = ''
                len_hex = len(hex_list)
                frow = ''
                for i in range(len_hex):
                    frow += ' ' + hex_list[i]
                    # an enough line (16)
                    if (i + 1) % 16 == 0:
                        # print format((i+1-16),'04')
                        # print hex(i+1-16)[2:].rjust(4,'0')
                        offset = hex(i + 1 - 16)[2:].rjust(4, '0')
                        totalrow = offset + frow + '\n'
                        f_hex.write(totalrow)
                        # print totalrow
                        frow = ''
                # the rest line (not enough one line)
                offset = hex(len_hex / 16 * 16)[2:].rjust(4, '0')
                totalrow = offset + frow + '\n'
                f_hex.write(totalrow)
                # print totalrow
                offset = hex(len_hex)[2:].rjust(4, '0') + '\n'
                # print offset
                f_hex.write(offset)

                hexx = ''

            else:
                hexx = hexx+' '+src_line

        if hexx != '':
            hex_list = hexx.strip().split()
            # print hex_list
            offset = ''
            len_hex = len(hex_list)
            frow = ''
            for i in range(len_hex):
                frow += ' ' + hex_list[i]
                # an enough line (16)
                if (i + 1) % 16 == 0:
                    # print format((i+1-16),'04')
                    # print hex(i+1-16)[2:].rjust(4,'0')
                    offset = hex(i + 1 - 16)[2:].rjust(4, '0')
                    totalrow = offset + frow + '\n'
                    f_hex.write(totalrow)
                    # print totalrow
                    frow = ''
            # the rest line (not enough one line)
            offset = hex(len_hex / 16 * 16)[2:].rjust(4, '0')
            totalrow = offset + frow + '\n'
            f_hex.write(totalrow)
            # print totalrow
            offset = hex(len_hex)[2:].rjust(4, '0') + '\n'
            # print offset
            f_hex.write(offset)

            hexx = ''

        src_f.close()
        f_hex.close()

    # tmp_hex to pcap
    for filename in os.listdir(tmp_dir_path):
        command = 'text2pcap ' + tmp_dir_path+'/'+filename + ' ' + res_pcap_path+'/'+filename[:-4] + '.pcap'
        os.system(command)


if __name__ == '__main__':
    src_dir_path = './data/s'   # 原始文件夹 最后不要带'/'
    tmp_dir_path = './data/t'   # 中间文件夹 最后不要带'/'
    res_pcap_path = './data/p'  # 结果pcap文件夹 最后不要带'/'

    hexToPcap(src_dir_path, tmp_dir_path, res_pcap_path)
