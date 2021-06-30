#include "store.hpp"
#include <iostream>
#include <vector>

void
store::string(int const x, int const y, string const a)
{
  InterestArray[x][y] = a;
};

void
store::Test()
{
  std::cout << "Test" << std::endl;
}
