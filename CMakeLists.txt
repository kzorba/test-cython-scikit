cmake_minimum_required(VERSION 3.15...3.30)
project(${SKBUILD_PROJECT_NAME} LANGUAGES C)

find_package(
  Python
  COMPONENTS Interpreter Development.Module
  REQUIRED)

add_custom_command(
  OUTPUT "${CMAKE_CURRENT_SOURCE_DIR}/src/cmod.c"
  COMMENT
    "Making ${CMAKE_CURRENT_BINARY_DIR}/src/cmod.c from ${CMAKE_CURRENT_SOURCE_DIR}/src/cmod.pyx"
  COMMAND Python::Interpreter -m cython
          "${CMAKE_CURRENT_SOURCE_DIR}/src/cmod.pyx"
            --output-file "${CMAKE_CURRENT_SOURCE_DIR}/src/cmod.c"
  DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/src/cmod.pyx"
  VERBATIM)

Python_add_library(cmod MODULE WITH_SOABI
  "${CMAKE_CURRENT_SOURCE_DIR}/src/cmod.c"
  "${CMAKE_CURRENT_SOURCE_DIR}/src/util.c")

target_include_directories(cmod PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/src")

install(TARGETS cmod DESTINATION ${SKBUILD_PROJECT_NAME})
