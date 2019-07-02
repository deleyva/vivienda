# -*- coding: utf-8 -*-
import scrapy


class ViviendaEncinacorbaSpider(scrapy.Spider):
    name = 'vivienda-encinacorba'
    allowed_domains = ['www.fincasverus.com']
    start_urls = ['http://www.fincasverus.com/busqueda-avanzada/?title=encinacorba&status=en-venta/']

    def parse(self, response):
        if 'fincasverus' in response._get_url():
            for casa in response.css('div.property-inner'):
                item = {
                    'imagen_casa': casa.css('div.property-image img::attr(src)').get(),
                    'metros': casa.css('div.property-area-inner span.property-info-value::text').get().strip('\t'),
                    'dormitorios': casa.css('div.property-bedrooms-inner span.property-info-value::text').get().strip('\t'),
                    'baños': casa.css('div.property-bathrooms-inner span.property-info-value::text').get().strip('\t'),
                    'precio': casa.css('div.property-price span::text').get().strip()
                    # 'garaje': casa.css('div.property-garages-inner span.property-info-value::text').get().strip('\t'),
                }
                print(item)
                yield item
