import pytest

from hypothesis import given, example
from hypothesis.strategies import integers

from gilded_rose import Item, GildedRose


def test_generic_item_quality_decreases_by_1_before_sell_by_date():
    item = Item(name="Generic", sell_in=10, quality=5)
    truc = GildedRose([item])

    truc.update_quality()

    assert item.sell_in == 9
    assert item.quality == 4


def test_generic_item_quality_decreases_by_2_after_sell_by_date():
    item = Item(name="Generic", sell_in=0, quality=5)
    truc = GildedRose([item])

    truc.update_quality()

    assert item.sell_in == -1
    assert item.quality == 3


def test_item_quality_is_never_negative():
    item = Item(name="Generic", sell_in=1, quality=0)
    truc = GildedRose([item])

    truc.update_quality()

    assert item.sell_in == 0
    assert item.quality == 0


def test_brie_quality_increases_by_1_before_sell_by_date():
    item = Item(name="Aged Brie", sell_in=10, quality=5)
    truc = GildedRose([item])

    truc.update_quality()

    assert item.sell_in == 9
    assert item.quality == 6


@pytest.mark.parametrize("name", [
    "Generic",
    "Aged Brie",
    "Sulfuras, Hand of Ragnaros",
    "Backstage passes to a TAFKAL80ETC concert",
])
def test_quality_is_never_more_than_50(name):
    item = Item(name=name, sell_in=10, quality=50)
    truc = GildedRose([item])

    truc.update_quality()

    assert item.quality <= 50


def test_sulfuras_never_has_to_be_sold_or_decreases_in_quality():
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=42, quality=10)
    truc = GildedRose([item])

    truc.update_quality()

    assert item.sell_in == 42
    assert item.quality == 10


def test_backstage_pass_quality_increases_by_1_10_days_before_concert():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=5)
    truc = GildedRose([item])

    truc.update_quality()

    assert item.sell_in == 10
    assert item.quality == 6


def test_backstage_pass_quality_increases_by_2_between_5_and_9_days_before_concert():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=5)
    truc = GildedRose([item])

    truc.update_quality()

    assert item.sell_in == 7
    assert item.quality == 7


def test_backstage_pass_quality_increases_by_3_5_days_before_concert():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=5)
    truc = GildedRose([item])

    truc.update_quality()

    assert item.sell_in == 2
    assert item.quality == 8


def test_backstage_pass_quality_is_zero_after_concert():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=5)
    truc = GildedRose([item])

    truc.update_quality()

    assert item.sell_in == -1
    assert item.quality == 0


@given(integers())
@example(11)
@example(10)
@example(9)
@example(6)
@example(5)
@example(4)
@example(1)
@example(0)
@example(-1)
def test_backstage_pass_quality(days_before_concert):
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=days_before_concert, quality=5)
    truc = GildedRose([item])

    truc.update_quality()

    assert item.sell_in == days_before_concert - 1

    if days_before_concert > 10:
        assert item.quality == 6
    elif days_before_concert > 5:
        assert item.quality == 7
    elif days_before_concert > 0:
        assert item.quality == 8
    else:
        assert item.quality == 0
