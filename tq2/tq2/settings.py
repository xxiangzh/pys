# Scrapy settings for tq2 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "tq2"

SPIDER_MODULES = ["tq2.spiders"]
NEWSPIDER_MODULE = "tq2.spiders"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# 添加BOM头的UTF-8，防止excel打开乱码
FEED_EXPORT_ENCODING = "utf-8-sig"

# 添加此配置，可直接运行run_spider.py导出文件
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
    # 可以添加更多导出目标
    # "output/%(name)s_%(time)s.json": {
    #     "format": "json",          # 导出格式（json, csv, xml 等）
    #     "encoding": "utf-8",       # 编码（避免中文乱码）
    #     "overwrite": True,         # 如果文件存在则覆盖
    #     "store_empty": False,      # 不导出空数据
    #     "item_export_kwargs": {
    #         "export_empty_fields": True,  # 导出所有字段（包括空值）
    #     },
    # },
}
