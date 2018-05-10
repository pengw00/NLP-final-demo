import re
import ipywidgets as widgets


class TestSaver:
    def __init__(self):
        self.cky_trees_path = 'cky_trees.txt'
        self.pcky_tree_path = 'pcky_tree.tsv'
        self.multiple_choice_path = 'multiple_choice.tsv'
        self.num_q = 8
        self.choices = {ex_id+1: None for ex_id in range(self.num_q)}
        self.questions = {ex_id+1: ['Option A', 'Option B', 'Option C', 'Option D'] for ex_id in range(self.num_q)}

    def save_choices(self):
        with open(self.multiple_choice_path, 'w+') as f:
            for i, ans in self.choices.items():
                if ans == None:
                    print("You did not select a choice on question {}".format(i))
                f.write("{}\t{}\n".format(i, ans))
        print('\nYour choices have been saved. You can overwrite your results by running this cell again.')

    def save_cky_trees(self, trees):
        flat_trees = [re.sub('\n+',' ', t if isinstance(t, str) else str(t)) for t in trees]
        flat_trees = [re.sub(' +',' ', t) for t in flat_trees]
        with open(self.cky_trees_path, 'w+') as f:
            for tree in flat_trees:
                f.write('{}\n'.format(tree))
        print('Your trees have been saved. You can overwrite your results by running this function again.')

    def save_pcky_tree(self, tree, prob):
        t = tree if isinstance(tree, str) else str(tree)
        t = re.sub('\n+',' ', t)
        t = re.sub(' +',' ', t)
        with open(self.pcky_tree_path, 'w+') as f:
            f.write('{}\t{}\n'.format(t, prob))
        print('Your tree has been saved. You can overwrite your results by running this function again.')

    def show_choices(self):
        for i, ans in self.choices.items():
            print("{} -> {}".format(i, chr(64+ans) if ans else None))
            
            
class TestManager:
    def __init__(self):
        self.test_saver = TestSaver()
        self.dropdowns = [self.create_dropdown(ex_id, options) for ex_id, options in self.test_saver.questions.items()]
    
    def display(self, ex_id):
        display(self.dropdowns[ex_id-1])
    
    def save_choices(self):
        self.test_saver.save_choices()
        
    def save_cky_trees(self, trees):
        self.test_saver.save_cky_trees(trees)
        
    def save_pcky_tree(self, tree, prob):
        self.test_saver.save_pcky_tree(tree, prob)
        
    def show_choices(self):
        self.test_saver.show_choices()
    
    def create_dropdown(self, ex_id, options, description='Your choice:'):
        w = widgets.Dropdown(
            options=['-- Select one'] + options,
            description=description)
        def on_change(change):
            if change['type'] == 'change' and change['name'] == 'value':
                new_index = change['owner'].index
                self.test_saver.choices[ex_id] = new_index if new_index else None
        w.observe(on_change)
        return w