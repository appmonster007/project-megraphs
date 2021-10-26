# Code Specification
I was hoping we could have one file to document the code spec we wil be using, so let's start here. I had thought of this proposal for our cleaning up some of the clutter with the code

## Project Layout
- Project root
    - README.md
    - SPEC.md
    - assets
        - *Individual graph files*
    - src
        - Notebooks
            - *ipynb files*
        - Python
            - *python files*
    - License
    - Makefile (*Do we need one?*)
    - .gitignore

## Code layout
For the code I thought of having the very basic graph functions in a ```GraphBase``` class. The ```GraphBase``` class will be simple and will only provide us with functionality that we might want to use on multiple graphs  for multiple purposes. Eg: reading from file, writing details to files etc etc. At the very least these two operations should be supported in one form or another.

For centrality computation we could separate individual centralities into multiple files (if they are too complex) or group them all into a single ```Centrality.py``` file as long as the file remains readable.

## Current Status
We can use this section to mantain docs of the current state of the program. The first paragraph can serve as a suimmary of recent changes to the codebase while small tldr style docs can be added below.

### Available Functionality
- Graph Base class
    - (Proposed)
- Centralities
    - (Proposed)
