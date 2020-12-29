#Gomoku
##Iteration 1
Starting with the Game
First part of the Game is the Board
We need to be able to put Pieces on the Board
We must be able to detect wins
Once a piece is in you can't change it

Have the GUI fit the internals and not the other way around.
Because the GUI will keep changing.

How do we want to represent the board?
- We can have a dictionary with keys the coordinates and the values the players

Build something to verify very quickly. Remember TDD is all about instant feedback.

##Iteration 2
Testing stone placements at board bounds
High levels must dominate low levels
Its better to let the exception happen at run time and deal with it

We want to be able to detect a win
Is this something that the board must do? Or a higher level policy
A higher level policy, so that board can be reusable if need be

test_names = the given condition(setup)_assertion you are making


###Rules and the board
- the board has the rules
- the rules has the board
- the rules gets passed the board everytime rules need to be decided

If rules are hold onto the board
- You can't call the rules function with any other boards, imagine a stack of board for which
we need to determine a win quickly.

For now we can keep our options open

Rules could be just a bunch of methods, however, it feels like the rules will have local state, in which case
it is best to have instances of the rules.

###Policy
Low level policy for detecting win/loss -> gomoku rules
High level policy for managing turns -> game procedures

These policies are kept separate, so that if one changes the other is not affected.
But still one of them has to know about the other, so what is the direction of the
dependency?

The direction of dependency is a function of which is policy and which is a low level detail.

###Model View Presenter
The core idea behind the presenter is to allow testing without getting into the screen.\
When writing code which is testable, it is more about the design of the code rather than testability
