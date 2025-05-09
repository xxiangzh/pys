import scrapy
import re

class DoubanMovieItem(scrapy.Item):
    title = scrapy.Field()
    info = scrapy.Field()

class DoubanTop250Spider(scrapy.Spider):
    name = 'douban_top250'
    start_urls = ['https://movie.douban.com/top250']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'douban_top250.csv',
        'FEED_EXPORT_FIELDS': ['title', 'info'],
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...',
        'DOWNLOAD_DELAY': 2
    }

    def parse(self, response):
        for movie in response.css('ol.grid_view li'):
            item = DoubanMovieItem()

            # 提取标题
            item['title'] = movie.css('.title::text').get().strip()

            # 提取信息部分
            info_section = movie.css('.bd p')

            # 使用XPath分割<br>后的内容
            raw_info = info_section.xpath('.//text()').extract()
            info_line = ''.join(raw_info).split('主演:')[-1].split('<br>')[-1].strip()

            # 清洗并分割信息
            clean_info = re.sub(r'\s+', ' ', info_line)  # 合并多个空格
            clean_info = clean_info.replace('&nbsp;', ' ')  # 处理HTML实体
            item['info'] = clean_info

            yield item

        # 分页处理
        next_page = response.css('span.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
