# Generated Cmake Pico project file

cmake_minimum_required(VERSION 3.13)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Initialise pico_sdk from installed location
# (note this can come from environment, CMake cache etc)

# == DO NOT EDIT THE FOLLOWING LINES for the Raspberry Pi Pico VS Code Extension to work ==
if(WIN32)
    set(USERHOME $ENV{USERPROFILE})
else()
    set(USERHOME $ENV{HOME})
endif()
set(sdkVersion 2.2.0)
set(toolchainVersion 14_2_Rel1)
set(picotoolVersion 2.2.0-a4)
set(picoVscode ${USERHOME}/.pico-sdk/cmake/pico-vscode.cmake)
if (EXISTS ${picoVscode})
    include(${picoVscode})
endif()
# ====================================================================================
set(PICO_BOARD pico CACHE STRING "Board type")

# Pull in Raspberry Pi Pico SDK (must be before project)
include(pico_sdk_import.cmake)

project(OLED_Library C CXX ASM)

# Initialise the Raspberry Pi Pico SDK
pico_sdk_init()

# Add executable. Default name is the project name, version 0.1

add_executable(OLED_Library 
    OLED_Library.c 
)

pico_set_program_name(OLED_Library "OLED_Library")
pico_set_program_version(OLED_Library "0.1")

# Modify the below lines to enable/disable output over UART/USB
pico_enable_stdio_uart(OLED_Library 0)
pico_enable_stdio_usb(OLED_Library 1)

# Driver library
add_library(driver
    driver/SSD1306_driver.c
)

target_include_directories(driver PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}/driver
)

add_library(graphics_2d
    graphics/graphics_2d.c
)

target_include_directories(graphics_2d PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}/graphics
)

target_link_libraries(graphics_2d
    pico_stdlib
)

target_link_libraries(driver
    pico_stdlib
    hardware_i2c
)

target_link_libraries(OLED_Library
    driver
    graphics_2d
)

# Add the standard include files to the build
target_include_directories(OLED_Library PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}
)

pico_add_extra_outputs(OLED_Library)

