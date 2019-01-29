import scrapy
from newspaper import Article


class TheHindu(scrapy.Spider):
    name = "toi_scrapper"

    def start_requests(self):
        urls = []

        for i in range(84):
            urls.append(f'https://timesofindia.indiatimes.com/searchresult.cms?sortorder=score_artdate&searchtype=2&maxrow=10&startdate=2001-01-01&enddate=2001-01-14&article=2&pagenumber={i + 1}&isphrase=no&query=hiv&searchfield=&section=&kdaterange=1500&date1mm=01&date1dd=01&date1yyyy=2001&date2mm=01&date2dd=14&date2yyyy=2001')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        href = response.xpath('//div[@class="maintable12"]/div/div/a/@href').extract()

        for url in href:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_article)

    def parse_article(self, response):
        article = Article(response.url)
        article.download()
        article.parse()
        text = article.text
        title = article.title
        date = response.xpath('//time/@datetime').extract()[0][:10] 
        location = article.text.split(':')[0] 
        category = response.xpath('//div[@class="container"]/ul/li/a/span/text()').extract()
        
        yield {'name': title, 'date': date, 'location': location, 'category': category,'body': text}