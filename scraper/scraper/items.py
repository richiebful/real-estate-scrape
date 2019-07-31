# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from datetime import datetime
from decimal import Decimal

def strip_string(s: str):
    if s != None:
        return s.strip()
    else:
        return None

def parse_us_date(s: str):
    return datetime.strptime(s, '%m/%d/%Y')

def parse_us_dollars(s: str):
    return Decimal(s.replace('$', '').replace(',', ''))

class Parcel(scrapy.Item):
    """Capture parcel-level data from the "General Information" page on the portal site"""
    parcel_id = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    property_address = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=Join("\n")
    )
    municipality = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    owner_name = scrapy.Field(
        input_processor=MapCompose(strip_string)
    )
    school_district = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    neighborhood_code = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    tax_code = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    owner_code = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    clean_green = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    zoning_class = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    recording_date = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_date),
        output_processor=TakeFirst()
    )
    use_code = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    sale_date = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_date),
        output_processor=TakeFirst()
    )
    homestead = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    sale_price = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    farmstead = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    deed_book = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    deed_page = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    lot_area = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    abatement = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    # this section depends on current_year
    current_year = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    cy_market_land_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    cy_market_building_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    cy_market_total_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    py_market_land_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    py_market_building_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    py_market_total_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    cy_assessed_land_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    cy_assessed_building_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    cy_assessed_total_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    py_assessed_land_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    py_assessed_building_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    py_assessed_total_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    owner_mailing = scrapy.Field(
        output_processor=Join("\n")
    )

class Building(scrapy.Item):
    """Capture parcel-level data from the "Building Information" page on the portal site"""
    parcel_id = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    use_code = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    number_rooms = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    style = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    condition = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    stories = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    year_built = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    exterior_finish = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    roof_type = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    total_rooms = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    basement = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    bedrooms = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    grade = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    full_baths = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    half_baths = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    fireplaces = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    heating = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    cooling = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    basement_garage = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    living_area = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )

class PreviousOwner(scrapy.Item):
    """Capture all the previous owners of a parcel from the 'Owner History' page"""
    parcel_id = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    owner = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    sale_date = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_date),
        output_processor=TakeFirst()
    )
    sale_price = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )

class PreviousTaxBill(scrapy.Item):
    """Capture recent tax payments from the page 'Tax Info'"""
    #top level elements
    parcel_id = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    millage_rate = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    taxable_market_value = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )

    #row elements
    year_assessed = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    paid_status = scrapy.Field(
        input_processor=MapCompose(strip_string),
        output_processor=TakeFirst()
    )
    tax_amount = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    penalty_amount = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    interest_amount = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    total_amount = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_dollars),
        output_processor=TakeFirst()
    )
    date_paid = scrapy.Field(
        input_processor=MapCompose(strip_string, parse_us_date),
        output_processor=TakeFirst()
    )

# class Residential
