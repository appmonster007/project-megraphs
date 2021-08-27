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
        std::ifstream in;
        in.open(fileName);
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
}