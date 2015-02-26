# -*- coding: utf-8 -*-

class Node:
# {{{ Node Class
    node_id = 0
    # records edges that are already created
    taken = []
    def __init__(self, name):
        if name not in Node.taken:
            self.name = name
            self.id = Node.node_id
            Node.node_id = Node.node_id + 1
            Node.taken.append(name)
        else:
            print "{} has been taken!".format(name)

    def __eq__(self, node):
        if self.name == node.name:
            return True
        else:
            return False

    # make Node objects hashable
    # (Act as dict keys)
    def __hash__(self):
        return self.id

    def __str__(self):
        return 'Node {}'.format(self.name)

    def __repr__(self):
        return 'Node {}'.format(self.name)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def copy(self):
        return Node(self.name)
# }}}
