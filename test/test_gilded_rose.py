# -*- coding: utf-8 -*-
import unittest

from main.GildedRose.gilded_rose_new import Item, GildedRose , SellInRange

class GildedRoseTest(unittest.TestCase):

    def setUp(self):
        self.items = [
            Item("Sulfuras, Hand of Ragnaros", 5, 80),
            Item("Conjured item", 5, 40),
            Item("foo", 0, 40),
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 40),
        ]


        self.item_types = {"Aged Brie": [SellInRange(None, None, 1)],
                      "Backstage passes to a TAFKAL80ETC concert": [SellInRange(6, None, 1), SellInRange(1, 6, 2), SellInRange(None, 0, -100)],
                      "Sulfuras, Hand of Ragnaros": [SellInRange(None, None, 0)],
                      "Conjured item": [SellInRange(1, None, -2), SellInRange(None, 0, -4)],
                      "Generic Item": [SellInRange(1, None, -1), SellInRange(None, 0, -2)]
                      }


    def test_types(self):

        gilded_rose = GildedRose(self.items, self.item_types)

        gilded_rose.update_quality()

        self.assertEquals("Sulfuras, Hand of Ragnaros", self.items[0].name)
        self.assertEquals(80, self.items[0].quality)
        self.assertEquals(5, self.items[0].sell_in)

        self.assertEquals("Conjured item", self.items[1].name)
        self.assertEquals(38, self.items[1].quality)
        self.assertEquals(4, self.items[1].sell_in)

        #Generic item test, no specific item rules apply for it, uses Generic item definition
        self.assertEquals("foo", self.items[2].name)
        self.assertEquals(38, self.items[2].quality)
        self.assertEquals(-1, self.items[2].sell_in)

        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", self.items[3].name)
        self.assertEquals(0, self.items[3].quality)
        self.assertEquals(-1, self.items[3].sell_in)

    def test_get_sell_range(self):

        ranges = self.item_types[self.items[1].name]
        gilded_rose = GildedRose(self.items, self.item_types)

        range = gilded_rose._get_sell_range(ranges, 5)
        self.assertEquals(-2, range.quality_change)


        range = gilded_rose._get_sell_range(ranges, -1)
        self.assertEquals(-4, range.quality_change)


if __name__ == '__main__':
    unittest.main()
