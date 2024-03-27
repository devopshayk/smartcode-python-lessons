class PaginationHelper:
    
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.item_per_page = items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        if len(self.collection) % self.item_per_page == 0:
            return len(self.collection) // self.item_per_page
        else:
            return len(self.collection) // self.item_per_page + 1

    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        elif page_index == self.page_count() - 1:
            return len(self.collection) % self.item_per_page
        else:
            return self.item_per_page

    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        pass

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# print(helper.item_count())
# print(helper.page_count())
print(helper.page_item_count(0))
