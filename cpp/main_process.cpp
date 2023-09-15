#include <map>
#include <string>
#include <functional>
#include <iostream>
#include <vector>

#include "call.hpp"
#include "main_process.hpp"
#include "share.hpp"



static int opt_val = 1;
static int pat_val = 1;



void main_process(int val){
    
    int data;

    data = val;

    print_fizzbuzz(data);
    printf("%d\n",share_val);
}


void print_option(std::string str){
    std::cout << str << std::endl;
    std::cout << "opt" << std::endl;
    std::cout << VAL << std::endl;
}   


void print_pattern(std::string str){
    std::cout << str << std::endl;
    std::cout << "pat" << std::endl;
    
}   


void read_data(void){

    std::vector<std::string> str_v{"option","pattern"};


    std::map<std::string,std::function<void(std::string)>> rfntbl{
        {"option",[](std::string str){print_option(str);}},
        {"pattern",[](std::string str){print_pattern(str);}},
    };

    for (auto data : str_v){
        if (data == "option") continue;
        rfntbl[data](data);
        
    }


}

int check_string(std::string str){
    if (str.empty()) return 1;
    
    std::cout << str << std::endl;
    std::cout << 5 << std::endl;

    return 0;


}
