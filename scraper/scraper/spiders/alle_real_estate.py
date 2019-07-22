# -*- coding: utf-8 -*-
import scrapy
from pprint import pprint

class AlleRealEstateSpider(scrapy.Spider):
    name = 'alle-real-estate'
    allowed_domains = ['alleghenycounty.us']
    start_urls = ['http://www2.alleghenycounty.us/RealEstate/search.aspx']

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
                                         formdata={
                                            'ddlMuniCode':'1',
                                            'txtStreetNum': '1903',
                                            'txtStreetName': 'BUENA VISTA',
                                            'radio1': 'Address'
                                         },
                                         callback=self.parse_parcel)
                                        
    def parse_parcel(self, response):
        pprint(response.body)
