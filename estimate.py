import math
import unittest

# Wallis Function

def wallis(n):
    pi = 1
    pi *= 4 * n ** 2 / (4 * n ** 2  - 1.)
    return(pi)


class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            pi *= 2
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            pi *= 2
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")




#Monte_Carlo

def monte_carlo(INTERVAL):

    import random
    
    circle_points = 0
    square_points = 0
    # Total Random numbers generated= possible x
    # values* possible y values
    for i in range(INTERVAL**2):
  
        # Randomly generated x and y values from a
        # uniform distribution
        # Rannge of x and y values is -1 to 1
        rand_x= random.uniform(0, 1)
        rand_y= random.uniform(0, 1)
  
        # Distance between (x, y) from the origin
        origin_dist= rand_x**2 + rand_y**2
  
        # Checking if (x, y) lies inside the circle
        if origin_dist<= 1:
            circle_points+= 1
  
        square_points+= 1
  
        # Estimating value of pi,
        # pi= 4*(no. of points generated inside the 
        # circle)/ (no. of points generated inside the square)
        pi = 4* circle_points/ square_points
  
    ##    print(rand_x, rand_y, circle_points, square_points, "-", pi)
    ##    print("\n")
  
    return(pi)  


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
