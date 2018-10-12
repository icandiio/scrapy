# coding:utf-8

import logging

from pymongo import MongoClient
from pyx_gutils.util import datetime_util
from pyx_scrapy_exts.const import Entity, ItemK

logger = logging.getLogger(__name__)


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
        dset_cli = self.db[dset]
        self._insert_or_update(dset_cli, data)
        return item

    def _insert_or_update(self, dset_cli, data):
        primary_key = data.get(Entity.id)

        query_builder = {Entity.id: primary_key}
        update_builder = {'$set': {}, '$setOnInsert': {}}

        utime = datetime_util.get_long_time()

        for k, v in data.items():
            update_builder['$set'][k] = v

        update_builder['$setOnInsert'][Entity.ctime] = utime
        update_builder['$set'][Entity.utime] = utime

        dset_cli.update_one(query_builder, update_builder, upsert=True)
