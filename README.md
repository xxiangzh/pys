# pys

安装 Scrapy
pip install scrapy

创建一个爬虫项目
scrapy startproject demo_project

进入该目录，创建一个爬虫
cd demo_project
scrapy genspider demo_spider www.?.com

输出JSON文件
scrapy crawl demo_spider -o demo_data.json

输出CSV文件
scrapy crawl demo_spider -o demo_data.csv
