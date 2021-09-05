#include <iostream>

#define __HERODOTOS_IMPLEMENTATION__
#include "../include/herodotos.hpp"

int main() {
    info((char *)"This is some debugging information", stdout);
    warn((char *)"This is a warning", stderr);
    error((char *)"This is an error", stderr);
    return 0;
}