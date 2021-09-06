#include <iostream>
#include "include/parser.h"

int main() {
    std::string fileName("tech-internet-as.mtx");
    parser::readMTXFile(fileName);
    return 0;
}