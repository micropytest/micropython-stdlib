import unittest
from enum import (
  IntEnum,
  enum,  # pyright: ignore
)


# The test int enum.
@enum
class Color(IntEnum):
  RED = 1
  BLUE = 2
  GREEN = 3


class TestIntEnum(unittest.TestCase):
  def test_values(self):
    """Check that an IntEnum subclass is well-defined."""

    assert Color.BLUE == 2
    assert isinstance(Color.BLUE, int)
    assert isinstance(Color.BLUE, Color)

  def test_call_returns_i(self):
    """Check that Color(value) returns a Color instance if value found."""

    assert Color(1) is Color.RED
    assert Color(2) is Color.BLUE
    assert Color(3) is Color.GREEN

  def test_call_raises_error(self):
    """Check that Color(value) raises error if value not found."""

    with self.assertRaises(ValueError) as cm:
      Color(123)

    assert str(cm.exception) == "Value '123' not found in Color(IntEnum)."
