from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy import log
from bot.items import BotItem


class BotSpider(CrawlSpider):
	name = "careerslip"
	allowed_domains = ["careerslip.com"]
	start_urls = ["http://careerslip.com/find/jobs"]

	rules = (
		#Gets all pagination
		Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="pagination"]/a[@href]'))),

		#Gets all data pages, and parse links for scraping
		Rule(SgmlLinkExtractor(restrict_xpaths=('//ul[@class="listing"]//h3/a[@href]')), callback='parse_page', follow=False),
		)

	def __init__(self, *args, **kwargs):
		self.ref_init = 1
		super(BotSpider, self).__init__(*args, **kwargs)

	def parse_paginate(self, response):
		self.log('Found overviewpage %s' % (response.url), log.INFO)

	def parse_page(self, response):
		sel = Selector(response)
		self.log('Parsing page %s' % (response.url), log.INFO)

		item = BotItem()
		item["job_title"] = self.title(''.join(response.xpath('//div[@class="static_info"]//td[2]/span/text()').extract()).strip())
		item["company_name"] = ''.join(response.xpath('//div[@class="static_info"]//td[2]/a/strong/text()').extract())
		item["job_level"] = ""#''.join()
		item["industry"] = ''.join(response.xpath('//table[@cellpadding="3"]//td[2]/text()').extract())
		item["specialization"] = ''.join(response.xpath('//table[@cellpadding="3"]//td[4]/text()').extract())
		item["location"] = self.location(''.join(response.xpath('//div[@class="static_info"]//td[2]/span/text()').extract()).strip())
		item["employment_type"] = ''.join(response.xpath('//table[@cellpadding="3"]//td[10]/text()').extract())
		item["experience"] = ''.join(response.xpath('//table[@cellpadding="3"]//td[8]/text()').extract())
		item["description"] = ''.join(response.xpath('//div[@class="wideinfo userInfo"]//span/text() |'
			'//div[@class="wideinfo userInfo"]//p/text()').extract())
		item["source"] = "Careerslip"
		item["requirement"] = ''.join(response.xpath('//table[@cellpadding="3"]//td[6]/text()').extract())
		item["salary"] = ''.join(self.salary(response.xpath('//div[@class="one_params"][span[@class="label salary"]]/strong/text()').extract()))
		item["url"] = response.url
		self.ref_init += 1

		return item

	def title(self, item):
		if ' in ' in item:
			name = item.split(' in ')[0]
			return name
		else:
			return item

	def location(self, item):
		if ' in ' in item:
			location = item.split(' in ')[1]
			return location.strip(',')
		else:
			return item

	def salary(self, item):
		if not item:
			return 'Competitive'
		else:
			return item