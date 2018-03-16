# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from ..items import DingdianItem
import os


class DingdianSpider(scrapy.Spider):
    name = 'dingdian'
    allowed_domains = ['x23us.com']
    start_urls = ['https://www.x23us.com/']

    # 每个分类的起始页
    def start_requests(self):
        for i in range(1, 11):
            start_url = 'https://www.x23us.com/class/' + str(i) + '_1.html'
            yield Request(url=start_url, callback=self.parse)

    # 获得每个分类的最大页码，加到生成器
    def parse(self, response):
        # print(response.text)
        max_num = response.xpath("//div[@class='pagelink']//a[@class='last']/text()").extract()[0]
        # print(max_num)
        current_url = response.url[:-6]
        # print(current_url)
        for i in range(1, 10):
            url = current_url + str(i) + '.html'
            yield Request(url=url, callback=self.get_title)

    # 获取每个分类页面的 所有书籍名称，url，作者
    def get_title(self, response):
        # print(response.url)
        book_title_list = response.xpath(
            "//tr[@bgcolor='#FFFFFF']//td[position() < 2]//a[position()>1]//text()").extract()
        # print(book_name_list)

        property_list = response.xpath("//tr[@bgcolor='#FFFFFF']//td[position() > 2]/text()").extract()
        # print(property_list)
        author_list = [property_list[a] for a in range(0, len(property_list), 4)]
        # print(author_list)

        book_url_list = response.xpath("//tr[@bgcolor='#FFFFFF']//td[position() < 2]//a[position()>1]/@href").extract()
        # print(book_url_list)

        for title, novelurl, author in zip(book_title_list, book_url_list, author_list):
            # 传给 item 存储
            item = DingdianItem()
            item['title'] = title
            item['author'] = author
            item['novelurl'] = novelurl
            yield item
            yield Request(url=novelurl, callback=self.get_chapter_url)

    # 进到每个小说页面，获取 章节名称，url
    def get_chapter_url(self, response):
        current_url = response.url
        # print(current_url)

        chapter_title_list = response.xpath("//td[@class='L']//a/text()").extract()
        # print(chapter_title_list)

        chapter_url_list = response.xpath("//td[@class='L']//a/@href").extract()
        # print(chapter_url_list)

        for chapter_url, chapter_title in zip(chapter_url_list, chapter_title_list):
            intact_chapter_url = current_url + chapter_url
            # print(intact_chapter_url)

            yield Request(url=intact_chapter_url,callback=self.donwload_content)

    # 下载章节内容
    def donwload_content(self, response):
        print(response.body)
        print("-------------------------开始下载小说--------------------------------------")

        novel_title = response.xpath("//dt//a//text()").extract()[-1]
        print(novel_title)

        chapter_title = response.xpath("//dd//h1/text()").extract()[0]
        print(chapter_title)

        contents = response.xpath("//dd[@id='contents']/text()").extract()
        print(contents)

        path = r'E:\python三阶段\高级爬虫/Spider\note/' + novel_title + '/'

        try:
            os.makedirs(r'E:\python三阶段\高级爬虫/Spider\note/' + novel_title)

            with open(path +chapter_title+'.txt','w',encoding='utf-8')as f:
                for content in contents:
                    f.write(content + '\n')
        except:
            with open(path +chapter_title+'.txt','w',encoding='utf-8')as f:
                for content in contents:
                    f.write(content + '\n')
