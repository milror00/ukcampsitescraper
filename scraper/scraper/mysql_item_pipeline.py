# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import logging
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem, NotConfigured
from scrapy.http import Request
from scrapy.utils import spider


class MySQLTescoPipeline():

    def __init__(self, db, user, passwd, host):
        self.db = db
        self.user = user
        self.passwd = passwd
        self.host = host

    @classmethod
    def from_crawler(cls, crawler):
        db_settings = crawler.settings.getdict("DB_SETTINGS")
        if not db_settings:
            raise NotConfigured
        db = db_settings['db']
        user = db_settings['user']
        passwd = db_settings['passwd']
        host = db_settings['host']
        return cls(db, user, passwd, host)

    def open_spider(self, spider):
        self.conn = MySQLdb.connect(db=self.db,
                               user=self.user, passwd=self.passwd,
                               host=self.host,
                               charset='utf8', use_unicode=True)
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()
        self.spider = spider

    def doesStoreIDExist(self, item):
        try:
            self.spider.logger.debug('Checking  for duplicates')
            value = self.cursor.execute('SELECT count(*) FROM stores WHERE storeID = "' + str(item['storeID']+'"'))
            result = self.cursor.fetchone()
            if result[0] > 0:
                self.spider.logger.debug('StoreID already exists')
                return True
            else:
                return False

        except MySQLdb.Error as e:
            self.spider.logger.debug("Error %d: %s" % (e.args[0], e.args[1]))
            return False

    def process_item(self, item, spider):
        try:
            self.spider.logger.debug('processing item: ')
            if not (self.doesStoreIDExist(item)):
                self.cursor.execute("""INSERT INTO tesco.stores (storeID, storeName, address, telephone)  
                            VALUES (%s, %s, %s, %s)""",
                           (    item['storeID'].encode('utf-8'),
                                item['storeName'].encode('utf-8'),
                                item['address'].encode('utf-8'),
                                item['telephone'].encode('utf-8')
                             )
                           )
        except MySQLdb.Error as e:
            self.logger.debug("Error %d: %s" % (e.args[0], e.args[1]))
        return item

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()