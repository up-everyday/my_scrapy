import scrapy
from ImageSpider.items import ImageSpiderItem
class ImgspiderSpider(scrapy.Spider):
    name = 'ImgSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = ImageSpiderItem()  # 实例化item
        imgurls = response.css(".post img::attr(src)").extract() # 注意这里是一个集合也就是多张图片
        item['image_urls'] = imgurls
        self.logger.warning('xxxxx image_url is  %s' % imgurls)
        yield item
        pass