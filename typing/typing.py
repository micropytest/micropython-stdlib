__all__ = [
  "Any",
  "final",
  "Literal",
  "override",
]


def override(fn):
  """Decorator to indicate that a method is intended to override a method in a base class."""

  return fn


def final(fn):
  """Decorator to indicate final methods and final classes."""

  return fn


Any = object


class Literal:
  """Special typing form to define literal types (a.k.a. value types)."""

  def __getitem__(self, _):
    return self
