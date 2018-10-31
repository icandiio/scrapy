from scrapy import cmdline

from scrapy.crawler import CrawlerProcess
from scrapy.spiderloader import SpiderLoader
from scrapy.utils.project import get_project_settings


def v1cmds():
    cmdline.execute('scrapy crawl v1spider'.split())


def v2crawler():
    settings = get_project_settings()
    spider_loader = SpiderLoader(settings)
    spider_names = spider_loader.list()

    crawler_process = CrawlerProcess(settings)
    for spider_name in spider_names:
        crawler_process.crawl(spider_name)

    crawler_process.start()


if __name__ == "__main__":
    v1cmds()
    pass
