import scrapy
from newspaper import Article


class TheHindu(scrapy.Spider):
    name = "hindu_scrapper"

    def start_requests(self):
        urls = []

        for i in range(1358):
            urls.append(f'https://www.thehindu.com/search/?q=hiv&order=DESC&sort=publishdate&page={i + 1}')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        href = response.xpath('//section/div/div/div/div/a/@href').extract()
        for url in href:
            yield scrapy.Request(url=url, callback=self.parse_article)

    def parse_article(self, response):
        article = Article(response.url)
        article.download()
        article.parse()
        date = response.xpath("//none/text()").extract()[0]
        date = date.strip()[:-10]
        location = response.xpath('//a[@class="section-name"]/text()').extract()[0].strip()
        category = response.xpath('//ul[@class="breadcrumb"]/li/a/span/text()').extract()
        try:
            author = response.xpath('//a[@class="auth-nm lnk"]/text()').extract()[0].strip()
        except:
            author = None
        text = article.text
        title = article.title
        yield {'name': title, 'date': date, 'location': location, 'category': category, 'author': author ,'body': text}