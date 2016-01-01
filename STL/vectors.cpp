#include <iostream>
#include <vector>

using namespace std;

int main()
{
  vector<string> strings;

  strings.push_back("one");
  strings.push_back("two");
  strings.push_back("three");
  strings[1] ="dog";

  cout << strings[3] << "\n";
  cout << strings.size() << "\n";

  for (int i=0; i<strings.size(); i++) {
    cout << strings[i] << "\n";
  }

  cout << "Java like for loop" << "\n";
  for (vector<string>::iterator it = strings.begin(); it != strings.end(); ++it) {
    cout << *it << "\n";
  }

  return 0;
}
