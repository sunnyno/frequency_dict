# -*- coding: utf-8 -*-
import codecs
import hunspell as HS
import xml.etree.cElementTree as ET
import os
import re
import time
from url_work import *

work_file = 'info.txt'
res_file = 'result.xml'
doc ='/home/eugenia/PycharmProjects/l1/dict/docs.xml'
f = open('info.txt', "a")





def find_words(work_f):

    if os.path.isfile(work_f):
        print("work file " + work_f)
    file = codecs.open(work_f, encoding='utf-8', mode='r')
    txt = file.read()
    p = re.compile("([а-яА-ЯіІїЇЄє]+)".decode('utf-8'))
    return p.findall(txt)


def create_dict(work_file):
    res = find_words(work_file)
    for key in res:
        if hobj.spell(key):
            key = hobj.stem(key)[0].decode('utf-8')
        else:
            continue
        if key in lsWord:
            value = lsWord[key]
            lsWord[key] = value+1
        else:
            lsWord[key] = 1
# создаем список ключей отсортированный по значению словаря lsWord
    sorted_keys = sorted(lsWord, key=lambda x: int(lsWord[x]), reverse=True)
    return sorted_keys


def check_dict(res_file, work_file):
    sorted_keys = create_dict(work_file)
    root = ET.Element("words")
    for key in sorted_keys:
        ET.SubElement(root, "word", quantity=str(lsWord[key])).text = key
    tree = ET.ElementTree(root)
    tree.write(res_file)
    print('Резуьтат записан: ' + res_file)


def working_time():
    start = time.time()
    get_info(doc)
    check_dict(res_file,work_file)
    finish = time.time()
    print (finish-start)

hobj = HS.HunSpell('/home/eugenia/AK/hunspell/uk_UA/uk_UA.dic',
                   '/home/eugenia/AK/hunspell/uk_UA/uk_UA.aff')
lsWord = {}

if __name__ == '__main__':
    working_time()
