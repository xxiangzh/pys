import scrapy
from scrapy.item import Item, Field


class WeatherItem(Item):
    date = Field()  # 日期（含星期）
    weather = Field()  # 白天天气
    temp = Field()  # 温度
    wind_dir = Field()  # 风向
    wind_level = Field()  # 风力等级
    icon_day = Field()  # 白天图标代码
    icon_night = Field()  # 夜间图标代码


class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['www.weather.com.cn']
    start_url = 'https://www.weather.com.cn/weather/101280604.shtml'

    def start_requests(self):
        yield scrapy.Request(self.start_url, callback=self.parse)

    def parse(self, response):
        # 定位7天天气预报容器
        container = response.css('div#7d.c7d')
        if not container:
            self.logger.error("天气容器未找到")
            return

        # 提取每一天的数据
        for day in container.css('ul.t.clearfix > li'):
            try:
                item = WeatherItem()

                # 处理日期
                date_text = day.css('h1::text').get()
                item['date'] = date_text

                # 处理天气图标（白天和夜间）
                icons = day.css('big[class^="png40"]')
                item['icon_day'] = icons[0].xpath('@class').re_first(r'd(\d+)')
                item['icon_night'] = icons[1].xpath('@class').re_first(r'n(\d+)')

                # 天气状况
                wea = day.css('p.wea')
                item['weather'] = wea.xpath('@title').get()

                # 温度处理
                temp = day.css('p.tem')
                temp_high = temp.css('span::text').get()
                temp_low = temp.css('i::text').get()
                item['temp'] = temp_high + '~' + temp_low

                # 风力处理
                wind = day.css('p.win')
                item['wind_dir'] = self.parse_wind_dir(wind)
                item['wind_level'] = wind.css('i::text').get()

                yield item

            except Exception as e:
                self.logger.error(f"解析失败: {str(e)}")

    def parse_wind_dir(self, wind_element):
        """解析风向（合并两个相同值）"""
        directions = wind_element.css('span[title]::attr(title)').getall()
        return '/'.join(set(directions)) if directions else None

# 运行命令（输出JSON文件）：
# scrapy crawl weather -o weather_data.json
# 输出CSV（自动处理中文）
# scrapy crawl weather -o weather_data.csv
