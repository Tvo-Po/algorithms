from collections import deque


def breadth_first_search(graph: dict, item: str, is_needed_item):
    search_queue = deque()
    search_queue += graph[item]['connections']
    searched = []
    while search_queue:
        check_item = search_queue.popleft()
        if check_item not in searched:
            if is_needed_item(graph[check_item]['properties']):
                return check_item
            else:
                search_queue += graph[check_item]['connections']
                searched.append(check_item)
    return None


if __name__ == '__main__':
    graph = {
        "Doug": {
            "connections": ["Alice", "Bob", "Claire"],
            "properties": "postman",
        },
        "Alice": {
            "connections": ["Peggy"],
            "properties": "postman",
        },
        "Bob": {
            "connections": ["Peggy", "Anuj"],
            "properties": "dentist",
        },
        "Claire": {
            "connections": ["Jonny", "Tom"],
            "properties": "shopper",
        },
        "Anuj": {
            "connections": [],
            "properties": "businessman",
        },
        "Peggy": {
            "connections": [],
            "properties": "mango_seller",
        },
        "Tom": {
            "connections": [],
            "properties": "carpenter",
        },
        "Jonny": {
            "connections": [],
            "properties": "painter",
        },
    }

    def find_profession(item_property):
        return item_property == "dentist"

    print(breadth_first_search(graph, "Doug", find_profession))
