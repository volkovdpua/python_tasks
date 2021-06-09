import pytest
from tasks import filter_list
from tasks import find_matches
from tasks import comb_without_zip
from tasks import merge_dict
from tasks import get_extension


def test_filter_list():
    assert filter_list([1, 5, 4, 3, 2], 4) == [1, 3, 2]


def test_find_matches():
    assert find_matches([1, 2, 3, 4], [2, 5, 7, 3]) == [2, 3]


def test_comb_without_zip():
    assert comb_without_zip([1, 2, 5], [2, 3, 6, 7]) == [[1, 2], [2, 3], [5, 6]]


def test_get_extension():
    assert get_extension("test_file.txt") == ".txt"


def test_merge_dict():
    assert merge_dict({1: 2, 2: 4}, {3: 6}) == {1: 2, 2: 4, 3: 6}
