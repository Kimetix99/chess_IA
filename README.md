# Chess_IA

Chess Software with an AI to play against.

## Usage

$ python Chess.py

## Technics

The following algorithms have been used to perform this Artificial Intelligence:

* Minimax
* Alpha-Beta Pruning
* Neightboor Search

## Explanation

In this project I tried to make an AI capable of running on my computer. The typical practice when doing this type of chess AI is to use the minimax algorithm together with alpha-beta pruning. Even so, if you want the AI ​​to make a prediction of a possible movement that you can make, the computational cost is still very large due to the number of different situations that exist in each state of the game.

For this reason, I have combined these two algorithms with a neightboor search algorith with which we make N random evaluations for each state of the game. This N is equivalent to the ramification factor, so I can control how much the tree expands at each prediction level.

In order to do it as quickly as possible, in the search for neighbors, evaluations can be repeated, since in the end the objective is to make the maximum number of evaluations possible in a reasonable time.
