# VSCode-Template-Automation
Automate code template creation for C & C++ development in Visual Studio Code with this handy tool. Say goodbye to manual setup and save time on repetitive tasks. Start your coding projects with consistency and efficiency, and focus on what matters most - writing great code.

## About

This repository provides a solution to automate code template creation for C and C++ development in Visual Studio Code. It simplifies your development workflow by automatically including header files and establishing a fundamental code structure to enhance your productivity.

### Video Demo
https://youtu.be/sVhAmx4cvzo

### Features

- Gets triggered as soon as a new .c or .cpp file is created.
- Automatically includes frequently used header files and initializes 'int main()' with 'return 0;'
- Ensures a consistent code structure for every project.
- Enhances productivity by eliminating manual setup distractions.
- Easy setup and integration into your Visual Studio Code workflow.

## Getting Started

To use this automation tool, follow these steps:

1. **Install Necessary Python Libraries:** First, make sure you have the required Python library installed. You can install it using pip:
pip install watchdog


2. **Create Python Scripts:**
- Create `detect.py` and `automate.py` in your working repository. You can copy the provided scripts or create your own.

3. **Configure Visual Studio Code:**
- In your working repository, create a `.vscode` folder if it doesn't already exist.
- Inside the `.vscode` folder, create a `tasks.json` file. You can copy the provided JSON configuration or customize it to your needs.

4. **Run the Task:**
- In Visual Studio Code, press `Ctrl+Shift+P` to open the command palette.
- Type and select "Run Task."
- Choose the "Watch for New .cpp Files" task you defined in the `tasks.json` file.

Now, every time a new `.cpp` file is created in the specified directory, your Python automation script (`automate.py`) will be executed, automating the desired task.

Feel free to customize these instructions in your README file and provide any additional information or context as needed.


### What are VSCode Tasks?

**VSCode Tasks** are a built-in feature of Visual Studio Code that allows you to automate various development-related tasks, such as building, testing, and running code. You can define and configure tasks to streamline your workflow and execute common actions with ease.

### What is the Python Watchdog Library?

The **Python Watchdog Library** is a tool for monitoring file system events, such as file creation, modification, or deletion. It's used to detect and respond to changes in files and directories, making it valuable for automating actions based on real-time file system events, such as triggering scripts when a new file is created.

**Let's simplify C & C++ development together!** 🚀
