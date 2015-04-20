# -*- coding: utf-8 -*-
import urllib2
from xml.dom.minidom import *
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


def get_url(url, f):
    response = urllib2.urlopen(url).read().decode('latin-1')
# Преобразование тела документа в дерево элементов (DOM)
    parsed_body = html.document_fromstring(response)
    if 'nashakazka' in str(url):
        f.write("\n".join(parsed_body.xpath('//title/text()'))
                .encode("iso8859-1"))
        f.write("\n".join(parsed_body.xpath('//p/text()')).encode("iso8859-1"))
    else:
        f.write("\n".join(parsed_body.xpath('//title/text()')).encode("utf-8"))
        f.write("\n")
        f.write("\n\n".join(parsed_body.xpath('//h2/text()')).encode("utf-8"))
        f.write("\n".join(parsed_body.xpath('//p/text()')).encode("utf-8"))
        f.write("\n")


def get_urls(doc):
    xml = parse(doc)
    url = xml.getElementsByTagName('url')
    urls = []
    for node in url:
        urls.append(node.childNodes[0].nodeValue)
    return urls




