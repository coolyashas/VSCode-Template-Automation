import os, sys

template_code = """#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>

int main()
{
    //Code here

    return 0;
}
"""

def automate_task(new_file):
    with open(new_file, 'w') as f:
        f.write(template_code)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 automate.py new_c_file.cpp")
        sys.exit(1)
    # Specify the path where the new .cpp file is created
    new_file = f"{sys.argv[1]}"
    automate_task(new_file)
