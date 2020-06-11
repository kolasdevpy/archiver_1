#!/usr/bin/python 3.8
# -*- coding: utf-8 -*-



from datetime import datetime
import os
import sys
import time




FUNC_NAME = sys.argv[1]
FILE_IN = sys.argv[2]
CACHE = 1000000        # max bytes in cache array   (must have: CACHE > 10)


def del_3_el(array):
    '''delete 1st, 2nd and 3th elements in first iteration => extension'''
    del array[0]
    del array[0]
    del array[0]
    return array

def add_to_file(array, FILE_OUT):
    '''add cache array to file out'''
    j = 0
    with open(FILE_OUT, 'ab') as f_arch:
        length = len(array) - 5
        while j != length:
            el = array[j]
            el = el.to_bytes(1, 'big')
            f_arch.write(el)
            j += 1
    return array


def compress(FILE_IN, CACHE):
    '''compress file into array'''
    FILE_OUT = (FILE_IN + '-arch')
    byte_raw = [75, 79, 76]
    print(f'{FILE_IN} compress into {FILE_OUT}')
    with open(FILE_IN, 'rb') as f:
        flag = True
        i = 0
        while f.read(1):
            f.seek(i)
            x = ord(f.read(1))

            if i == CACHE:
                #print(f'{i}  rec  ', datetime.now() - start_time)
                add_to_file(byte_raw, FILE_OUT)
                byte_raw = byte_raw[-5:]
                #print(f'{i}  end  ', datetime.now() - start_time)
                CACHE += CACHE

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

    j = 0
    with open(FILE_OUT, 'ab') as f_arch:
        length = len(byte_raw)
        while j != length:
            el = byte_raw[j]
            el = el.to_bytes(1, 'big')
            f_arch.write(el)
            j += 1

    size = os.path.getsize(FILE_OUT)
    print(f'COMPRESSED   IN {i}  ==>  OUT {size}      ratio OUT/IN =  {size/i}')
    return byte_raw


def decompress(FILE_IN, CACHE):
    '''decompress file into array'''
    time = datetime.now().strftime('%H.%M.%S_')
    FILE_OUT = (time +'_' + FILE_IN.split('-')[0])
    print(f'{FILE_IN} decompress into {FILE_OUT}')
    with open(FILE_IN, 'rb') as f:
        byte_raw = []
        i = 0
        flag_for_first_array = True
        flag = True
        while f.read(1):
            f.seek(i)
            x = ord(f.read(1))

            if i == CACHE:
                if flag_for_first_array:
                    del_3_el(byte_raw)
                    flag_for_first_array = False
                #print(f'{i}  rec  ', datetime.now() - start_time)
                add_to_file(byte_raw, FILE_OUT)
                byte_raw = byte_raw[-5:]
                #print(f'{i}  end  ', datetime.now() - start_time)
                CACHE += CACHE

            if i < 5:
                if i == 0 or i == 1 or i == 2:       # 1, 2, 3 elements - file extension (type)
                    byte_raw.append(x)
                elif i == 3:          # 1st and 2nd bytes invariably record into byte_raw always
                    byte_raw.append(x)
                elif i == 4:   
                    byte_raw.append(x)

            # after one fulfillment of this condition it is necessary to skip its fulfillment once
            elif byte_raw[-2] == byte_raw[-1] and flag:

                if x == byte_raw[-4] and x == byte_raw[-3] and x == byte_raw[-2] and x == byte_raw[-1]:
                    byte_raw.append(x)
                    flag = True                  # if more than 512 identical bytes in a row

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

    j = 0
    with open(FILE_OUT, 'ab') as f_arch:
        if flag_for_first_array:
            del_3_el(byte_raw)
        length = len(byte_raw)
        while j != length:
            el = byte_raw[j]
            el = el.to_bytes(1, 'big')
            f_arch.write(el)
            j += 1

    size = os.path.getsize(FILE_OUT)
    print(f'DECOMPRESSED   IN {i}  ==>  OUT {size}      ratio OUT/IN =  {size/i}')
    return byte_raw




# python3 archiver.py compress file
# python3 archiver.py decompress file-arch

if __name__ == "__main__":
    print('======================================================================================\n')
    if sys.argv[1] == 'compress':
        start_time = datetime.now()
        print(datetime.now().strftime('%H.%M.%S_%f'))
        compress(FILE_IN, CACHE)
        print(datetime.now() - start_time)
        print('======================================================================================')


    elif sys.argv[1] == 'decompress':
        start_time = datetime.now()
        print(datetime.now().strftime('%H.%M.%S_%f'))
        decompress(FILE_IN, CACHE)
        print(datetime.now() - start_time)
        print('======================================================================================')

    else:
        print('Please, input correctly your instruction')
        print('FOR EXAMPLE:  python3 archiver.py compress capitals.txt')
        print('\t\t archiver.py decompress capitals.txt-arch')
