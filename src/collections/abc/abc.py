__all__ = [
  "Iterator",
]


class Iterator:
  """Base class for the iterators."""

  def __next__(self):
    raise StopIteration()

  def __iter__(self):
    return self
