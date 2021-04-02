# Product Name

> Markov library is implementation of markov-chains algorithm.

In markov we have n different states. Transitions happens between different states. We create a graph with probability of transitions from one state to all possible states using the path data available. Next we use removal effect, which gives us the relative importance of each and every state. Using those relative importance values we can optimize other metrics which are related to those states.

Example: We first used markov models in calculations of marketting attribution. Steps are as follows:

1. Create a dataframe with 2 columns 'path' and 'conversions'.
2. In path add the user journey for ex- youtube -> google -> youtube.
3. Add respective number of conversions which were achieved though that path ex- 3.
4. Create the state's graph with probabilities using conversions columns.
5. Use removal effect using matrix manipulations and get the relative importance of the states.(In our example it's the channels)
6. Use this information to optimize the marketing budget.

## Test data

OS X & Linux:

    1. cd data
    2. python3 get_test_data.py

## Release History

- 1.0.0
  - ADD: Initial module added first version launched

## Meta

Saurabh Waradkar – waradkarsaurabh@gmail.com
Rishabh Bhardwaj – [@rishabhb932](https://twitter.com/rishabhb932) – rishabhb932@gmail.com

Distributed under the GPL-3 license. See `LICENSE` for more information.
