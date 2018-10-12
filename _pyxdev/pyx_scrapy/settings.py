# -*- coding: utf-8 -*-

BOT_NAME = 'pyx_scrapy'

SPIDER_MODULES = ['pyx_scrapy.spiders.tutor']

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
SCHEDULER = 'pyx_scrapy_exts.scheduler.redis.scheduler.RedisScheduler'
SCHEDULER_QUEUE_CLASS = 'pyx_scrapy_exts.scheduler.redis.queue.PriorityQueue'
DUPEFILTER_CLASS = 'pyx_scrapy_exts.scheduler.dupefilter.RedisDupeFilter'

# CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS = 16

DOWNLOADER_MIDDLEWARES = {
    'pyx_scrapy_exts.downloadermiddlewares.useragent.RandomUserAgentMiddleware': 550,
    'pyx_scrapy_exts.downloadermiddlewares.referer.RefererMiddleware': 1000,
    'pyx_scrapy_exts.downloadermiddlewares.headers.HeadersMiddleware': 2000,
    # 'pyx_scrapy_exts.downloadermiddlewares.threshold.ThresholdErrorMiddleware': 9999,
    # replace by self define,not use both
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'pyx_scrapy_exts.downloadermiddlewares.proxypool.ProxyPoolMiddleware': 600,
}

# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

MONGODB_URI = 'mongodb://tk/scrapy'
MONGODB_DB = 'scrapy'
ITEM_PIPELINES = {
    # 'pyscrapy.pipelines.mongo.MongoPipeline': 300,
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
