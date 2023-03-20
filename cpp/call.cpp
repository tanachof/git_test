#include "call.hpp"
#include <iostream>

int x = 5;
int y;

int get_value(void){
    y = 2 * x;
    return y;
}

void print_fizzbuzz(int data){
     if (data % 15 == 0) {
        std::cout << "FizzBuss" << std::endl;
    }else if(data % 3 == 0) {
        std::cout << "Fizz" << std::endl;
    }else if(data % 5 == 0) {
        std::cout << "Buzz" << std::endl;
    }

    if (x % 15 == 0) {
        std::cout << "FizzBuss" << std::endl;
    }else if(x % 3 == 0) {
        std::cout << "Fizz" << std::endl;
    }else if(x % 5 == 0) {
        std::cout << "Buzz" << std::endl;
    }
}