from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from db.spiders.douban_spider import DoubanTop250Spider

'''
1.在settings.py加配置 
FEEDS = {
    # 导出到当前目录的 output 文件夹下的 csv 文件
    "output/%(name)s_%(time)s.csv": {
        "format": "csv",           # 导出格式（json, csv, xml 等）
        "encoding": "utf-8-sig",   # 编码（兼容excel）
        "overwrite": True,         # 如果文件存在则覆盖
        "store_empty": False,      # 不导出空数据
        "item_export_kwargs": {
            "export_empty_fields": True,  # 导出所有字段（包括空值）
        },
    },
}
2.执行此main方法，可直接运行爬虫脚本
'''
if __name__ == "__main__":
    # 创建 CrawlerProcess 实例，并传递默认配置
    process = CrawlerProcess(get_project_settings())
    # 添加要运行的爬虫（通过名称或直接传递 Spider 类）
    process.crawl(DoubanTop250Spider)
    # 启动爬虫（这会阻塞直到所有任务完成）
    process.start()
