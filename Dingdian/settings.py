# -*- coding: utf-8 -*-

# Scrapy settings for Dingdian project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Dingdian'

SPIDER_MODULES = ['Dingdian.spiders']
NEWSPIDER_MODULE = 'Dingdian.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Dingdian (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.7
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'Dingdian.middlewares.DingdianSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'Dingdian.middlewares.DingdianDownloaderMiddleware': 543,
   #  'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':123,
   #  'Dingdian.middlewares.IPPOOLS':125,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':2,
    'Dingdian.middlewares.Uamid':1
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'Dingdian.pipelines.DingdianPipeline': 300,
    'Dingdian.pipelines.DingdianSQLitePipline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# ip 代理池
IPPOOL = [
    {'ipaddr': '115.218.122.24:9000'},
    {'ipaddr': '114.234.80.233:9000'},
    {'ipaddr': '115.223.209.232:9000'},
    {'ipaddr': '115.223.248.103:9000'},
    {'ipaddr': '218.95.51.199:9000'},
    {'ipaddr': '115.223.255.151:9000'},
    {'ipaddr': '115.196.55.215:9000'},
    {'ipaddr': '115.218.218.124:9000'},
    {'ipaddr': '115.223.243.51:9000'},
    {'ipaddr': '117.90.7.126:9000'},
    {'ipaddr': '117.90.6.84:9000'},
    {'ipaddr': '59.62.54.82:9000'},
    {'ipaddr': '115.218.124.104:9000'},
    {'ipaddr': '115.223.209.169:9000'},
    {'ipaddr': '180.118.94.63:9000'},
    {'ipaddr': '117.90.3.243:9000'},
    {'ipaddr': '115.223.200.58:9000'},
    {'ipaddr': '180.118.73.249:9000'},
    {'ipaddr': '115.218.126.170:9000'},
    {'ipaddr': '117.90.1.242:9000'},
    {'ipaddr': '101.68.49.228:9000'},
    {'ipaddr': '121.232.148.49:9000'},
    {'ipaddr': '121.232.146.48:9000'},
    {'ipaddr': '60.214.155.243:53281'},
    {'ipaddr': '182.129.240.168:9000'},
    {'ipaddr': '117.90.3.135:9000'},
    {'ipaddr': '121.232.145.190:9000'},
    {'ipaddr': '182.141.45.10:9000'},
    {'ipaddr': '125.94.0.252:8080'},
    {'ipaddr': '115.223.217.118:9000'},
]

# 用户代理池
UAPOOL = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/58.0',
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
]
