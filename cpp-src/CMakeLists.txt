cmake_minimum_required(VERSION 3.0.1)
project(Main VERSION 0.1.0)

add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_subdirectory(include)

add_executable(Main main.cc)
# target_include_directories(Main PUBLIC include)
target_link_libraries(Main PUBLIC include ${CONAN_LIBS})
