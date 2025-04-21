import scrapy


class DemoSpiderSpider(scrapy.Spider):
    name = "demo_spider"
    allowed_domains = ["localhost"]
    start_urls = ["https://localhost"]

    def parse(self, response):
        pass
