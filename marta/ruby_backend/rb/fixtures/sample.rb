# Fixture exercising the parameter kinds and class features the parser must capture.

module Greetable
  def greeting_prefix
    "Hello"
  end
end

class Calculator < Numeric
  include Greetable
  extend Comparable

  def initialize(base = 0)
    @base = base
  end

  # Every parameter kind in one signature.
  def compute(a, b = 1, *rest, k:, k2: 2, **opts, &blk)
    a + b
  end

  def self.version
    "1.0"
  end

  def no_args
    42
  end
end

def top_level_helper(x, y)
  x - y
end
