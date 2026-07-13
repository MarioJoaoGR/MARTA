"""Ruby language backend for MARTA (MVP).

Isolates everything Ruby-specific — parsing (Prism via a Ruby helper),
syntax check, RSpec runner and SimpleCov coverage — behind a small surface the
language-agnostic orchestrator can call. See ``ruby_ast.py`` for the parser
wrapper, the entry point of Fase 1.
"""
