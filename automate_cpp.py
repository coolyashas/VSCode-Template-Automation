import os, sys

template_code = """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    //Your code here
    
    return 0;
}
"""

def automate_task(new_file):
    with open(new_file, 'w') as f:
        f.write(template_code)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 automate.py new_cpp_file.cpp")
        sys.exit(1)
    # Specify the path where the new .cpp file is created
    new_file = f"{sys.argv[1]}"
    automate_task(new_file)
