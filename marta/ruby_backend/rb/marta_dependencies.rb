#!/usr/bin/env ruby
# Production namespace evidence. Never require the libraries being inspected.
# Bundler metadata is read in a separate mode so its activated JSON version is
# respected; Prism inspection runs without activating the project's bundle.
if ARGV.first == "--bundle"
  require "bundler/setup"
  require "json"
  puts JSON.generate(Bundler.load.specs.map do |spec|
    roots = spec.full_require_paths.select { |p| File.directory?(p) }
    conventional = [spec.name, spec.name.tr("-", "/"), spec.name.tr("-", "_")].uniq
    candidates = conventional.flat_map do |name|
      roots.filter_map do |root|
        path = File.join(root, "#{name}.rb")
        {"require" => name, "path" => path} if File.file?(path)
      end
    end
    if candidates.empty?
      candidates = roots.flat_map do |root|
        Dir[File.join(root, "*.rb")].sort.map do |path|
          {"require" => File.basename(path, ".rb"), "path" => path}
        end
      end
    else
      # Prefer the first conventional name; multiple names can be aliases.
      candidates = candidates.select { |c| c["require"] == candidates.first["require"] }
    end
    {"gem" => spec.name, "version" => spec.version.to_s,
     "gem_path" => spec.full_gem_path, "roots" => roots, "entries" => candidates}
  end)
  exit
end

require "prism"
require "json"

class DependencyFacts < Prism::Visitor
  attr_reader :definitions, :references

  def initialize
    super
    @scope, @definitions, @references = [], [], []
  end

  def namespace(node)
    name = node.constant_path.slice.to_s
    full = name.start_with?("::") ? name.delete_prefix("::") : (@scope + [name]).join("::")
    @definitions << full
    old = @scope
    @scope = full.split("::")
    visit_child_nodes(node)
    @scope = old
  end

  def visit_class_node(node) = namespace(node)
  def visit_module_node(node) = namespace(node)

  def visit_constant_read_node(node)
    @references << node.name.to_s
  end

  def visit_constant_path_node(node)
    name = node.slice.to_s.delete_prefix("::")
    @references << name if name.match?(/\A[A-Z]\w*(?:::[A-Z]\w*)*\z/)
    # Keep the complete reference, rather than generating ambiguous shorter
    # prefixes for every child of a qualified path.
  end

end

def facts(path)
  parsed = Prism.parse(File.read(path, encoding: "UTF-8").scrub("?"))
  visitor = DependencyFacts.new
  parsed.value.accept(visitor)
  {"definitions" => visitor.definitions.uniq.sort,
   "references" => visitor.references.uniq.sort,
   "errors" => parsed.errors.map(&:message)}
end

request = JSON.parse($stdin.read)
if ARGV.first == "--files"
  puts JSON.generate(request.fetch("files").to_h { |path| [path, facts(path)] })
else
  abort "expected --bundle or --files"
end
