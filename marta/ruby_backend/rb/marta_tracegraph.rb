#!/usr/bin/env ruby
# frozen_string_literal: true

# MARTA Ruby dynamic call graph helper.
#
# Runs a driver script under TracePoint and records the *actual* caller→callee
# edges between methods defined under the source directory. Emits them as JSON.
# The dynamic counterpart to the static Prism walker: exact for the paths the
# driver exercises, but blind to code it doesn't run.
#
#   ruby marta_tracegraph.rb <source_abs_dir> <driver.rb>
#
# Only Ruby-level :call/:return are traced (method-to-method). C-level methods
# (operators, and attr_reader/accessor accessors, which are C-defined) are NOT
# captured — a known difference from the static graph, surfaced in comparison.

require "json"

source_dir = File.expand_path(ARGV.shift.to_s)
driver = ARGV.shift

if source_dir.empty? || driver.nil?
  warn "usage: ruby marta_tracegraph.rb <source_abs_dir> <driver.rb>"
  exit 2
end

$LOAD_PATH.unshift(source_dir)

# Qualified name in MARTA's convention: Foo#inst_method / Foo.singleton_method.
def qname(klass, mid)
  s = klass.to_s
  if (m = s.match(/\A#<Class:(.+)>\z/))
    "#{m[1]}.#{mid}"
  else
    "#{klass}##{mid}"
  end
end

edges = {}
stack = []

tp = TracePoint.new(:call, :return) do |t|
  in_scope = t.path.to_s.start_with?(source_dir)
  if t.event == :call
    callee = { qn: qname(t.defined_class, t.method_id), scope: in_scope }
    caller = stack.last
    if caller && caller[:scope] && in_scope && caller[:qn] != callee[:qn]
      (edges[caller[:qn]] ||= [])
      edges[caller[:qn]] << callee[:qn] unless edges[caller[:qn]].include?(callee[:qn])
    end
    stack.push(callee)
  else
    stack.pop
  end
end

tp.enable
begin
  load driver
rescue Exception => e   # keep going: emit whatever was traced before the error
  warn "driver raised: #{e.class}: #{e.message}"
ensure
  tp.disable
end

$stdout.write(JSON.generate({ "source_dir" => source_dir, "edges" => edges }))
