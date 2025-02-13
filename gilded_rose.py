class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras":
                continue
            self.update_item(item)

    def update_item(self, item):
        if item.name == "Sulfuras":
            return

        self.update_sell_in(item)
        self.update_quality_value(item)

        if item.sell_in < 0:
            self.handle_expired_item(item)

    def update_sell_in(self, item):
        item.sell_in -= 1

    def update_quality_value(self, item):
        if item.name == "Aged Brie":
            self.increase_quality(item)
        elif item.name == "Backstage":
            self.update_backstage_passes(item)
        elif item.name == "Conjured":
            self.decrease_quality(item, 2)
        else:
            self.decrease_quality(item, 1)

    def update_backstage_passes(self, item):
        if item.sell_in > 10:
            self.increase_quality(item)
        elif item.sell_in > 5:
            self.increase_quality(item, 2)
        elif item.sell_in > 0:
            self.increase_quality(item, 3)
        else:
            item.quality = 0

    def handle_expired_item(self, item):
        if item.name == "Aged Brie":
            self.increase_quality(item)
        elif item.name == "Backstage":
            item.quality = 0
        elif "Conjured" in item.name:
            self.decrease_quality(item, 2)
        else:
            self.decrease_quality(item, 1)

    def increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)

    def decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)

    def get_items(self):
        return [item.name for item in self.items]

    def get_item_number(self):
        return len(self.items)