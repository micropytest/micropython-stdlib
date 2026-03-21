from typing import Any, Literal, final, override  # type: ignore
from unittest import TestCase


class TestOverride(TestCase):
  def test_override(self) -> None:
    """Check that @override does nothing."""

    # (1) act
    class Printer:
      def print(self, *_: Any) -> None:
        pass

    class PrinterX(Printer):
      @override
      def print(self, *_: Any) -> None:
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
    self.assertTrue(isclass(A))
    self.assertTrue(callable(B.m))


class TestLiteral(TestCase):
  def test_literal(self) -> None:
    def fn(l: Literal["x", "y"]) -> None:
      pass
