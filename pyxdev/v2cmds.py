from scrapy.crawler import CrawlerProcess
from scrapy.spiderloader import SpiderLoader
from scrapy.utils.project import get_project_settings


def multi_crawler():
    """
    no useful ,just last add spider running
    """
    settings = get_project_settings()
    crawler_process = CrawlerProcess(settings)
    spider_loader = SpiderLoader(settings)
    spider_names = spider_loader.list()
    for spider_name in spider_names:
        crawler_process.crawl(spider_name)

    crawler_process.start()


if __name__ == '__main__':
    multi_crawler()
