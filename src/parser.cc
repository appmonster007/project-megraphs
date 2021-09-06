#include<string>
#include<iterator>
#include<fstream>
#include<vector>
#include "include/parser.h"
namespace parser {
    std::vector<std::string> readCSVRow(const std::string &row) {
        CSVState state = CSVState::UnquotedField;
        std::vector<std::string> fields {""};
        size_t i = 0; // index of the current field
        for (char c : row) {
            switch (state) {
                case CSVState::UnquotedField:
                    switch (c) {
                        case ',': // end of field
                                fields.push_back(""); i++;
                                break;
                        case '"': state = CSVState::QuotedField;
                                break;
                        default:  fields[i].push_back(c);
                                break; }
                    break;
                case CSVState::QuotedField:
                    switch (c) {
                        case '"': state = CSVState::QuotedQuote;
                                break;
                        default:  fields[i].push_back(c);
                                break; }
                    break;
                case CSVState::QuotedQuote:
                    switch (c) {
                        case ',': // , after closing quote
                                fields.push_back(""); i++;
                                state = CSVState::UnquotedField;
                                break;
                        case '"': // "" -> "
                                fields[i].push_back('"');
                                state = CSVState::QuotedField;
                                break;
                        default:  // end of quote
                                state = CSVState::UnquotedField;
                                break; }
                    break;
            }
        }
        return fields;
    }
    Eigen::SparseMatrix<double> readCSVFile(std::string &fileName) {
        std::ifstream in(fileName);
        std::vector<std::vector<std::string>> table;
        std::string row;
        long int max = 0;
        std::getline(in, row);
        while(!in.eof()) {
            std::getline(in, row);
            if(in.bad() || in.fail()) {
                break;
            }
            auto fields = readCSVRow(row);
            if(std::stol(fields[0]) > max) {
                max = std::stol(fields[0]);
            }
        }
        Eigen::SparseMatrix<double> matrix(max, max);
        in.close();
        in.open(fileName);
        std::getline(in, row);
        while (!in.eof()) {
            std::getline(in, row);
            if (in.bad() || in.fail()) {
                break;
            }
            auto fields = readCSVRow(row);
            matrix.insert(stol(fields[0]), std::stol(fields[1])) = std::stod(fields[3]);
        }
        return matrix;
    }
    Eigen::SparseMatrix<double> readMTXFile(std::string & fileName) {
        long rows, columns, lines;
        std::ifstream in(fileName);
        while (in.peek() == '%')
            in.ignore(2048, '\n');
        in >> rows >> columns >> lines;
        Eigen::SparseMatrix<double> matrix(rows, columns);
        for (int i = 0; i < lines; i++)
        {
            double data;
            double row, col;
            in>>row>>col>>data;
            matrix.insert(row, col) = data;
        }
        in.close();
        return matrix;
    }
}