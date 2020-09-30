# -*- coding: utf-8 -*-
from __future__ import print_function

from main.GildedRose.gilded_rose_new import *

if __name__ == "__main__":
    print ("OMGHAI!")
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    item_types = {"Aged Brie": [SellInRange(None, None, 1)],
                   "Backstage passes to a TAFKAL80ETC concert": [SellInRange(6, None, 1), SellInRange(1, 6, 2),
                                                                 SellInRange(None, 0, -100)],
                   "Sulfuras, Hand of Ragnaros": [SellInRange(None, None, 0)],
                   "Conjured item": [SellInRange(1, None, -2), SellInRange(None, 0, -4)],
                   "Generic Item": [SellInRange(1, None, -1), SellInRange(None, 0, -2)]
                   }

    days = 3
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items, item_types).update_quality()
