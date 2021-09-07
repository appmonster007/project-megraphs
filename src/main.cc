#include <iostream>
#include "include/parser.h"

int main() {
    std::string fileName("tech-internet-as.mtx");
    Eigen::SparseMatrix<double> data = parser::readMTXFile(fileName);
    Eigen::SparseMatrix<double> * d = new Eigen::SparseMatrix<double>(data);
    fileName = "csvfile.csv";
    Eigen::SparseMatrix<double> dat = parser::readCSVFile(fileName);
    return 0;
}