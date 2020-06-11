#!/usr/bin/python 3.8
# -*- coding: utf-8 -*-


# recursively test for complex directory with set DIRS and FILES


from datetime import datetime
import sys
import time
import os


FUNC_NAME = sys.argv[1]
DIR = sys.argv[2]
ALL_COMPRESSIONS = []
<<<<<<< HEAD
CACHE = 100
=======
>>>>>>> f9e5395d176d1d9989a3ab720f6e4198aeb9009a



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


def compress(FILE_IN, CACHE, FILE_OUT):
    '''compress file into array'''
    byte_raw = [75, 79, 76]
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

    size_IN = os.path.getsize(FILE_OUT)
    return byte_raw, FILE_OUT, size_IN


def decompress(FILE_OUT, CACHE, FILE_OUT_2):
    '''decompress file into array'''
    with open(FILE_OUT, 'rb') as f:
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
                add_to_file(byte_raw, FILE_OUT_2)
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
    with open(FILE_OUT_2, 'ab') as f_arch:
        if flag_for_first_array:
            del_3_el(byte_raw)
        length = len(byte_raw)
        while j != length:
            el = byte_raw[j]
            el = el.to_bytes(1, 'big')
            f_arch.write(el)
            j += 1

    size_OUT = os.path.getsize(FILE_OUT_2)
    return byte_raw, size_OUT

def sizes(FILE_IN, FILE_OUT_2, FILE_OUT, ALL_COMPRESSIONS) :
    SIZE_IN = os.path.getsize(FILE_IN)
    SIZE_OUT = os.path.getsize(FILE_OUT)
    SIZE_OUT2 = os.path.getsize(FILE_OUT_2)
    if SIZE_IN == SIZE_OUT2:
        compression = SIZE_OUT/SIZE_IN
        #print(f'{SIZE_IN} == {SIZE_OUT2} --- coooool --- {compression}')
        #print("{:11d}  {:11d}  {:10f} ".format(SIZE_IN, SIZE_OUT2, compression))
        ALL_COMPRESSIONS.append(compression)
    else:
        broken = f'{FILE_IN} {SIZE_IN} != {SIZE_OUT2}'
<<<<<<< HEAD
        print(f'{broken} +++++  BROKEN  +++++')
=======
        print(f'{broken} ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
>>>>>>> f9e5395d176d1d9989a3ab720f6e4198aeb9009a
        with open('_log.txt', 'a') as f_log:
            f_log.writelines(broken + '\n')
    return ALL_COMPRESSIONS


<<<<<<< HEAD
def stack(DIR, CACHE):
=======
def stack(DIR):
>>>>>>> f9e5395d176d1d9989a3ab720f6e4198aeb9009a
    i = 0
    for top, dirs, files in os.walk(DIR):
        for nm in files:
            if nm.startswith('_archiver_test.py') or nm.startswith('_log.txt') or nm.startswith('.'):
                dirs, top
                pass
            else:
                if i % 10 == 0:
                    print(i)
<<<<<<< HEAD
                    # time.sleep(1)        # if overheats ;)
                FILE_IN = f'{top}/{nm}'
                print(f'{FILE_IN}')
                FILE_OUT = (FILE_IN + '-arch')
                new = datetime.now().strftime('%Y-%m-%d_%H.%M.%S.%f')
                FILE_OUT_2 = f'{top}/{new}{nm}'
=======
                    time.sleep(1)
                FILE_IN = f'{top}/{nm}'
                print(f'{top}/{nm}')
                FILE_OUT = (FILE_IN + '-arch')
                new = datetime.now().strftime('%Y-%m-%d_%H.%M.%S.%f')
                FILE_OUT_2 = f'{top}/{new}{nm}'

                CACHE = 100
>>>>>>> f9e5395d176d1d9989a3ab720f6e4198aeb9009a
                compress(FILE_IN, CACHE, FILE_OUT)
                decompress(FILE_OUT, CACHE, FILE_OUT_2)
                sizes(FILE_IN, FILE_OUT_2, FILE_OUT, ALL_COMPRESSIONS)
                
                i += 1
    print(i)



# python3 _archiver_AUTO_TESTING.py run DIR

if __name__ == "__main__":
    if sys.argv[1] == 'run':
<<<<<<< HEAD
        stack(DIR, CACHE)
=======
        stack(DIR)
>>>>>>> f9e5395d176d1d9989a3ab720f6e4198aeb9009a
        print(sum(ALL_COMPRESSIONS)/len(ALL_COMPRESSIONS))
    else:
        print('Please, input correctly your instruction')

