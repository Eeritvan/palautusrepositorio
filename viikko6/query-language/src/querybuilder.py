from matchers import And, All, Or, Not, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matcher = matcher

    def _group_matchers(self, matcher):
        return QueryBuilder(And(self._matcher, matcher))

    def build(self):
        return self._matcher
    
    def plays_in(self, team):
        return self._group_matchers(PlaysIn(team))
    
    def has_at_least(self, value, attr):
        return self._group_matchers(HasAtLeast(value, attr))

    def has_fewer_than(self, value, attr):
        return self._group_matchers(HasFewerThan(value, attr))
    
    def one_of(self, matcher1, matcher2):
        return QueryBuilder(Or(matcher1, matcher2))