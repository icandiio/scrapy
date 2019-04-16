# coding:utf-8

import logging

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders.crawl import Rule

logger = logging.getLogger(__name__)


class V1Crawler(CrawlSpider):
    name = "v1crawler"

    custom_settings = {
    }

    allowed_domains = [
        'news.baidu.com'
    ]

    start_urls = [
        'http://news.baidu.com'
    ]

    rules = (
        Rule(LinkExtractor(), callback='parse_rsp'),
    )

    @classmethod
    def schedule_runner(cls):
        print("++++++++++++++++++++++")

    # do not override parse method
    def parse_rsp(self, response):
        logger.info("+++++ %s +++++" % response.url)
        """
        xpath,css {list data},if just meta data ,ItemLoader is better,mapper the item properties
        if json str,json.loads(response.text)
        """
