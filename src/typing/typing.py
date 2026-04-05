__all__ = [
  "final",
  "override",
]


def override(fn):
  """Decorator to indicate that a method is intended to override a method in a base class."""

  return fn


def final(fn):
  """Decorator to indicate final methods and final classes."""

  return fn
