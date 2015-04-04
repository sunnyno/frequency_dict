# -*- coding: utf-8 -*-
import codecs
import hunspell as HS
import xml.etree.cElementTree as ET
import os
import re
import time
from info import *

work_file = 'info.txt'


def find_words():
    if make_cofig():
        get_url_info_inparallel()
    else:
        get_url_info()

    if os.path.isfile(work_file):
        print("work file " + work_file)
    file = codecs.open(work_file, encoding='utf-8', mode='r')
    txt = file.read()
    p = re.compile("([а-яА-ЯіІїЇЄє]+)".decode('utf-8'))
    return p.findall(txt)


def create_dict():
    res = find_words()
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


def check_dict():
    sorted_keys = create_dict()

    root = ET.Element("words")
    for key in sorted_keys:
        ET.SubElement(root, "word", quantity=str(lsWord[key])).text = key
    tree = ET.ElementTree(root)
    tree.write("result.xml")
    print('Резуьтат записан: result.xml')


def working_time():
    start = time.time()
    check_dict()
    finish = time.time()
    return finish-start

hobj = HS.HunSpell('/home/eugenia/AK/hunspell/uk_UA/uk_UA.dic',
                   '/home/eugenia/AK/hunspell/uk_UA/uk_UA.aff')
lsWord = {}
print ("Working time = " + str(working_time()))
