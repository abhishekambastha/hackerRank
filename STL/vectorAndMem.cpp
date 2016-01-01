#include <iostream>
#include <vector>
using namespace std;

int main()
{
  vector<double> numbers(20);
  cout << numbers.size() << "\n";

  int capacity = numbers.capacity();
  cout << "Capacity" << capacity << "\n";

  for (int i=0; i< 1000;i++) {
    if(numbers.capacity() != capacity){
      capacity = numbers.capacity();
      cout << "Capacity: " << capacity << "\n";
    }
    numbers.push_back(i);
  }

  return 0;
}
