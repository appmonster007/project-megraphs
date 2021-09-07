#include <iostream>
#include "include/parser.h"

int main() {
    std::string fileName("soc-karate.mtx");
    Eigen::SparseMatrix<double> data = parser::readMTXFile(fileName);
    Eigen::SparseMatrix<double> * d = new Eigen::SparseMatrix<double>(data);
    fileName = "csvfile.csv";
    Eigen::SparseMatrix<double> dat = parser::readCSVFile(fileName);
    std::cout<<data;
    return 0;
}