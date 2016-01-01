#include <iostream>
#include <map>
using namespace std;

int main()
{
  map<string, int> ages;

  ages["Mike"] = 40;
  ages["Vickey"] = 20;
  ages["Reena"] = 21;

  cout << ages["Reena"] << "\n";

  if (ages.find("Raj") != ages.end()) {
    cout << "Raj found" << "\n";
  }else{
    cout << "raj not found" << "\n";
  }

  for (map<string, int>::iterator it = ages.begin(); it != ages.end(); ++it) {
    cout << it->first << ": " << it->second << endl;
  }
  return 0;
}
