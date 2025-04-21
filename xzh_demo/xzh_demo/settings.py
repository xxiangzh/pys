# Scrapy settings for xzh_demo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# 定义项目名称，用于标识爬虫（例如在日志或统计中）。
BOT_NAME = "xzh_demo"

# 指定存放爬虫代码的模块路径。
SPIDER_MODULES = ["xzh_demo.spiders"]
# 指定 scrapy genspider 命令生成新爬虫时的默认路径。
NEWSPIDER_MODULE = "xzh_demo.spiders"


# 定义请求头中的 User-Agent，用于标识爬虫身份。
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# 是否遵守目标网站的 robots.txt 规则。默认值：False
# ROBOTSTXT_OBEY = True

# 全局最大并发请求数。默认值：16
#CONCURRENT_REQUESTS = 32

# 网站下载延迟（秒），用于控制爬取速度。默认值：0（无延迟）
DOWNLOAD_DELAY = 1
# 限制对同一域名的并发请求数。默认值：16
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 限制对同一 IP 地址的并发请求数。默认值：16
#CONCURRENT_REQUESTS_PER_IP = 16

# 是否启用 Cookies。默认值：True（启用）
#COOKIES_ENABLED = False

# 是否禁用 Telnet 控制台。默认值：True（启用）
#TELNETCONSOLE_ENABLED = False

# 覆盖默认请求头
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# 启用或配置爬虫中间件（例如代理、重试逻辑）。默认值：未设置时，Scrapy 使用内置中间件（如 UserAgentMiddleware、RetryMiddleware）
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "xzh_demo.middlewares.XzhTestSpiderMiddleware": 543,
#}

# 启用或配置下载器中间件（例如代理、重试逻辑）。默认值：未设置时，Scrapy 使用内置中间件（如 UserAgentMiddleware、RetryMiddleware）
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "xzh_demo.middlewares.XzhTestDownloaderMiddleware": 543,
#}

# 启用或禁用扩展
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# 定义数据处理管道（如数据清洗、存储到数据库）。默认值：未设置时，不启用任何管道
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "xzh_demo.pipelines.XzhTestPipeline": 300,
#}

# 启用自动限速扩展，根据服务器负载动态调整请求频率。默认值：False（关闭）
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# 初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# 在高延迟的情况下要设置的最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
# Scrapy 应该并行发送到每个服务器的平均请求数
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# 启用显示收到的每个响应的限制统计信息
#AUTOTHROTTLE_DEBUG = False

# 启用 HTTP 缓存，避免重复下载相同页面。默认值：False（关闭）
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# 指定 Twisted 框架的事件循环实现（如 asyncio）。
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# 导出数据文件（如 JSON、CSV）的编码格式。默认值：utf-8。
FEED_EXPORT_ENCODING = "utf-8"
