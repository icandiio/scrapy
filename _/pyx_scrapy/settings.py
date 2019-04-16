# -*- coding: utf-8 -*-

BOT_NAME = 'pyx_scrapy'

SPIDER_MODULES = ['pyx_scrapy.spiders']

NEWSPIDER_MODULE = 'pyx_scrapy.spiders'

ROBOTSTXT_OBEY = False

COMMANDS_MODULE = 'pyx_scrapy_exts.commands'
#
REDIS_CONFIG = {
    "host": "tk",
    "port": 6379,
    "decode_responses": True,
    # "password": "deliex-rds"
}

# 爬取的调度器
# SCHEDULER = 'pyx_scrapy_exts.scheduler.scheduler.Scheduler'
# SCHEDULER_QUEUE_CLASS = 'pyx_scrapy_exts.scheduler.queue.PriorityQueue2Redis'
# SCHEDULER_DUPEFILTER_CLASS = 'pyx_scrapy_exts.scheduler.dupefilter.DupeFilter2Redis'

# CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS = 16

# headers => dict.setdefault() 只有首次有效，再设置无覆盖效果
DOWNLOADER_MIDDLEWARES = {
    'pyx_scrapy_exts.downloadermiddlewares.referer.RefererMiddleware': 1000,
    'pyx_scrapy_exts.downloadermiddlewares.headers.HeadersMiddleware': 2000,
    # 'pyx_scrapy_exts.downloadermiddlewares.threshold.ThresholdErrorMiddleware': 9999,
    # replace by self define,禁用必须设置为None
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'pyx_scrapy_exts.downloadermiddlewares.useragent.RandomUserAgentMiddleware': 500,
    # 'pyx_scrapy_exts.downloadermiddlewares.proxypool.ProxyPoolMiddleware': 600,
}

# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# MONGODB_URI = 'mongodb://tk:27017/scrapy'
MONGODB_URI = 'mongodb://spider:spiderpass@192.168.1.231:27500/mzk_spiders'
# MONGODB_DB = 'scrapy'
MONGODB_DB = 'mzk_spiders'
ITEM_PIPELINES = {
    # 'pyx_scrapy.pipelines.AsyncMongoPipeline': 300,
}

REDIRECT_ENABLED = True

# LOG_FILE = 'app.log'
LOG_LEVEL = 'DEBUG'

SAVE_FILE_PATH = "/home/imake/data"

CLOSE_IF_IDLE = True

# 代理配置
# 代理池
# PROXY_POOL_URL = 'http://imake:1314'
# 是否开启代理
# PROXY_ENABLE = True
# 指定代理地址
PROXY_URL = 'http://imake:1314'
