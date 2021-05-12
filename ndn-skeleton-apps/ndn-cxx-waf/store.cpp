#include <iostream>
#include <vector>
#include "store.hpp"

void store::string(int const x, int const y, string const a){
  InterestArray[x][y] = a;
};

void store::Test(){
  std::cout << "Test" << std::endl;
}
