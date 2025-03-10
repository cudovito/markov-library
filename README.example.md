# Product Name

> Markov library is implementation of markov-chains algorithm.

<!-- [![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url] -->

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

<!-- ![](header.png) -->
<!--
## Installation

OS X & Linux:

```sh
npm install my-crazy-module --save
```

Windows:

```sh
edit autoexec.bat
``` -->

<!-- ## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots. -->

<!-- _For more examples and usage, please refer to the [Wiki][wiki]._ -->

<!-- ## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
``` -->

## Release History

- 1.0.0
  - ADD: Initial module added first version launched

<!-- - 0.2.0
  - CHANGE: Remove `setDefaultXYZ()`
  - ADD: Add `init()`
- 0.1.1
  - FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
- 0.1.0
  - The first proper release
  - CHANGE: Rename `foo()` to `bar()`
- 0.0.1
  - Work in progress -->

## Meta

Saurabh Waradkar – waradkarsaurabh@gmail.com
Rishabh Bhardwaj – [@rishabhb932](https://twitter.com/rishabhb932) – rishabhb932@gmail.com

Distributed under the GPL-3 license. See `LICENSE` for more information.

<!-- [https://github.com/yourname/github-link](https://github.com/dbader/) -->

<!-- ## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request -->

<!-- Markdown link & img dfn's -->
<!--
[npm-image]: https://media-exp1.licdn.com/dms/image/C4D0BAQGb8yrF0eThYQ/company-logo_200_200/0/1598708345771?e=1625702400&v=beta&t=w7R7JyoBRUSQCBxg-tY5x47aeYPz5QhLPX80nCfosdU -->

<!-- [npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki -->
