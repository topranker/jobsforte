from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy import log
from bot.items import BotItem

from urlparse import urljoin


class BotSpider(CrawlSpider):
	name = "naij"
	allowed_domains = ["job.naij.com"]
	start_urls = ["http://job.naij.com/city"]

	rules = (
		#Gets all city links from start_urls
		Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="lists_natures"]//li/a[@href]'))),
		#Gets all pagination
		#Rule(SgmlLinkExtractor(restrict_xpaths=('//ul[@class="pagination"]//li/a[@href]'))),
		#Gets all data pages, and parse links for scraping
		#Rule(SgmlLinkExtractor(restrict_xpaths=('//p[@class="p_title"]//a[@href]')), callback='parse_page', follow=False),
		#For Jobs posted today
		Rule(SgmlLinkExtractor(restrict_xpaths=('//ul[@class="pagination"]//li/a[@href]')), callback='parse_today', follow=True),
		)
	
	def parse_paginate(self, response):
		self.log('Found overviewpage %s' % (response.url), log.INFO)
	

	def parse_today(self, response):
		domain = "http://job.naij.com/"
		self.log('Found overviewpage %s' % (response.url), log.INFO)
		links = response.xpath('//td[@class="title_or_other"][p[contains(.,"Today")]]/p[@class="p_title"]//a/@href').extract()
		for link in links:
			link = urljoin(domain, link) # make absolute
			self.log('Found new jobpage: %s' % (link), log.INFO)
			request = Request(link, callback=self.parse_page)
			yield request
		

	def parse_page(self, response):
		self.log('Parsing page %s' % (response.url), log.INFO)
		item = BotItem()
		item["job_title"] = ''.join(response.xpath('//h1[@itemprop="title"]/text()').extract())
		item["company_name"] = ''.join(response.xpath('//span[@itemprop="name"]/a/text()').extract())
		item["job_level"] = ""# use ''.join() to remove [] from output. 
		item["industry"] = ""
		item["specialization"] = ""
		item["location"] = ''.join(response.xpath('//span[@itemprop="address"]/span/text()').extract()).strip()
		item["employment_type"] = ''.join(response.xpath('//span[@itemprop="employmentType"]/text()').extract()).strip()
		item["experience"] = ''.join(response.xpath('//div[@class="one_params"][span[@class="label experience"]]/strong/text()').extract()).strip()
		item["description"] = ''.join(response.xpath('//div[@itemprop="experienceRequirements"]/ul[1]/li/text()').extract())
		item["source"] = "Naij"
		item["requirement"] = ''.join(response.xpath('//div[@itemprop="experienceRequirements"]/ul[2]/li/text()').extract())
		item["salary"] = ''.join(response.xpath('//div[@class="one_params"][span[@class="label salary"]]/strong/text()').extract()).strip()
		item["url"] = response.url

		return item

