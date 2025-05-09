import scrapy
import re
from scrapy.exceptions import CloseSpider


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    start_urls = ['https://piaofang.maoyan.com/rankings/year']

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'FEED_EXPORT_ENCODING': 'utf-8-sig',
        'DUPEFILTER_DEBUG': True
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                headers=self.headers,
                callback=self.parse,
                errback=self.err_handler  # 错误回调
            )

    def parse(self, response):
        movies = response.css('ul.row')
        for movie in movies:
            try:
                item = self.process_item(movie)
                if item:  # 只返回有效数据
                    yield item
            except Exception as e:
                self.logger.error(f"处理条目失败: {str(e)}")

    def process_item(self, selector):
        """独立封装数据处理逻辑"""
        title = selector.css('.first-line::text').get('').strip()
        date_str = selector.css('.second-line::text').get('').strip()
        date_str = date_str.replace('上映', '')
        return {
            'title': title,
            'year': date_str
        }

    def err_handler(self, failure):
        """错误处理回调"""
        self.logger.error(repr(failure))
