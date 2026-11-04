"""Process-local reuse of static Planner context, never of error-directed help."""
from __future__ import annotations


class PlannerRetrievalCache:
    """Memoize formatted related lines for an explicitly versioned index snapshot.

    Custom indexes without a revision still work, but are queried every time.
    One successful entry per definition bounds storage to the queried target set.
    Empty results are not retained: the existing database API can also return
    an empty list on a transient query failure.
    """

    def __init__(self):
        self.clear()

    def clear(self):
        self._database = None
        self._revision = None
        self._entries = {}

    def related(self, database, query, *, exclude, k=3):
        revision = getattr(database, "retrieval_revision", None)
        cacheable = type(revision) is str and bool(revision)
        if (database is not self._database or revision != self._revision
                or not cacheable):
            self.clear()
            if cacheable:
                self._database, self._revision = database, revision
        key = (query, k)
        cached = self._entries.get(exclude)
        if cacheable and cached is not None and cached[0] == key:
            return list(cached[1]), True, True
        # Exceptions propagate; neither exceptions nor empty results are cached.
        lines = database.related_lines(query, k=k, exclude=exclude)
        if not lines:
            return None, False, cacheable
        stored = tuple(lines)
        if cacheable:
            self._entries[exclude] = (key, stored)
        # Keep the saved value independent of caller-side prompt reductions.
        return list(stored), False, cacheable
