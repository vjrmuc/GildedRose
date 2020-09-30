# -*- coding: utf-8 -*-
from main.util.exceptions.improper_configuration_exception import ImproperConfigurationException


class GildedRose(object):

    def __init__(self, items, item_types):
        self.items = items
        self.item_types = item_types

    def update_quality(self):
        """
        Entry point method to update the quality of all items based on item type and days left to sell
        :return:
        """
        for item in self.items:
            if item.name in self.item_types.keys():
                item_sell_ranges = self.item_types[item.name]
            else:
                item_sell_ranges = self.item_types["Generic Item"]

            sell_range = self._get_sell_range(item_sell_ranges, item.sell_in)
            self._update_item_quality(item, sell_range.quality_change)

    def _get_sell_range(self, item_sell_ranges, days_left):
        """
        Gets the sell range, which applies for the specific item
        :param item_sell_ranges: array with all sell ranges for a particular item
        :param days_left: number of days left to sell, used to pull a sell range
        :return:
        """
        for item_sell_range in item_sell_ranges:
            if item_sell_range.range_min is None and item_sell_range.range_max is None:
                return item_sell_range
            elif item_sell_range.range_min is None and days_left <= item_sell_range.range_max:
                return item_sell_range
            elif item_sell_range.range_max is None and days_left >= item_sell_range.range_min:
                return item_sell_range
            elif  item_sell_range.range_min is not None and item_sell_range.range_max is not None and days_left > item_sell_range.range_min and days_left < item_sell_range.range_max:
                return item_sell_range

        raise ImproperConfigurationException("The correct item_sell_range is not properly configured")

    def _update_item_quality(self, item, quality_change):
        """
        Updates quality of a specific item based on item type and qality change
        :param item:
        :param quality_change:
        :return:
        """
        if item.name == "Sulfuras, Hand of Ragnaros":
            return

        new_quality = item.quality + quality_change
        if new_quality <= 0:
            new_quality = 0
        elif new_quality >= 50:
            new_quality = 50

        item.quality = new_quality
        item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class SellInRange:
    def __init__(self, range_min, range_max, quality_change):
        self.range_min = range_min
        self.range_max = range_max
        self.quality_change = quality_change


