#include <iostream>
// #include <Eigen/Eigenvalues>
#include <Spectra/GenEigsSolver.h>
#include <Spectra/SymEigsSolver.h>
#include <Spectra/MatOp/SparseGenMatProd.h>
#include <Spectra/MatOp/SparseSymMatProd.h>
#include "include/parser.h"
// using namespace Spectra;

int main()
{
    std::string S_file, M_file, L_file;
    S_file = "../assets/S_soc-karate.mtx";
    M_file = "../assets/M_web-edu.csv";
    L_file = "../assets/L_tech-internet-as.mtx";

    // Eigen::MatrixXd S_mat = Eigen::MatrixXd::Zero(10, 10);
    // for(int i=0; i<10; i++){
    //     for(int j=0; j<10; j++){
    //         S_mat(i, j) = 1;
    //     }
    // }

    // Eigen::MatrixXd S_mat = parser::readMTXFiletoDense(L_file);
    Eigen::MatrixXd S_mat = parser::readCSVFiletoDense(M_file);
    // std::cout << S_mat << "\n";
    Eigen::EigenSolver<Eigen::MatrixXd> es(S_mat, false);
    std::cout << "The eigenvalues of the 10x10 matrix of ones are:" 
     << std::endl << es.eigenvalues() << std::endl;

    // // Eigen::SparseMatrix<double> * d = new Eigen::SparseMatrix<double>(data);
    // Eigen::SparseMatrix<double> M_mat = parser::readCSVFile(M_file);
    // Eigen::SparseMatrix<double> L_mat = parser::readMTXFile(L_file);

    // Spectra::SparseGenMatProd<double> XS_op(XS_mat);
    // Spectra::SparseSymMatProd<double> S_op(S_mat);
    // Spectra::SparseSymMatProd<double> M_op(M_mat);
    // Spectra::SparseSymMatProd<double> L_op(L_mat);

    // Construct eigen solver object, requesting the largest three eigenvalues
    // Spectra::GenEigsSolver<Spectra::SparseGenMatProd<double>> XS_eigs(XS_op, 8, 10);
    // Spectra::SymEigsSolver<Spectra::SparseSymMatProd<double>> S_eigs(S_op, 33, 34);
    // Spectra::SymEigsSolver<Spectra::SparseSymMatProd<double>> M_eigs(M_op, 3, 6);
    // Spectra::SymEigsSolver<Spectra::SparseSymMatProd<double>> L_eigs(L_op, 3, 6);

    // Initialize and compute
    // XS_eigs.init(); 
    // S_eigs.init();
    // M_eigs.init();
    // L_eigs.init();

    // int XS_nconv = XS_eigs.compute(Spectra::SortRule::LargestReal);
    // int S_nconv = S_eigs.compute(Spectra::SortRule::LargestMagn);
    // int M_nconv = M_eigs.compute(Spectra::SortRule::LargestMagn);
    // int L_nconv = L_eigs.compute(Spectra::SortRule::LargestMagn);

    // Retrieve results
    // Eigen::VectorXcd evalues;

    // std::cout << XS_mat;
    // std::cout << "\nX Small : " << XS_mat.nonZeros()<< "\n\n";
    // std::cout << XS_eigs.eigenvectors() << "\n";
    // if (XS_eigs.info() == Spectra::CompInfo::Successful)
    //     evalues = XS_eigs.eigenvalues();
    // std::cout << "Eigenvalues found for XS :\n"
    //           << evalues << std::endl;

    // std::cout << "\nSmall : " << S_mat.nonZeros() / 2 << "\n";
    // std::cout << S_eigs.eigenvectors() << "\n";
    // if (S_eigs.info() == Spectra::CompInfo::Successful)
    //     evalues = S_eigs.eigenvalues();
    // std::cout << "Eigenvalues found for S :\n"
    //           << evalues << std::endl;

    // std::cout << "\nMedium : " << M_mat.nonZeros() / 2 << "\n";
    // if (M_eigs.info() == Spectra::CompInfo::Successful)
    //     evalues = M_eigs.eigenvalues();
    // std::cout << "Eigenvalues found for M :\n"
    //           << evalues << std::endl;

    // std::cout << "\nLarge : " << L_mat.nonZeros() / 2 << "\n";
    // if (L_eigs.info() == Spectra::CompInfo::Successful)
    //     evalues = L_eigs.eigenvalues();
    // std::cout << "Eigenvalues found for L :\n"
    //           << evalues << std::endl;

    return 0;
}