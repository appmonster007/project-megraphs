#ifndef PARSER_H_
#define PARSER_H_
#include<string>
#include<iterator>
#include<fstream>
#include<vector>
#include <Eigen/Sparse>
namespace parser {
    enum class CSVState {
        UnquotedField,
        QuotedField,
        QuotedQuote
    };
    std::vector<std::string> readCSVRow(const std:: string& row);
    Eigen::SparseMatrix<double> readCSVFile(std::string & fileName);
    Eigen::SparseMatrix<double> readMTXFile(std::string & fileName);
}

#endif