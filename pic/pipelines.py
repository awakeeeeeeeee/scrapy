# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib.request
import os
import ssl

class PicPipeline(object):
    def process_item(self, item, spider):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        print("name:"+str(item['name']))
        print("src:"+str(item['src']))
        #下面这行是处理需要ssl认证的情况
        ssl._create_default_https_context = ssl._create_unverified_context
        req = urllib.request.Request(url=item['src'],headers=headers)
        res = urllib.request.urlopen(req)
        file_name = os.path.join(r'/Users/cool/numb/python',item['name']+'.jpg')
        with open(file_name,'wb') as fp:
            fp.write(res.read())
