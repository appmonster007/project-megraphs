#ifndef PARSER_H_
#define PARSER_H_
#include<string>
#include<iterator>
#include<fstream>
#include<vector>
// #include "edge_list.hpp"
// #include "adjacency_list.hpp"
// #include "adjacency_matrix.hpp"
namespace parser {
    enum class CSVState {
        UnquotedField,
        QuotedField,
        QuotedQuote
    };
    std::vector<std::string> readCSVRow(const std:: string& row);
    std::vector<std::vector<std::string>> readCSVFile(std::string & fileName);
    std::vector<std::vector<double>> readMTXFile(std::string & fileName);
}

#endif