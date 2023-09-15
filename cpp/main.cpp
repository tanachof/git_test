#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <cassert> 

#include "main_process.hpp"
#include "share.hpp"

 int share_val = 255;
int main(int argc, char const *argv[]){

   
   
    assert(argc == 2);
    
    std::cout << argc << std::endl;

    int data;
    data = atoi(argv[1]);

    std::string s = "t";

    std::cout << "start" << std::endl;

    main_process(data);

    read_data();

    std::cout << "end" << std::endl;
    std::cout << share_val << std::endl;
    

   

    
    return 0;
}