from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from tq2.spiders.weather import WeatherSpider

if __name__ == "__main__":
    # 获取项目默认配置
    settings = get_project_settings()

    # 创建 CrawlerProcess 实例，并传递配置
    process = CrawlerProcess(settings)

    # 添加要运行的爬虫（通过名称或直接传递 Spider 类）
    process.crawl(WeatherSpider)

    # 启动爬虫（这会阻塞直到所有任务完成）
    process.start()
