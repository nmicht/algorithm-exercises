# Can team a beat team b
# INCOMPLETE
import collections

MatchResult = collections.namedtuple('MatchResult',
                                    ('winning_team', 'losing_team'))

def can_team_a_beat_team_b(matches, team_a, team_b):
    def build_graph():
        graph = collections.defaultdict(set)
        for match in matches:
            graph[match.winning_team].add(match.losing_team)
        return graph

    def is_reachable(graph, start, end, visited):
        for i in graph[start]:
            if i == end:
                return True
            elif i not in visited:
                visited.add(i)
                return is_reachable(graph, i, end, visited)
            else:
                return False

    return is_reachable(build_graph(), team_a, team_b, visited=set())

g = can_team_a_beat_team_b([
    MatchResult(winning_team=6, losing_team=1), 
    MatchResult(winning_team=1, losing_team=3), 
    MatchResult(winning_team=3, losing_team=2),
    MatchResult(winning_team=1, losing_team=2)], 6, 5)
print(g)