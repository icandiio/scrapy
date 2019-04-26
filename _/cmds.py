from scrapy import cmdline

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import task


def v1cmds():
    cmdline.execute('scrapy crawl v1spider'.split())


def looping_call_spider(crawler_process):
    spider_loader = crawler_process.spider_loader
    spider_names = spider_loader.list()
    print(spider_names)
    for spider_name in spider_names:
        crawler_process.crawl(spider_name)


def v2crawler():
    settings = get_project_settings()

    crawler_process = CrawlerProcess(settings)

    _looping = task.LoopingCall(looping_call_spider, crawler_process)
    _looping.start(5)  # call every second

    crawler_process.start(stop_after_crawl=False)


if __name__ == "__main__":
    v1cmds()
    # v2crawler()
