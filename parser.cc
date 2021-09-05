#include<string>
#include<iterator>
#include<fstream>
#include<vector>
#include "parser.h"
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
    std::vector<std::vector<std::string>> readCSVFile(std::string &fileName) {
        std::ifstream in(fileName);
        std::vector<std::vector<std::string>> table;
        std::string row;
        while (!in.eof()) {
            std::getline(in, row);
            if (in.bad() || in.fail()) {
                break;
            }
            auto fields = readCSVRow(row);
            table.push_back(fields);
        }
        return table;
    }
    std::vector<std::vector<double>> readMTXFile(std::string & fileName) {
        long rows, columns, lines;
        std::ifstream in(fileName);
        while (in.peek() == '%')
            in.ignore(2048, '\n');
        in >> rows >> columns >> lines;
        std::vector<std::vector<double>> matrix(rows, std::vector<double> (columns, 0));
        for (int i = 0; i < lines; i++)
        {
            double data;
            double row, col;
            in>>row>>col>>data;
            matrix[row-1][col-1] = data;
        }
        in.close();
        return matrix;
    }
}