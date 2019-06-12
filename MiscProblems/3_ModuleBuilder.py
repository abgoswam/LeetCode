node_dict = {}

class Node():
    def __init__(self, name, body):
        self.name = name
        self.body = body
        self.dependents = []
        self.visited = False


class ModuleBuilder():
    def add_module(self, name, deps, body):

        if name in node_dict:
            node = node_dict[name]
            node.body = body
        else:
            node = Node(name, body)
            node_dict[name] = node

        for dep in deps:
            if dep in node_dict:
                node.dependents.append(node_dict[dep])
            else:
                nnode = Node(dep, None)
                node_dict[dep] = nnode
                node.dependents.append(nnode)

    def query_module(self, name):
        if name not in node_dict:
            return None

        node = node_dict[name]
        if node.visited == True:
            return None

        node.visited = True
        deps = node.dependents

        for dep in deps:
            self.query_module(dep.name)

        print(node.body)


mb = ModuleBuilder()

mb.add_module("a", ["b", "c"], "b() c()")
mb.add_module("b", ["c", "d", "e"], "c() d() e()")
mb.add_module("c", ["d", "e"], "d() e()")
mb.add_module("d", [], "NA (d)")
mb.add_module("e", [], "NA (e)")
mb.add_module("f", ["g"], "g()")
mb.add_module("g", [], "NA (g)")

print("View a:")
mb.query_module("a")

print("View f:")
mb.query_module("f")