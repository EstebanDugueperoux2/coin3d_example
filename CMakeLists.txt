cmake_minimum_required(VERSION 3.15)
project(coin3d_test CXX)

find_package(Qt5 COMPONENTS Widgets REQUIRED)
find_package(Quarter REQUIRED)
find_package(Coin REQUIRED)

add_executable(coin3d_test src/main.cpp)

target_include_directories(
        coin3d_test 
        PRIVATE 
        "/usr/include/Coin4/" 
        "/usr/include/qt5/QtCore/" 
        "/usr/include/qt5/QtGui/" 
        "/usr/include/qt5/" 
        "/usr/include/qt5/QtOpenGL/"
)

target_link_libraries(coin3d_test
    PUBLIC
    Coin
    Qt5Core
    Qt5Widgets
    Quarter
)

install(TARGETS coin3d_test)
