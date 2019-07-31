# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from pprint import pprint
from scraper.items import Parcel, Building, PreviousOwner, PreviousTaxBill
import pandas as pd
import time

class AlleRealEstateSpider(scrapy.Spider):
    name = 'alle-real-estate'
    allowed_domains = ['alleghenycounty.us']
    start_urls = ['http://www2.alleghenycounty.us/RealEstate/search.aspx']

    def parse(self, response):
        df_address_points = pd.read_parquet('../data/address_points.parquet')
        for _, row in df_address_points.iterrows():
            yield scrapy.FormRequest.from_response(response,
                                                    formdata={
                                                        'ddlMuniCode': row['PortalMunicipalityCode'],
                                                        'txtStreetNum': row['ADDR_NUM'],
                                                        'txtStreetName': row['ST_NAME'],
                                                        'radio1': 'Address'
                                                    },
                                                    callback=self.parse_parcel)

    def parse_parcel(self, response):
        loader = ItemLoader(item=Parcel(), response=response)
        loader.add_xpath(
            'parcel_id', '//span[@id="BasicInfo1_lblParcelID"]/text()')
        loader.add_xpath('property_address',
                         '//span[@id="BasicInfo1_lblAddress"]/text()')
        loader.add_xpath(
            'municipality', '//span[@id="BasicInfo1_lblMuni"]/text()')
        loader.add_xpath(
            'owner_name', '//span[@id="BasicInfo1_lblOwner"]/text()')
        loader.add_xpath('school_district', '//span[@id="lblSchool"]/text()')
        loader.add_xpath('neighborhood_code',
                         '//span[@id="lblNeighbor"]/text()')
        loader.add_xpath('tax_code', '//span[@id="lblTax"]/text()')
        loader.add_xpath('owner_code', '//span[@id="lblOwnerCode"]/text()')
        loader.add_xpath('zoning_class', '//span[@id="lblState"]/text()')
        loader.add_xpath('recording_date', '//span[@id="lblRecDate"]/text()')
        loader.add_xpath('use_code', '//span[@id="lblUse"]/text()')
        loader.add_xpath('sale_date',
                         '//span[@id="lblSaleDate"]/text()')
        loader.add_xpath('homestead',
                         '//span[@id="lblHomestead"]/text()')
        loader.add_xpath('sale_price',
                         '//span[@id="lblSalePrice"]/text()')
        loader.add_xpath('farmstead',
                         '//span[@id="lblFarmstead"]/text()')
        loader.add_xpath('deed_book',
                         '//span[@id="lblDeedBook"]/text()')
        loader.add_xpath('clean_green',
                         '//span[@id="lblCleanGreen"]/text()')
        loader.add_xpath('deed_page',
                         '//span[@id="lblDeedPage"]/text()')
        loader.add_xpath('abatement', '//span[@id="lblAbatement"]/text()')
        loader.add_xpath('lot_area', '//span[@id="lblLot"]/text()')
        loader.add_xpath('cy_market_land_value',
                         '//span[@id="lblFullLand"]/text()')
        loader.add_xpath('cy_assessed_land_value',
                         '//span[@id="lblCountyLand"]/text()')
        loader.add_xpath('cy_market_building_value',
                         '//span[@id="lblFullBuild"]/text()')
        loader.add_xpath('cy_assessed_building_value',
                         '//span[@id="lblCountyBuild"]/text()')
        loader.add_xpath('cy_assessed_total_value',
                         '//span[@id="lblFullTot"]/text()')
        loader.add_xpath('cy_market_total_value',
                         '//span[@id="lblCountyTot"]/text()')
        loader.add_xpath('py_market_land_value',
                         '//span[@id="lblFullLand"]/text()')
        loader.add_xpath('py_assessed_land_value',
                         '//span[@id="lblCountyLand"]/text()')
        loader.add_xpath('py_market_building_value',
                         '//span[@id="lblFullBuild"]/text()')
        loader.add_xpath('py_assessed_building_value',
                         '//span[@id="lblCountyBuild"]/text()')
        loader.add_xpath('py_assessed_total_value',
                         '//span[@id="lblFullTot"]/text()')
        loader.add_xpath('py_market_total_value',
                         '//span[@id="lblCountyTot"]/text()')
        loader.add_xpath('owner_mailing',
                         '//span[@id="lblChangeMail"]/text()')

        yield loader.load_item()

        building_info_url = response.url.replace("GeneralInfo", "Building")
        yield scrapy.Request(building_info_url, callback=self.parse_building_info, method='GET')

        building_info_url = response.url.replace("GeneralInfo", "Sales")
        yield scrapy.Request(building_info_url, callback=self.parse_owner_history, method='GET')

        building_info_url = response.url.replace("GeneralInfo", "Tax")
        yield scrapy.Request(building_info_url, callback=self.parse_tax_info, method='GET')

    def parse_building_info(self, response):
        loader = ItemLoader(item=Building(), response=response)
        loader.add_xpath('parcel_id', '//span[@id="BasicInfo1_lblParcelID"]/text()')
        loader.add_xpath('use_code', '//span[@id="lblUse"]/text()')
        loader.add_xpath('number_rooms', '//span[@id="lblResTotRooms"]/text()')
        loader.add_xpath('basement', '//span[@id="lblResBasement"]/text()')
        loader.add_xpath('style', '//span[@id="lblResStyle"]/text()')
        loader.add_xpath('bedrooms', '//span[@id="lblResBedrooms"]/text()')
        loader.add_xpath('grade', '//span[@id="lblGrade"]/text()')
        loader.add_xpath('stories', '//span[@id="lblResStories"]/text()')
        loader.add_xpath('full_baths', '//span[@id="lblResFullBath"]/text()')
        loader.add_xpath('condition', '//span[@id="lblResCondition"]/text()')
        loader.add_xpath('year_built', '//span[@id="lblResYearBuilt"]/text()')
        loader.add_xpath('half_baths', '//span[@id="lblResHalfBath"]/text()')
        loader.add_xpath('fireplaces', '//span[@id="lblFireplace"]/text()')
        loader.add_xpath('exterior_finish',
                         '//span[@id="lblResExtFinish"]/text()')
        loader.add_xpath('heating', '//span[@id="lblResHeat"]/text()')
        loader.add_xpath('basement_garage',
                         '//span[@id="lblResGarage"]/text()')
        loader.add_xpath('roof_type', '//span[@id="lblResRoofType"]/text()')
        loader.add_xpath('cooling', '//span[@id="lblResCool"]/text()')
        loader.add_xpath('living_area', '//span[@id="lblResLiveArea"]/text()')
        yield loader.load_item()

    def parse_owner_history(self, response):
        rows = response.xpath("//div[@id='pnlPrevOwnerInfo']//tr[position() > 1]")
        for row in rows:
            loader = ItemLoader(item=PreviousOwner(), response=response)
            cells = row.css("span.Data::text").extract()
            if len(cells) < 3:
                continue
            loader.add_xpath('parcel_id', '//span[@id="BasicInfo1_lblParcelID"]/text()')
            loader.add_value('owner', cells[0])
            loader.add_value('sale_date', cells[1])
            loader.add_value('sale_price', cells[2])
            yield loader.load_item()

    def parse_tax_info(self, response):
        rows = response.xpath("//span[@id='lblTaxInfo']//tr[position() > 1]")
        for row in rows:
            loader = ItemLoader(item=PreviousTaxBill(), response=response)
            cells = row.css("td::text").extract()
            if len(cells) < 7:
                continue
            loader.add_xpath('parcel_id', '//span[@id="BasicInfo1_lblParcelID"]/text()')
            loader.add_xpath('millage_rate', '//span[@id="Label10"]/text()')
            loader.add_xpath('taxable_market_value', '//span[@id="lblTaxValue"]/text()')
            loader.add_value('year_assessed', cells[0])
            loader.add_value('paid_status', cells[1])
            loader.add_value('tax_amount', cells[2])
            loader.add_value('penalty_amount', cells[3])
            loader.add_value('interest_amount', cells[4])
            loader.add_value('total_amount', cells[5])
            loader.add_value('date_paid', cells[6])
            yield loader.load_item()
