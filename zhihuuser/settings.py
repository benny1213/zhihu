# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https:   //docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_TIMEOUT = 200

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7,zh-TW;q=0.6',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',

  # ':authority': 'www.zhihu.com',
  # ':method': 'GET',
  # ':path': '/api/v4/members/excited-vczh/followers?include=data%5B*%5D.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge%5B%253F(type=best_answerer)%5D.topics&offset=0&limit=20',
  # ':scheme': 'https',
  # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
  # 'accept-encoding': 'gzip, deflate, br',
  # 'accept-language': 'en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7,zh-TW;q=0.6',
  # 'cache-control': 'max-age=0',
  # 'cookie': '_zap=6d99c222-e392-47ed-9f9a-b031494cd8be; _xsrf=6f0be6ef-49b8-4d1a-8ebf-4a2630997dc8; d_c0="ACAjvorgvw-PTt8NkTNM71XxYfplNOWVffg=|1563354693"; capsion_ticket="2|1:0|10:1564299204|14:capsion_ticket|44:OGUwOTMyNDdhODM0NDAwODg4YTI1NWM4ZTVlOWI0MWY=|6b8f5d61ab23b74a8fe7b34f0083eff037429f31abb05242813099c54f380641"; z_c0="2|1:0|10:1564299207|4:z_c0|92:Mi4xWWVJSEF3QUFBQUFBSUNPLWl1Q19EeVlBQUFCZ0FsVk54NTBxWGdEQmZMZ011eERpMWZ1NVQwSEo4am5Wdi1lU2hR|0fcce5fa703e01d9df3142244b7d2237aa867b75364ebf00dc9d0a768c3b02cb"; tst=r; q_c1=819eff922c094c02aa563a6975d2bda1|1564589123000|1564589123000; __utma=51854390.500332031.1565343799.1565343799.1565343799.1; __utmc=51854390; __utmz=51854390.1565343799.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/bug-bunny/following/collections; __utmv=51854390.100-1|2=registration_date=20160514=1^3=entry_date=20160514=1; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c',
  # 'dnt': '1',
  # 'sec-fetch-mode': 'navigate',
  # 'sec-fetch-site': 'none',
  # 'sec-fetch-user': '?1',
  # 'upgrade-insecure-requests': '1',
  # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'zhihuuser.middlewares.ZhihuuserDownloaderMiddleware': 100,
   'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware':5,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihuuser.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGO_URI = 'localhost'
MONGO_DATABASE = 'zhihu'