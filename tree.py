import random

def generate_data():
    return random.random()


tree = {}
def add_to_tree(tree_node, name):
    tree_node['id'] = name
    tree_node['data'] = generate_data()
    tree_node['children'] = {}


add_to_tree(tree)
print(tree)
add_to_tree(tree['children'])
print(tree)






tree_demonstrator = {'data': generate_data(),
                    'children': {'data': generate_data(),
                                'children': {'data': generate_data(),
                                            'children': None}}}