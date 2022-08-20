import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import langdetect
import hashlib
import requests
import multiprocessing
import threading
from queue import Queue
from bs4 import BeautifulSoup


class Crawler(object):
    def __init__(self):
        pass

    def sha256(self, input_str):
        encoder = hashlib.sha256()
        encoder.update(input_str.encode())
        return encoder.hexdigest()

    def multi_processing(self, input_list):
        pool = multiprocessing.Pool(processes=6)
        result = pool.map_async(self.multi_thread_crawling, input_list)
        pool.close()
        pool.join()
        
        return result
        

    def multi_thread_crawling(self, batch_inputs):
        # use queue object to collect returned info from the crawlers
        q = Queue()
        threads = []
        for url in batch_inputs:
            t = threading.Thread(target= self.crawling, args=(url, q))
            t.start()
            threads.append(t)
        
        for thread in threads:
            thread.join()

        return [q.get() for i in range(q.qsize())]


    def crawling(self, url, Q_object):
        # url = "https://udn.com/news/cate/2/7227"
        try:
            html = requests.get(url, 
                            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}, 
                            timeout=5)

            if html.status_code == 200:
                html.encoding = 'utf-8'
                soup = BeautifulSoup(html.text, 'lxml')

                title = soup.find('meta', attrs={'property':'og:title'})
                lang = soup.find('html')

                if title != None and lang != None:
                    if 'lang' in lang.attrs:
                        title = title.attrs['content']
                        lang_code = lang.attrs['lang'][:2]
                        if len(lang_code) == 2 and len(title) > 0:
                            title_hash = self.sha256(title)
                            url_hash = self.sha256(url)
                            
                            if lang_code == 'en':
                                lang_code = langdetect.detect(title)[:2]
                            
                            Q_object.put([url, url_hash, title, title_hash, lang_code])

            elif html.status_code == 429:
                Q_object.put([url])

        except Exception:
            pass
        
    