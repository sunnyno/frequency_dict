from info import  *

def get_url_info(doc):
    print ("sequential")
    urls = get_urls(doc)
    for url in urls:
        get_url(url, f)


def get_url_info_inparallel(doc):
    print("parallel")
    urls = get_urls(doc)
    jobs = [gevent.spawn(get_url, url, f) for url in urls]
    gevent.joinall(jobs)

def get_info(doc):
   if make_cofig():
       get_url_info_inparallel(doc)
   else:
       get_url_info(doc)
