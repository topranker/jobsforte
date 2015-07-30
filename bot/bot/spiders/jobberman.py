from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy import log
from bot.items import BotItem

from urlparse import urljoin


class BotSpider(CrawlSpider):
	name = "jobberman"
	download_delay = 0.5
	allowed_domains = ["jobberman.com"]
	start_urls = ["http://www.jobberman.com/"]

	rules = (
		#Gets all city links from start_urls
		Rule(SgmlLinkExtractor(restrict_xpaths=('//ul[@class="location-tab clearfix"]/li/a[@href]'))),
		#Gets all pagination
		#Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@id="pagination"]//li/a[@href]'))),
		#Gets all data pages, and parse links for scraping
		#Rule(SgmlLinkExtractor(restrict_xpaths=('//p[@class="job-title"]/a[@href]')), callback='parse_page', follow=False),
		#Gets all jobs link posted as "Today"
		Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@id="pagination"]//li/a[@href]')), callback='parse_today', follow=True),
		)

	def __init__(self, *args, **kwargs):
		self.ref_init = 1
		super(BotSpider, self).__init__(*args, **kwargs)

		# allow 'scrapy crawl -a starturl=http://job.naij.com/city-Lagos-jobs-2-22'
		# for testing
		if not not kwargs.get('starturl'):
			self.start_urls = [kwargs.get('starturl')]
	
	def parse_paginate(self, response):
		self.log('Found overviewpage %s' % (response.url), log.INFO)
	

	def parse_today(self, response):
		self.log('Found overviewpage %s' % (response.url), log.INFO)
		links = response.xpath('//div[@class="search-details-top clearfix"][div/p[contains(.,"Today")]]//p[@class="job-title"]/a/@href').extract()
		for link in links:
			#link = urljoin(response.url, link) # make absolute
			self.log('Found new jobpage: %s' % (link), log.INFO)
			yield Request(link, callback=self.parse_page)
		

	def parse_page(self, response):
		self.log('Parsing page %s' % (response.url), log.INFO)
		item = BotItem()
		item["title"] = ''.join(response.xpath('//div[@class="job-quick-sum"]/h1/text()').extract())
		item["organisation"] = ''.join(response.xpath('//p[@class="job-details-sum-subhead"][1]/a/text()').extract())
		item["level"] = ''.join(response.xpath('//p[@class="job-details-sum-subhead"][2]/a/text()').extract())
		item["industry"] = ""
		item["specialization"] = ''.join(response.xpath('//p[@class="job-details-sum-subhead"][4]/a/text()').extract())
		item["location"] = ''.join(response.xpath('//p[@class="job-details-sum-subhead"][3]/a/text()').extract())
		item["employment_type"] = ''.join(response.xpath('//p[@class="job-details-sum-subhead"][5]/a/text()').extract())
		item["experience"] = ''.join(response.xpath('//p[@class="job-details-sum-subhead"][7]/a/text()').extract())
		item["description"] = ''.join(response.xpath('//div[@class="job-details-main"]//span//text()').extract())
		item["source"] = "Jobberman"
		item["requirement"] = ''.join(response.xpath('//p[@class="job-details-sum-subhead"][6]/a/text()').extract())
		item["salary"] = ''.join(self.salary(response.xpath('//p[@class="job-details-sum-subhead"][8]/a/text()').extract()))
		item["url"] = response.url

		return item

	def salary(self, item):
		if not item:
			return 'Competitive'
		else:
			return item
