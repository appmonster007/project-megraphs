cmake_minimum_required(VERSION 3.0.1)
project(Main)

add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_subdirectory(include)

add_executable(Main main.cc include/parser.h include/parser.cc)
target_include_directories(Main PUBLIC include)
target_link_libraries(Main PUBLIC ${CONAN_LIBS})
