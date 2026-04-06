from typing import (
  final,
  overload,
  override,  # type: ignore
)
from unittest import TestCase


class TestOverload(TestCase):
  def test_overload(self) -> None:
    """Check that @overload does nothing."""

    # (1) act
    @overload
    def sum(x: int, y: int) -> int: ...

    @overload
    def sum(x: float, y: float) -> float: ...

    def sum(x, y):
      return x + y

    # (2) assessment
    self.assertTrue(callable(sum))
    self.assertEqual(sum(12, 34), 46)


class TestOverride(TestCase):
  def test_override(self) -> None:
    """Check that @override does nothing."""

    # (1) act
    class Printer:
      def print(self, *_) -> None:
        pass

    class PrinterX(Printer):
      @override
      def print(self, *_) -> None:
        pass

    # (2) assessment
    self.assertTrue(callable(PrinterX.print))


class TestFinal(TestCase):
  def test_final(self) -> None:
    # (1) act
    @final
    class A:
      pass

    class B:
      @final
      def m(self) -> None:
        pass

    # (2) assessment
    self.assertIsInstance(A, type)
    self.assertTrue(callable(B.m))
