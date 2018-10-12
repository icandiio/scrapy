import logging

import scrapy

logger = logging.getLogger(__name__)


class V1Spider(scrapy.Spider):
    name = "v1spider"

    start_urls = [
        "http://www.baidu.com",
    ]

    def parse(self, response):
        logger.info("++++++++ %s +++++ %s +++++" % (self.name, response.url))
