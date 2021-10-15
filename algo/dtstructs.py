class Connection:
    """
    Representation of connections between graphs.
    """

    class ConnectionError(Exception):
        pass

    def __init__(self, first_node, second_node, is_orient: bool = False):
        """
        Connect first node with second node.
        If orient, connection goes from first to second.
        """
        if isinstance(first_node, Node) and isinstance(second_node, Node):
            self.__first_end = first_node
            self.__second_end = second_node
            if is_orient:
                self.__orient_to = second_node
        else:
            raise ValueError('Ends of connection must be nodes')

    def remove_connection(self):
        """
        Remove connection between current nodes.
        """
        if self.__first_end and self.__second_end:
            self.__first_end = None
            self.__second_end = None
            self.__orient_to = None
            raise self.ConnectionError('You\'re trying to remove empty connection')
        else:
            self.__first_end = None
            self.__second_end = None
            self.__orient_to = None

    def reset_connection(self, first_node, second_node, is_orient: bool = False):
        """
        Reuse empty connection to connect first node with second node.
        If orient, connection goes from first to second.
        If connection not empty, raise error.
        """
        if self.__first_end or self.__second_end:
            raise self.ConnectionError('Connection already exists')
        if isinstance(first_node, Node) and isinstance(second_node, Node):
            self.__first_end = first_node
            self.__second_end = second_node
            if is_orient:
                self.__orient_to = second_node
        else:
            raise ValueError('Ends of connection must be nodes')

    def move_to_next(self, node):
        if not self.__orient_to:
            if node == self.__first_end:
                return self.__second_end
            elif node == self.__second_end:
                return self.__first_end
            else:
                raise self.ConnectionError('Given node doesn\'t belong to this connection')
        else:
            if node == self.__first_end:
                return self.__second_end
            elif node == self.__second_end:
                raise self.ConnectionError('Given node hasn\'t way back')
            else:
                raise self.ConnectionError('Given node doesn\'t belong to this connection')

    def __str__(self):
        if self.__orient_to:
            return self.__first_end.name + ' -> ' + self.__second_end.name
        else:
            return self.__first_end.name + ' - ' + self.__second_end.name


class Node:
    """
    Representation of graph Nodes.
    :param self.name: The name of Node.
    """

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Graph:

    def __init__(self, connections: dict, is_orient=False):
        self.__connections = {}
        for node_name in connections.keys():
            self.__connections[node_name] = (Node(node_name), [])
        for node_name, node_connections in connections.items():
            for connected_node in node_connections:
                if self.__connections.get(connected_node):
                    self.__connections[node_name][1].append(Connection(self.__connections[node_name],
                                                                       self.__connections[connected_node], is_orient))
                else:
                    raise ValueError('You didn\'t declare this node')


if __name__ == '__main__':
    print('Not valid. Reinventing bicycle...')
