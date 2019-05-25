cmake_minimum_required(VERSION 3.0.0)
project(capture4 VERSION 0.1.0)

include(CTest)
enable_testing()

# project include directory
include_directories(include)

aux_source_directory(src DIR_SRCS)
link_directories(lib)
link_libraries(libglfw3.a)

add_executable(capture4 ${DIR_SRCS})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
