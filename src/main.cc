#include <iostream>
#include <Spectra/GenEigsSolver.h>
#include <Spectra/MatOp/SparseGenMatProd.h>
#include "include/parser.h"
// using namespace Spectra;

int main()
{
    std::string S_file, M_file, L_file;
    S_file = "../assets/S_soc-karate.mtx";
    M_file = "../assets/M_web-edu.csv";
    L_file = "../assets/L_tech-internet-as.mtx";

    Eigen::SparseMatrix<double> S_mat = parser::readMTXFile(S_file);
    // Eigen::SparseMatrix<double> * d = new Eigen::SparseMatrix<double>(data);
    Eigen::SparseMatrix<double> M_mat = parser::readCSVFile(M_file);
    Eigen::SparseMatrix<double> L_mat = parser::readMTXFile(L_file);

    Spectra::SparseGenMatProd<double> S_op(S_mat);
    Spectra::SparseGenMatProd<double> M_op(M_mat);
    Spectra::SparseGenMatProd<double> L_op(L_mat);

    // Construct eigen solver object, requesting the largest three eigenvalues
    Spectra::GenEigsSolver<Spectra::SparseGenMatProd<double>> S_eigs(S_op, 3, 6);
    Spectra::GenEigsSolver<Spectra::SparseGenMatProd<double>> M_eigs(M_op, 3, 6);
    Spectra::GenEigsSolver<Spectra::SparseGenMatProd<double>> L_eigs(L_op, 3, 6);

    // Initialize and compute
    S_eigs.init();
    M_eigs.init();
    L_eigs.init();
    int S_nconv = S_eigs.compute(Spectra::SortRule::LargestMagn);
    int M_nconv = M_eigs.compute(Spectra::SortRule::LargestMagn);
    int L_nconv = L_eigs.compute(Spectra::SortRule::LargestMagn);

    // Retrieve results
    Eigen::VectorXcd evalues;

    std::cout << "\nSmall : " << S_mat.nonZeros() / 2 << "\n";
    if (S_eigs.info() == Spectra::CompInfo::Successful)
        evalues = S_eigs.eigenvalues();
    std::cout << "Eigenvalues found for S :\n"
              << evalues << std::endl;

    std::cout << "\nMedium : " << M_mat.nonZeros() / 2 << "\n";
    if (M_eigs.info() == Spectra::CompInfo::Successful)
        evalues = M_eigs.eigenvalues();
    std::cout << "Eigenvalues found for M :\n"
              << evalues << std::endl;

    std::cout << "\nLarge : " << L_mat.nonZeros() / 2 << "\n";
    if (L_eigs.info() == Spectra::CompInfo::Successful)
        evalues = L_eigs.eigenvalues();
    std::cout << "Eigenvalues found for L :\n"
              << evalues << std::endl;


    return 0;
}