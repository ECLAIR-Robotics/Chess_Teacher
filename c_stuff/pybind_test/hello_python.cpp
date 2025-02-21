#include <string>
#include <iostream>
#include <pybind11/pybind11.h>

int hello(const std::string& str) {
    std::cout << "user string: " << str << std::endl;
    return 69;
}

PYBIND11_MODULE(py_hello, m) {
    m.def("hello", &hello, "A function that prints and returns");
}
