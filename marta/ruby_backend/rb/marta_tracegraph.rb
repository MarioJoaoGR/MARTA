#!/usr/bin/env ruby
# frozen_string_literal: true

# Optional diagnostic driver, never part of ordinary generation.
# ruby marta_tracegraph.rb <source_abs_dir> <driver.rb> [--include-c]
# C event paths identify the call site, NOT the method definition. Include a
# C-backed method only when its UnboundMethod source_location is in the project.
require "json"

include_c = !!ARGV.delete("--include-c")
if ARGV.length != 2 || !File.directory?(ARGV[0])
  warn "usage: ruby marta_tracegraph.rb <source_abs_dir> <driver.rb> [--include-c]"
  exit 2
end
source_dir = File.expand_path(ARGV[0])
driver = File.expand_path(ARGV[1])
$LOAD_PATH.unshift(source_dir)

def qname(klass, mid)
  s = klass.to_s
  if (m = s.match(/\A#<Class:(.+)>\z/))
    "#{m[1]}.#{mid}"
  else
    "#{klass}##{mid}"
  end
end

prefix = source_dir.end_with?(File::SEPARATOR) ? source_dir : source_dir + File::SEPARATOR
paths = {}
in_scope = lambda do |path|
  paths.fetch(path) do
    absolute = path && File.expand_path(path)
    paths[path] = !!(absolute && (absolute == source_dir || absolute.start_with?(prefix)))
  end
end
# Do not cache method lookups: redefinition during the driver can change origins.
method_origin = lambda do |event|
  begin
    event.defined_class.instance_method(event.callee_id || event.method_id).source_location&.first
  rescue NameError, TypeError
    nil
  end
end

edges, observations, stacks = {}, {}, {}
metadata = { "policy" => "ruby-tracepoint-v2", "ruby_version" => RUBY_VERSION,
             "include_c" => include_c, "driver" => driver,
             "driver_status" => "running", "completed" => false,
             "unmatched_returns" => 0, "stack_resets" => 0,
             "projection" => "ruby-and-project-c; external-c-transparent; external-ruby-barrier" }
events = include_c ? %i[call return c_call c_return] : %i[call return]
metadata["events"] = events.map(&:to_s)
tp = TracePoint.new(*events) do |t|
  # A suspended fiber/thread must never become the caller in another context.
  stack = (stacks[[Thread.current, Fiber.current]] ||= [])
  ruby_event = %i[call return].include?(t.event)
  token = [ruby_event ? :ruby : :c, t.defined_class, t.method_id]
  if t.event == :call || t.event == :c_call
    origin = ruby_event ? t.path : method_origin.call(t)
    frame = { token: token, qn: qname(t.defined_class, t.method_id), scope: in_scope.call(origin), ruby: ruby_event }
    # Built-in iterators and Class#new must not hide the enclosing Ruby caller.
    # An out-of-scope Ruby method remains a barrier, as in the Ruby-only mode.
    caller = stack.reverse_each.find { |parent| parent[:ruby] || parent[:scope] }
    if caller && caller[:scope] && frame[:scope] && caller[:qn] != frame[:qn]
      (edges[caller[:qn]] ||= [])
      edges[caller[:qn]] << frame[:qn] unless edges[caller[:qn]].include?(frame[:qn])
      observations[[caller[:qn], frame[:qn], t.event.to_s]] = true
    end
    stack.push(frame)
  elsif stack.last && stack.last[:token] == token
    stack.pop
  else
    metadata["unmatched_returns"] += 1
    unless stack.empty?
      metadata["stack_resets"] += 1
      stack.clear  # Abstain rather than attach future calls to a stale frame.
    end
  end
end

begin
  tp.enable(target_thread: nil) { load driver }
  metadata["driver_status"] = "returned"
  metadata["completed"] = true
rescue Exception => e # Preserve partial evidence, distinguish it from completion.
  metadata["driver_status"] = e.is_a?(SystemExit) ? "system_exit" : "raised"
  metadata["driver_error"] = { "class" => e.class.name, "message" => e.message }
  metadata["driver_exit_status"] = e.status if e.is_a?(SystemExit)
  warn "driver raised: #{e.class}: #{e.message}"
ensure
  tp.disable
end
metadata["remaining_frames"] = stacks.values.sum(&:length)
records = observations.keys.map { |caller, callee, event| { "caller" => caller, "callee" => callee, "event" => event } }
$stdout.write(JSON.generate({ "source_dir" => source_dir, "edges" => edges,
                             "observations" => records, "trace" => metadata }))
