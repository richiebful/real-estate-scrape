import pyarrow.parquet as pq
from scrapy.exporters import JsonLinesItemExporter

def item_type(item):
    return type(item).__name__.replace('Item','').lower()  # TeamItem => team

class SaveToJsonLinesPipeline(object):
    save_types = ['PreviousOwner', 'PreviousTaxBill', 'Building', 'Parcel']
    
    def open_spider(self, spider):
        self.files = dict([ (name, open('../data/' + name +'.jl','w+b')) for name in self.save_types ])
        self.exporters = dict([ (name,JsonLinesItemExporter(self.files[name])) for name in self.save_types])
        [e.start_exporting() for e in self.exporters.values()]

    def close_spider(self, spider):
        [e.finish_exporting() for e in self.exporters.values()]
        [f.close() for f in self.files.values()]

    def process_item(self, item, spider):
        what = item_type(item)
        if what in set(self.save_types):
            self.exporters[what].export_item(item)
        return item

    
