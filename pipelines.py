# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import urllib.request
import urllib.parse
import urllib.error
class ImgspiderPipeline(object):
    def __init__(self):
        self.dir='E:\imgspider\imgspider\image'
    def process_item(self, item, spider):
        fulldir=self.dir+'\\'+item['title'][0]+'\\'
        print(fulldir)
        if os.path.exists(fulldir):
            pass
        else:
            os.mkdir(fulldir)
        for imgurl in item['imgurls']:
            filename = fulldir + imgurl[-8:]
            if os.path.isfile(filename)==False:
                try:
                    new_url = imgurl.replace(imgurl.split('/')[-1], urllib.parse.quote(imgurl.split('/')[-1]))
                    urllib.request.urlretrieve(new_url, filename)
                except urllib.error.URLError as e:
                    print(e)

                except Exception as e:
                    print(e)


        return item
