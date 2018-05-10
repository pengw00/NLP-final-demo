import numpy as np

class Grader:
    def __init__(self):
        self._total_points = 0
        self._total_percent = 0.0
        self._percentage = 1.0
        self._solutions = {}
        self._evaluators = {
            'ex_1': self._ex11,
            'ex_2': self._ex12,
            'ex_3': self._ex13,
            'ex_4': self._ex14,
            'ex_5': self._ex15,
            'ex_6': self._ex16,
            'ex_7': self._ex17,
            'ex_8': self._ex18,
            'ex_9': self._ex19,
            'ex_10': self._ex110,
            'ex_11': self._ex111,
        }
        self._points = {
            'ex_1': 3,  # for tokenizing data
            'ex_2': 2,  # for getting the vocabulary
            'ex_3': 3,  # for getting the prior probs
            'ex_4': 3,  # for counting occurrences
            'ex_5': 4,  # for counting label occurrences
            'ex_6': 3,  # for calculating the likelihood prob
            'ex_7': 2,  #
            'ex_8': 3,
            'ex_9': 3,
            'ex_10': 1,
            'ex_11': 2,
        }
    
    def get_grade(self):
        return self._total_percent
    
    def set_solution(self, ex_name, solution):
        if ex_name in self._points:
            if callable(solution):
                self._solutions[ex_name] = solution
            else:
                self._solutions[ex_name] = lambda: solution
            # print('{}:\t {} pts earned'.format(ex_name, self._evaluators[ex_name]()))
    
    def _ex11(self):
        question = 'Testing capital the lEtters ! 12; ,'
        expected = ['testing', 'capital', 'letters', '12;']
        solution = self._solutions['ex_1']
        if expected == solution(question):
            return self._points['ex_1']
        return 0
    
    def _ex12(self):
        solution = self._solutions['ex_2']()
        if len(solution) == 16374:
            return self._points['ex_2']
        return 0
    
    def _ex13(self):
        question = 'a a a a a a b b b b'.split()
        solution = self._solutions['ex_3'](question)
        if solution['a'] == 0.6 and solution['b'] == 0.4:
            return self._points['ex_3']
        return 0
    
    def _ex14(self):
        solution = self._solutions['ex_4']()
        if len(solution) == 28425:
            return self._points['ex_4']
        return 0
    
    def _ex15(self):
        question = {'0': 380571, '1': 190057}
        solution = self._solutions['ex_5']()
        if solution == question:
            return self._points['ex_5']
        return 0
    
    def _ex16(self):
        probs = [0.0008155448102411381, 0.00018918940224031783, 0.0, 0.0]
        pairs = [('fine', '1'), ('fine', '0'), ('the', '1'), ('of', '1')]
        solution = [self._solutions['ex_6'](*pair) for pair in pairs]
        if solution == probs:
            return self._points['ex_6']
        return 0
    
    def _ex17(self):
        prob = 0.000755700451967001
        pair = 'fine', '1'
        solution = self._solutions['ex_7'](*pair)
        if solution == prob:
            return self._points['ex_7']
        return 0

    #################################################################
    def _ex18(self):
        question = 'this is a good review'.split()
        expected = [-55.036783629100135, -54.86062843180087]
        solution = [self._solutions['ex_8'](question, '0'), self._solutions['ex_8'](question, '1')]
        if solution == expected:
            return self._points['ex_8']
        return 0
    #################################################################

    def _ex19(self):
        questions = ['this is a good review'.split(), 'this is a bad review'.split()]
        expected = ['1', '0']
        solution = [self._solutions['ex_9'](sent) for sent in questions]
        if solution == expected:
            return self._points['ex_9']
        return 0
    
    def _ex110(self):
        question = ['this is a good review'.split(), 'this is a bad review'.split()]
        expected = ['1', '0']
        solution = self._solutions['ex_10'](question)
        if solution == expected:
            return self._points['ex_10']
        return 0
    
    def _ex111(self):
        y_pred = [0, 2, 1, 3]
        y_true = [0, 1, 2, 3]
        solution = self._solutions['ex_11']
        if solution(y_true, y_pred) == 0.5:
            return self._points['ex_11']
        return 0
    
    def grade(self):
        total = sum(self._points.values())
        right = 0
        
        for ex_name, ex_points in self._points.items():
            if ex_name not in self._evaluators:
                print('WARNING: solution {} has not been set'.format(ex_name))
                
            elif callable(self._evaluators[ex_name]):
                award = self._evaluators[ex_name]()  
                print('{}:\t{} / {}'.format(ex_name, award, ex_points))
                right += award
            
        
        self._total_points = right
        self._total_percent = round(100 * self._percentage * self._total_points / total, 2)
        
        print('\nTOTAL:\t{} / {}\n'.format(self._total_points, total))
        print('FINAL GRADE: {}'.format(self._total_percent))
