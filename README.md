# project-megraphs
Multi edge graphs: synthetic edges for noise reduction and improved community detection in networks

## Collaborators
<a href="https://github.com/appmonster007/project-megraphs/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=appmonster007/project-megraphs" />
</a>

Made with [contributors-img](https://contrib.rocks).

## Notes

### Header Only Libraries
- Managing header and source files across versions can be pain, so we suggest the idea of using header only libraries
- herodotos.hpp is a simple logging utility which can be found in the include folder and can be used as a template to write more header only libraries
- Advantages of header only libraries, no need to worry about managing .hpp and .cc files separately, no complex build process, just include and remember to use the implementation, it's so simple?

### The EdgeList implementation
- Storing the matrix is becoming an issue, instead of storing whole matrices, we experiment with storing just edge lists (as are provided in the file) and try to perform computations on the fly
- Results: Takes ~40s to compute second order degree of every vertex of the large graph. I feel this is not fast enough since degree computation, simple as it is is taking a while. On the positive side, storage requirement is absolutely tiny, maybe a sorted edge list with an index and skip pointers is an idea?
- The EdgeList implementation is a WIP, so I haven't included it in the standard build process, anyone who wants to play around, can directly play around using the code at src/EdgeList.c (yes, it is a .c file). 

### Install conan
- refer to this link to [get started](https://docs.conan.io/en/latest/getting_started.html)

### Build excutable

- For 1st time
```sh
% mkdir build && cd build
% conan install ../src --build=missing 
% cmake ../src -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=[DEBUG|RELEASE]
% cmake --build .
% ./bin/<projectName>
```
