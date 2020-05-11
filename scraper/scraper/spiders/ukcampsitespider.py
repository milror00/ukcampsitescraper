# -*- coding: utf-8 -*
import scrapy
from ukpostcodeutils import validation
from scraper.scraper.websiteHelper import websiteHelper


class UKCampsiteSpider(scrapy.Spider):
    name = 'ukcampsite'
    allowed_domains = ['ukcampsite.co.uk']
    start_urls = []
    start = 0
    end = 0

    def __init__(self):
        super(UKCampsiteSpider, self)
        self.logger.debug('Start: ' + str(self.start))
        self.logger.debug('End: ' + str(self.end))
        self.logger.debug("ukcampsite spider initialised")

    @classmethod
    def setInitialVariables(cls, start, end):
        cls.start = start
        cls.end = end

    def start_requests(self):
        self.logger.debug('ukcampsite spider start_requests function')
        for i in range(int(self.start), int(self.end)):
            url = 'http://www.ukcampsite.co.uk/sites/details.asp?revid=%s' % str(i)
            self.logger.debug('Spider requesting : %s', url)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        for site_response in response.css('body'):

            addressExtract = websiteHelper.splice(response.text,
                                  'heading4',
                                  'See Weather Forecast')
            postcode = websiteHelper.extractPostcodeFromString(addressExtract)
            telephone = websiteHelper.extractTelephoneFromString(addressExtract)
            siteName = websiteHelper.extractSiteNameFromString(addressExtract)
            if siteName == '':
                 return
        yield {
            'siteName': siteName,
            'postcode': postcode,
            'telephone': telephone,
        }
        
