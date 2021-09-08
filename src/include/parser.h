#ifndef PARSER_H_
#define PARSER_H_
#include <string>
#include <iterator>
#include <fstream>
#include <vector>
#include <Eigen/Sparse>
#include <Eigen/Dense>
namespace parser
{
    enum class CSVState
    {
        UnquotedField,
        QuotedField,
        QuotedQuote
    };
    std::vector<std::string> readCSVRow(const std::string &row);
    Eigen::SparseMatrix<double> readCSVFile(std::string &fileName);
    Eigen::MatrixXd readCSVFiletoDense(std::string &fileName);
    Eigen::SparseMatrix<double> readMTXFile(std::string &fileName);
    Eigen::SparseMatrix<double> readMTXFile(std::string &fileName, int mode);
    Eigen::MatrixXd readMTXFiletoDense(std::string &fileName);
}

#endif