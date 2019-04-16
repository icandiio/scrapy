import logging
import time

from pyx_scrapy_exts.const import Entity, ScrapyItem

import scrapy

logger = logging.getLogger(__name__)


class V1Spider(scrapy.Spider):
    name = "v1spider"

    start_urls = [
        "http://www.baidu.com",
        "http://www.baidu.com",
    ]

    def parse(self, response):
        logger.info("++++++++ %s +++++ %s +++++" % (self.name, response.url))
        yield ScrapyItem.create_item("atest", {Entity.id: 1, "v": time.time()})
