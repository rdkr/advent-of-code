from dataclasses import dataclass


@dataclass
class Rule:
    colour: str
    rules: list


@dataclass
class Node:
    colour: str
    contains: list
    contained_by: list


@dataclass
class Link:
    count: int
    node: Node


def contained_by(nodes_q):
    colours = set()
    while nodes_q:
        node = nodes_q.pop()
        colours.add(node.colour)
        nodes_q.extend([link.node for link in node.contained_by])
    return len(colours) - 1


def contains(nodes_q):
    count = 0
    while nodes_q:
        node = nodes_q.pop()
        count = count + sum([link.count for link in node.contains])
        for link in node.contains:
            nodes_q.extend([link.node] * link.count)
    return count


def graph():
    graph = {}
    rules = []

    with open("07.txt") as _input:
        for line in _input:
            clean = line.replace(".", "").replace("bags", "").replace("bag", "").strip()
            container, contents = clean.split("contain")
            name = container.strip()
            rules.append(Rule(name, [x.strip() for x in contents.split(",")]))
            graph[name] = Node(name, [], [])

    for rule in rules:
        for link in rule.rules:
            if link == "no other":
                continue
            count, colour = link.split(" ", 1)
            graph[colour].contained_by.append(Link(int(count), graph[rule.colour]))
            graph[rule.colour].contains.append(Link(int(count), graph[colour]))

    return graph


graph = graph()
print(contained_by([graph["shiny gold"]]))
print(contains([graph["shiny gold"]]))
