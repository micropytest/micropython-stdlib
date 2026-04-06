__all__ = [
  "final",
  "overload",
  "override",
]


def overload(fn):
  """Decorator to indicate that a function or method is an overload."""

  return fn


def override(fn):
  """Decorator to indicate that a method is intended to override a method in a base class."""

  return fn


def final(fn):
  """Decorator to indicate final methods and final classes."""

  return fn
