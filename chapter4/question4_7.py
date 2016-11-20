from collections import deque, OrderedDict


class Project:
    def __init__(self, name):
        self.name = name
        self.children = []


def build_links(projects, deps):
    project_dict = {name: Project(name) for name in projects}
    root_nodes = project_dict.keys()
    for parent_name, child_name in deps:
        parent = project_dict[parent_name]
        child = project_dict[child_name]

        parent.children.append(child)
        root_nodes -= set(child_name)

    root_nodes = [project_dict[root] for root in root_nodes]

    return project_dict, root_nodes


def build_order(projects, roots):
    queue = deque(roots)

    order = OrderedDict()
    while queue:
        cur_node = queue.pop()
        order[cur_node.name] = cur_node
        for child in cur_node.children:
            if child.name not in order:
                queue.appendleft(child)

    return order if len(order) == len(projects) else None


def main():
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    deps = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

    project_dict, root_nodes = build_links(projects, deps)
    order = build_order(projects, root_nodes)
    print(order.keys())


if __name__ == '__main__':
    main()
