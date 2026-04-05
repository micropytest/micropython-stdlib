import collections
import collections.abc as abc
from unittest import TestCase


class TestCollections(TestCase):
  def test_import_collections(self) -> None:
    """Check that when collections imported, namedtuple and others available."""

    self.assertTrue(collections.namedtuple)
    self.assertTrue(collections.OrderedDict)
    self.assertTrue(collections.deque)

  def test_import_collections_abc(self) -> None:
    """Check that when collections.abc imported, Iterator available."""

    self.assertTrue(abc.Iterator)
