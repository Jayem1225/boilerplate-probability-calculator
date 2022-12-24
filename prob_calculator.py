import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for ball_type, count in kwargs.items():
            self.contents += [ball_type] * count
    
    def draw(self, count):
        drawn = []
        for i in range(count):
            if not self.contents:
                break
            ran_index = random.randrange(0, len(self.contents))
            drawn.append(contents.pop(ran_index))
        return drawn
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_passed = 0
    for i in range(num_experiments):
        test_passed = True
        test_hat = copy(hat)
        drawn = test_hat.draw(num_balls_drawn)
        draw_counts = {
            ball: 0
            for ball in set(drawn)
        }
        for ball in drawn:
            draw_counts[ball] += 1
        for ball, count in draw_counts.items():
            if expected_balls[ball] > draw_counts[ball]:
                test_passed = False
        if test_passed:
            count_passed += 1
            
     return count_passed/num_experiments
        
