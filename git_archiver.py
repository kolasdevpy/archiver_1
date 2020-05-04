#!/usr/bin/python 3.8
# -*- coding: utf-8 -*-



import sys
from datetime import datetime
import time




FUNC_NAME = sys.argv[1]
FILE_IN = sys.argv[2]


def compress(FILE_IN):
    '''compress file into array'''
    byte_raw = [75, 79, 76]
    #BYTE_RAW_IN = []
    with open(FILE_IN, 'rb') as f:
        flag = True
        i = 0
        while f.read(1):
            f.seek(i)
            x = ord(f.read(1))
            #BYTE_RAW_IN.append(x)
 
            if i == 0:   # 1st byte invariably record into byte_raw always
                byte_raw.append(x)

            elif x == byte_raw[-1] and flag:
                byte_raw.append(x)
                compress_byte_counter = 0
                byte_raw.append(compress_byte_counter)
                flag = False

            elif x == byte_raw[-3] and x == byte_raw[-2] and not flag:
                byte_raw[-1] += 1

                if byte_raw[-1] == 255:             # counter more than 255 = UnError
                    byte_raw[-1] = 253
                    byte_raw.append(byte_raw[-2])
                    byte_raw.append(byte_raw[-3])
                    byte_raw.append(0)

            else:
                byte_raw.append(x)
                flag = True

            i +=1




    print('---------------------------------------')
    # print(f'{BYTE_RAW_IN[:100]} <-----------> {BYTE_RAW_IN[-100:]}')
    # print('---------------------------------------')
    # print(f'{byte_raw[:100]} <-----------> {byte_raw[-100:]}')
    # print('---------------------------------------')
    # print('BYTE_IN  = ' + str(len(BYTE_RAW_IN)))
    print('BYTE_OUT = ' + str(len(byte_raw)))
    # print('Compress = ' + str(len(byte_raw) / len(BYTE_RAW_IN)))
    print('======================================================================================')

    return byte_raw




def decompress(FILE_IN):
    '''decompress file into array'''
    with open(FILE_IN, 'rb') as f:
        byte_raw = []
        #BYTE_RAW_IN = []
        i = 0
        flag = True
        
        while f.read(1):
            f.seek(i)
            x = ord(f.read(1))
            #BYTE_RAW_IN.append(x)
            
            if i == 0 or i == 1 or i == 2:       # 1, 2, 3 elements - file extension (type)
                byte_raw.append(x)
            elif i == 3:          # 1st and 2nd bytes invariably record into byte_raw always
                byte_raw.append(x)
            elif i == 4:   
                byte_raw.append(x)

            elif byte_raw[-2] == byte_raw[-1] and flag:

                if x == byte_raw[-4] and x == byte_raw[-3] and x == byte_raw[-2] and x == byte_raw[-1]:
                    byte_raw.append(x)
                    flag = True

                elif x == 0:
                    flag = False
                    
                else:
                    for _ in range(x):
                        byte_raw.append(byte_raw[-1])
                    flag = False
                    
            else:
                byte_raw.append(x)
                flag = True
                
            i += 1
        print('del begin', datetime.now() - start_time)
        del byte_raw[0]
        print('del 0', datetime.now() - start_time)
        del byte_raw[0]
        print('del 1', datetime.now() - start_time)
        del byte_raw[0]
        print('del 2', datetime.now() - start_time)

    print('---------------------------------------')
    # print(f'{BYTE_RAW_IN[:100]} <-----------> {BYTE_RAW_IN[-100:]}')
    # print('---------------------------------------')
    # print(f'{byte_raw[:100]} <-----------> {byte_raw[-100:]}')
    # print('---------------------------------------')
    # print('BYTE_IN  = ' + str(len(BYTE_RAW_IN)))
    print('BYTE_OUT = ' + str(len(byte_raw)))
    # print('Deompress = ' + str(len(byte_raw) / len(BYTE_RAW_IN)))
    print('======================================================================================')

    return byte_raw




def write_into_archived_file(array, FILE_IN):
    '''Write array into file'''
    with open(FILE_IN + '-arch', 'wb') as f:
        print('write', datetime.now() - start_time)
        i = 0
        while i != len(array):
            for el in array:
                el = el.to_bytes(1, 'big')
                f.write(el)
                i += 1
    f.close()
    return FILE_IN # преобразовать в новый






def write_into_unarchived_file(array, FILE_IN):
    '''Write array into file'''
    FILE_OUT = 'new_' + FILE_IN.split('-')[0]
    with open(FILE_OUT, 'wb') as f:
        print('write', datetime.now() - start_time)
        i = 0
        while i != len(array):
            for el in array:
                el = el.to_bytes(1, 'big')
                f.write(el)
                i += 1
    f.close()
    return FILE_OUT



# python3 archiver.py compress 'file_name'
# python3 archiver.py decompress 'file_name'

if __name__ == "__main__":
    print('\n\n\n')
    if sys.argv[1] == 'compress':
        start_time = datetime.now()
        print(f'{FILE_IN} compression in progress')
        array = compress(FILE_IN)
        print(datetime.now() - start_time)
        write_into_archived_file(array, FILE_IN)
        print(datetime.now() - start_time)

    elif sys.argv[1] == 'decompress':
        start_time = datetime.now()
        print(f'{FILE_IN} file decompression in progress')
        array = decompress(FILE_IN)
        print(datetime.now() - start_time)
        write_into_unarchived_file(array, FILE_IN)
        print(datetime.now() - start_time)

    else:
        print('Please, input correctly your instruction')
        print('FOR EXAMPLE:  python3 archiver.py compress capitals.txt')
        print('\t\t archiver.py decompress capitals.txt-arch')
