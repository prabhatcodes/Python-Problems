# https://media.discordapp.net/attachments/511344208955703306/769965174211346472/pipe_types.png?width=360&height=47

# Hell Challenge
# Alex always adored playing video games. Today he finally decided to write his own version of the legendary game from scratch.
#
# In this game the player has to place the pipes on a rectangular field to make water pour from each source to a respective sink. He has already come up with the entire program, but one question still bugs him: how can he best check that the arrangement of pipes is correct?
#
# It's your job to help him figure out exactly that.
#
# Alex has 7 types of pipes in his game, with numbers corresponding to each type:
#
# 1 - vertical pipe
# 2 - horizontal pipe
# 3-6 - corner pipes
# 7 - two pipes crossed in the same cell (note that these pipes are not connected)
# Here they are, pipes 1 to 7, respectively:
#
# Images Below
#
# Water pours from each source in each direction that has a pipe connected to it (thus it can even pour in all four directions). The puzzle is solved correctly only if all water poured from each source eventually reaches a corresponding sink.
#
# Help Alex check whether the arrangement of pipes is correct. If it is correct, return the number of cells with pipes that will be full of water at the end of the game. If not, return -X, where X is the number of cells with water before the first leakage point is reached, or if the first drop of water reaches an incorrect destination (whichever comes first). Assume that water moves from one cell to another at the same speed.
# Example:
# for
#  state = ["a224C22300000",
#  "0001643722B00",
#  "0b27275100000",
#  "00c7256500000",
#  "0006A45000000"]
#
# the output should be solution(state) = 19
# Submission and grading
# - code must be written in python
# - code must be in a function named solution
# - function must take in one array of strings argument
# - function must return an integer
# - no imports/libraries allowed

