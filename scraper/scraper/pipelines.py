import pyarrow.parquet as pq

class SaveToJsonLinesPipeline(object):
    def process_item(self, item, spider):
        return item
    
    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    
