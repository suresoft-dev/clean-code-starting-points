"""
General Quality Rules:
- update_quality is called once per day
- The Quality of a regular item drops by 1 every day
- Once the sell by date has passed, Quality degrades twice as fast
- The Quality of an item is never negative

Special Items:
- "Aged Brie" actually increases in Quality the older it gets
- The Quality of an item is never more than 50
- "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
- "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
  Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
  Quality drops to 0 after the concert
- "Conjured" items degrade in Quality twice as fast as normal items
"""


def decay_sulfuras(item):
    pass


def decay_regular(item):
    item.quality = item.quality - 1
    if item.sell_in < 0:
        item.quality = item.quality - 1


def decay_brie(item):
    item.quality = item.quality + 1
    if item.sell_in < 0:
        item.quality = item.quality + 1


def decay_backstage_passes(item):
    item.quality = item.quality + 1
    if item.sell_in < 10:
        item.quality = item.quality + 1
    if item.sell_in < 5:
        item.quality = item.quality + 1

    if item.sell_in < 0:
        item.quality = 0


item_decays = {
    "Aged Brie": decay_brie,
    "Backstage passes to a TAFKAL80ETC concert": decay_backstage_passes,
    "Sulfuras, Hand of Ragnaros": decay_sulfuras,
}


class GildedRose:
    def __init__(self, items: list["Item"]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # can we also just continue for Sulfaras and get rid of many checks?
            # if item.name == "Sulfuras, Hand of Ragnaros":
            #    continue
            # ??? +2
            self.decay(item)

    def decay(self, item: "Item") -> None:
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

        # Quality updates
        decay = item_decays.get(item.name, decay_regular)
        decay(item)

        # extra check method?
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.quality = max(0, min(50, item.quality))


# sub classes using Polymorphism? items that are gone bad, special items
class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
