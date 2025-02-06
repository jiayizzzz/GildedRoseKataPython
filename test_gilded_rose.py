# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    def test_aged_brie_increases_in_quality_when_getting_older(self):
        items = [Item("Aged Brie", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        aged_brie_item = items[0]
        self.assertEquals(19, aged_brie_item.quality)

    def test_quality_never_negative(self):
        items = [Item("Elixir of the Mongoose", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, -1)

    def test_quality_never_above_50(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 51)

    def test_gilded_rose_list_item_number(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        item_number = gilded_rose.get_item_number()
        self.assertEquals(1, item_number)


if __name__ == '__main__':
    unittest.main()