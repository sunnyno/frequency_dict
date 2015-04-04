# -*- coding: utf-8 -*-

from xml.dom.minidom import *
import requests
from lxml import html
from gevent import monkey
import gevent
import ConfigParser

monkey.patch_socket()
f = open('info.txt', "a")


def make_cofig():
    conf = ConfigParser.RawConfigParser()
    if not conf.has_section('Version'):
        conf.add_section('Version')
        conf.set('Version', 'parallel', 'true')
    with open('l1.conf', 'wb') as configfile:
        conf.write(configfile)
    return conf.getboolean('Version', 'parallel')


def get_url(url):
    response = requests.get(url)
# Преобразование тела документа в дерево элементов (DOM)
    parsed_body = html.fromstring(response.text)
    f.write("\n".join(parsed_body.xpath('//title/text()')).encode("utf-8"))
    f.write("\n")
    f.write("\n\n".join(parsed_body.xpath('//h2/text()')).encode("utf-8"))
    f.write("\n".join(parsed_body.xpath('//p/text()')).encode("utf-8"))
    f.write("\n")



def get_urls():

    xml = parse('/home/eugenia/PycharmProjects/l1/dict/docs.xml')
    url = xml.getElementsByTagName('url')
    urls = []
    for node in url:
        urls.append(node.childNodes[0].nodeValue)
    return urls


def get_url_info():
    print ("sequential")
    urls = get_urls()
    for url in urls:
        get_url(url)


def get_url_info_inparallel():
    print("parallel")
    urls = get_urls()
    jobs = [gevent.spawn(get_url, url) for url in urls]
    gevent.joinall(jobs)
