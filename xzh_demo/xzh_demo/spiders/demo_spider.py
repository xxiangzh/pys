import json

import scrapy


class DemoSpiderSpider(scrapy.Spider):
    name = 'demo_spider'

    def start_requests(self):
        # 接口地址
        url = "http://localhost:8596/bop-oms/pay/query"

        # 构造json格式请求参数
        payload = {"data": {"serialNo": "123"}}

        # 发送POST请求
        yield scrapy.Request(
            url=url,
            method='POST',
            body=json.dumps(payload),
            headers={'Content-Type': 'application/json'},
            callback=self.parse_response
        )

    def parse_response(self, response):
        # 直接输出json格式的响应结果
        # 执行命令输出文件：scrapy crawl demo_spider -o demo_spider.json
        yield response.json()
