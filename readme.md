# Base bdd setup
This base setup includes the mamba bdd test runner for using gherkin style syntax (Given, when then) at unit test level.
By first defining the expected behavior with a failing test, fixing the software to make the test succeed and refactor this code we can achieve 100% behaviour coverage.

This way of developing software might seem tedious at first but by having the itterative and incremental way of working we reduce the amount of code written that is actually not needed.
A second important aspect of developing software will araise sooner; making proper design choices.
By having to define behaviour instead of simple function we require to really think about the design, by constantly refactoring we have the opportunity to work towards the best suited design.


# Setup explained
In this setup we use bash script to reduce the complexity of our make file.
The Makefile is used to facilitate local development regardless of IDE and use of this within the online replit.com IDE.
This is a Python setup using Mamba as a test runner, Expects for asserions and Coverage for a code coverage report.

## Important files
**.coveragerc:**
> is used to specify the files included (source) and excluded (omit) in the code coverage.

**specs:**
> holds all our unit test files, these are run with the run_tests.sh

**package:**
> holds our source code, when extending or renaming these make sure to update **.coveragerc**

# Running things

Within replit you can click the Run button to activate the unit tests and updating the coverage report.
The same can be achieved by running the command:  
``` bash
$ make
```

To launch a local local webserver to view the code coverage give the command:

``` bash
$ make serve
```

