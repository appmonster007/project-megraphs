#include<string>
#include<iterator>
#include<fstream>
#include<iostream>
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
        Eigen::SparseMatrix<double> matrix(max+1, max+1);
        in.close();
        in.open(fileName);
        std::getline(in, row);
        while (!in.eof()) {
            std::getline(in, row);
            if (in.bad() || in.fail()) {
                break;
            }
            auto fields = readCSVRow(row);
            if(matrix.coeff(stol(fields[0]), std::stol(fields[1])) == 0)
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
        Eigen::SparseMatrix<double> matrix(rows+1, columns+1);
        for (int i = 0; i < lines; i++)
        {
            double data;
            long int row, col;
            in>>row>>col>>data;
            if (matrix.coeff(row, col) == 0)
                matrix.insert(row, col) = data;
        }
        in.close();
        return matrix;
    }
}