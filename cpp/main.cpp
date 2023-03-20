#include <stdio.h>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <vector> 
#include <algorithm>

#include "call.hpp"



int main(int argc, char const *argv[]){

    int data;

    data = atoi(argv[1]);

    print_fizzbuzz(data);

    
    return 0;
}