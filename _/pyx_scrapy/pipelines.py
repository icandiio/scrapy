# coding:utf-8

import logging

from pymongo import MongoClient
from pyx_gutils.util import datetime_util
from pyx_scrapy_exts.const import Entity, ItemK
from twisted.internet.defer import inlineCallbacks
from txmongo.connection import ConnectionPool

logger = logging.getLogger(__name__)


class AsyncMongoPipeline(object):
    def __init__(self, crawler):
        self.crawler = crawler
        mongo_uri = self.crawler.settings.get('MONGODB_URI', 'mongodb://localhost')
        db_name = self.crawler.settings.get('MONGODB_DB', 'scrapy_mongo_pipeline')
        self.ctx = ConnectionPool(mongo_uri)
        self.db = self.ctx[db_name]

    @classmethod
    def from_crawler(cls, crawler):
        pipe = cls(crawler)
        return pipe

    def process_item(self, item, spider):
        if ItemK.DATA not in item or Entity.id not in item[ItemK.DATA] or item[ItemK.DATA].get(Entity.id) is None:
            logger.error(item)
            return
        dset = item[ItemK.DSET]
        data = item[ItemK.DATA]
        self._insert_or_update(dset, data)
        return item

    @inlineCallbacks
    def _insert_or_update(self, dset, data):
        dset_cli = self.db[dset]

        primary_key = data.get(Entity.id)
        query_builder = {Entity.id: primary_key}
        update_builder = {'$set': {}, '$setOnInsert': {}}

        utime = datetime_util.get_long_time()

        for k, v in data.items():
            update_builder['$set'][k] = v

        update_builder['$setOnInsert'][Entity.ctime] = utime
        update_builder['$set'][Entity.utime] = utime

        result = yield dset_cli.update_one(query_builder, update_builder, upsert=True)
        logger.info('ack is: %s, matched_count is: %s, modified_count is: %s, upserted_id is: %s' %
                    (result.acknowledged, result.matched_count, result.modified_count, result.upserted_id))


class MongoPipeline(object):
    def __init__(self, mongo_uri, db):
        client = MongoClient(mongo_uri)
        self.db = client[db]

    @classmethod
    def from_crawler(cls, crawler):
        mongo_uri = crawler.settings.get('MONGODB_URI', 'mongodb://localhost')
        db = crawler.settings.get('MONGODB_DB', 'scrapy_mongo_pipeline')
        pipe = cls(mongo_uri, db)
        return pipe

    def process_item(self, item, spider):
        if ItemK.DATA not in item or Entity.id not in item[ItemK.DATA] or item[ItemK.DATA].get(Entity.id) is None:
            logger.error(item)
            return
        dset = item[ItemK.DSET]
        data = item[ItemK.DATA]
        self._insert_or_update(dset, data)
        return item

    def _insert_or_update(self, dset, data):
        dset_cli = self.db[dset]

        primary_key = data.get(Entity.id)

        query_builder = {Entity.id: primary_key}
        update_builder = {'$set': {}, '$setOnInsert': {}}

        utime = datetime_util.get_long_time()

        for k, v in data.items():
            update_builder['$set'][k] = v

        update_builder['$setOnInsert'][Entity.ctime] = utime
        update_builder['$set'][Entity.utime] = utime

        dset_cli.update_one(query_builder, update_builder, upsert=True)
