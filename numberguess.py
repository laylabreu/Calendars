"""Practice with writing test cases and performing test-driven development using a
Guess-My-Number game as a problem statement.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Layla Abreu
"""

import random


def computerNumber():
    ''' This function SHOULD generate a random number in the 1-100 range 
    (inclusive), and return it'''
    return random.randint(1,100)
    # TODO: when testing this function, it can fails sometimes. Investigate why 
    # and fix the code to match the documentation of what the function should do.


def makeSmartGuess(lowest, highest, lastFeedback=None):
    ''' This function should make a smart guess within the given range and return it'''
    total =(lowest + highest)
    return total//2
    # TODO: code here AFTER making some tests (use Test-Driven Development)
    

def provideFeedback(guess, theNum):
    ''' This function should take as inputs the guess and the number from the computer,
    and will provide feedback as to whether the guess is too low, too high, or correct. 
    It should print the guess and feedback and then return the feedback'''
    if guess < theNum:
        return 'too low'
    elif guess> theNum:
        return 'too high'
    else: 
        return 'correct'
    # TODO: code here AFTER making some tests (use Test-Driven Development)


def gameLoop():
    ''' This function handles the main game loop, repeatedly calling the makeSmartGuess() and
    provideFeedback() functions until the guess is correct. When the guess is finally correct,
    it will return the number of guesses it took to find the answer. '''
    theNum = computerNumber()
    lowest = 1
    highest = 100
    tries = 0
    while True:
        guess= makeSmartGuess(lowest, highest)
        tries +=1
        feedback = provideFeedback(guess, theNum)
        if feedback =='too low':
            lowest = guess +1
        elif feedback == 'too high':
            highest =guess -1
        else:
            return tries
        
        
    # TODO: code here AFTER making some tests (use Test-Driven Development)


###############################################################
# Here is where you will write your basic test case functions
# Do NOT test provideFeedback here. That must go in the structured test further below
# If you wish, you can make all your tests here int the structured form.  

def testGeneratedNumber():
    for i in range(1000):
        aNum = computerNumber() ## calls the function we are testing
        # now verify that the function did as we expected:
        assert 1 <= aNum and aNum <= 100, "The computer generated a number out of valid range"
        # Often, we want to have very simple and direct tests
        # To improve the testing above, we might be do this instead:
        assert type(aNum) == type(1), "computerNumber() didn't generate an integer!"
        assert 1 <= aNum, "The computer generated a number that's too low"
        assert aNum <= 100, "The computer generated a number that's too high"
    # Why no output or return? Because we want fails to be loud, success is silent


## TODO: ADD MORE TEST FUNCTIONS HERE
# to fully test a function, we often need more than one test.  


###############################################################
# For large projects, structured testing like this is *necessary*

import unittest

class TestGuessMyNumber(unittest.TestCase):
    
   
    
    # Here is where you will write your structured tests for the provideFeedback function
    def testDemonstrationOfUnittesting(self):
        self.assertEqual(1, 1) # Placeholder example assertion which passes
        hasMessage = True
        self.assertTrue(hasMessage, "Here's the message if this test fails")
        # Actual tests should call a function, then assert/verify the results 
        # and changes from that function are what you expected
        
        # TODO: comment these out, they just demonstrate what test failures look like:
# =============================================================================
#         self.assertEqual(3, 7, "Demonstration purposes: test fails because 3 != 7")
#         self.fail("Here's a way to immediately fail a test!")
# =============================================================================
        
    # Here is where you will write your structured tests:
   
    
    def testMakeSmartGuessMiddle(self):
       self.assertEqual(makeSmartGuess(30, 70),50)
       hasMessage = True
       self.assertTrue(hasMessage, "Here's the message if this test fails")
   
    def testMakeSmartGuessInt(self):
       self.assertIsInstance(makeSmartGuess(30,70), int)
       hasMessage = True
       self.assertTrue(hasMessage, "Here's the message if this test fails")
    
    def testProvideFeedbackLow(self):
        # TODO: make this test!
        self.assertEqual(provideFeedback(66, 72), 'too low')
        hasMessage = True
        self.assertTrue(hasMessage, "Here's the message if this test fails")
        

    def testProvideFeedbackHigh(self):
        # TODO: make this test!
        self.assertEqual(provideFeedback(41,2), 'too high')
        hasMessage = True
        self.assertTrue(hasMessage, "Here's the message if this test fails")
        
    def testProvideFeedbackCorrect(self):
        self.assertEqual(provideFeedback(4,4), 'correct')
        hasMessage = True
        self.assertTrue(hasMessage, "Here's the message if this test fails")
        
    def testmakeSmartGuessfeedback(self):
        theNum = computerNumber()
        lowest = 1
        highest =100
        guess = makeSmartGuess(lowest, highest) 
        while guess != theNum:
            feedback = provideFeedback(guess, theNum)
            if feedback == 'too low':
                lowest = guess +1
            elif feedback =='too high':
                highest = guess -1
            else:
                pass
            guess2= makeSmartGuess(lowest, highest)
            self.assertNotEqual(guess2, guess, 'not same')  
            guess = guess2
        self.assertEqual(guess, theNum, 'same!')
   
               
    def testgameLoopEnd(self):
        self.assertGreater(gameLoop(), 0, 'one + attempts to complete')
    

        
        

    ### TODO: CREATE MORE TESTS HERE

    def aUtilityFunction(self, param):
        # This is a utility function which unittest.main() will NOT run automatically.
        # Your test functions could still use it though:  self.aUtilityFunction("hello")
        print("Utility function runs! Has parameter:", param)

###############################################################    

def main():
    print("Started basic testing...")
    # Call each one of your basic test functions first:
    testGeneratedNumber()
    # TODO: CALL MORE TEST FUNCTIONS
    print("Basic tests done and passed!")
    # Remember, if a basic assertion fails, no other tests will run.  
    # But for structured tests, every test is run and made into one big report
    
    print("Beginning structured tests...", flush=True)
    # This runs all methods in the TestGuessMyNumber that are named 'test...':
    unittest.main()
    print("Structured tests done (look above for report)")


if __name__ == "__main__":
    main()