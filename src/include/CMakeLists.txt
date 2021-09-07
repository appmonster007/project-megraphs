add_library(parser parser.cc)
target_include_directories(parser PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
# set_target_properties(parser PROPERTIES LINKER_LANGUAGE C++)
