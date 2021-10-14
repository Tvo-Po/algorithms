class NodeAlreadyExists(Exception):
    pass


class Node:
    """
    Representation of oriented graph Nodes
    :param self.name: The name of Node
    :param self.__connections: The dict of Nodes to which current connected
    """

    def __init__(self, name: str, connections: dict = {}):
        self.name = name
        self.__connections = {}
        for connect in connections:
            if isinstance(connect, Node):
                if self.__connections.get(connect):
                    raise NodeAlreadyExists('Node with this name already exists')
                else:
                    self.__connections[connect] = connections[connect]
            else:
                raise ValueError('Connections must be Node type')

    def __str__(self):
        node_amount = len(self.__connections)
        center = node_amount // 2
        name_length = len(self.name) + 1
        node_strings = [''] * node_amount
        for i, node in enumerate(self.__connections):
            node_strings[i] = ' ' * name_length + '-' + ' ' + node + '\n'
        node_map = ''
        if node_amount == 1:
            node_map = self.name + ' ' + node_strings[0].lstrip()
        elif node_amount == 0:
            node_map = self.name
        elif node_amount % 2 == 0:
            main_node_lain = self.name + ' ' + '\n'
            node_map = ''.join(node_strings[:center]) + main_node_lain + ''.join(node_strings[center:])
        else:
            node_strings[center] = self.name + ' ' + node_strings[center + 1].lstrip()
            node_map = ''.join(node_strings)
        return node_map

    def connect_with(self, other_node):
        """
        Connect current Node with other Nodes
        :return: None
        """
        if isinstance(other_node, Node):
            self.__connections.append(other_node)
            return Node('TemporaryNamedNode', self.__connections)
        else:
            raise ValueError('It\'s not a Node')

    @property
    def connection_list(self):
        return self.__connections


class Graph:

    def __init__(self):
        self.__node_list = []


if __name__ == '__main__':
    pass
