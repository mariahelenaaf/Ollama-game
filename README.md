# Ollama Prompt Game

This game is a Python-based interactive program designed to test and refine prompt engineering skills using the Ollama language model. The game challenges users to craft effective prompts for the language model, encouraging clarity, creativity, and precision in communication. Each exercise focuses on a specific skill, such as tone of voice, avoiding ambiguity, formatting outputs, or guiding step-by-step reasoning.

Users provide prompts to the language model, aiming to solve predefined exercises. After submitting a prompt, users receive immediate feedback on whether the exercise was successfully completed.

* The game was based on [this tutorial](https://github.com/ivanfioravanti/prompt-eng-ollama-interactive-tutorial) about prompt engineering.

## Getting Started

These instructions will cover usage information and for the docker container 

### Prerequisites

In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

## How to Run

### For Windows users
1. Navigate to the project folder.
2. Run the script (double click):
   ```bash
   bash run.bat

### For Linux/Mac Users
1. Open a Terminal
- On Linux: Look for "Terminal" in the applications menu.
- On macOS: Open the Terminal app (found in Applications > Utilities).

2. Navigate to the Script Directory
Use the `ls` command to check in which directory you currently are.
Use the `cd` command to go to the directory where the `.sh` file is located:
```bash
cd /path/to/sh script
```

3. Make the File Executable
Check if the script is executable:
```bash
ls -l script.sh
```
If it is not executable, make it executable:
```bash
chmod +x script.sh
```

4. Run the Script
Run the script using one of the following methods:
- **Method 1: Using `./`**
  ```bash
  ./script.sh
  ```
- **Method 2: Using `sh` or `bash`**
  ```bash
  sh script.sh
  ```
  or
  ```bash
  bash script.sh
  ```

  ---

## Running a `.sh` File by Double-Click

### On Linux

1. **Make the File Executable**
   Ensure the file is executable using:
   ```bash
   chmod +x script.sh
   ```

2. **Configure File Manager Behavior**

   - **GNOME (e.g., Ubuntu):**
     - Open **Files**.
     - Go to **Preferences** or **Settings**.
     - Under the **Behavior** tab, set **Executable Text Files** to **Run executable files when they are opened**.

   - **KDE (e.g., Kubuntu):**
     - Right-click the `.sh` file.
     - Go to **Properties > Permissions** and check **Is executable**.
     - Double-click the file and choose "Run."

   - **XFCE (e.g., Xubuntu):**
     - Open **Thunar** (File Manager).
     - Go to **Edit > Preferences > Behavior** and set **Executable Files** to **Run them.**

---

### On macOS

1. **Make the File Executable**
   Similar to Linux, ensure the script is executable:
   ```bash
   chmod +x script.sh
   ```

2. **Use Automator to Wrap the Script**
   - Open **Automator** and create a new **Application**.
   - Drag **Run Shell Script** into the workflow area.
   - Copy and paste your script's commands into the script area.
   - Save the application. You can now double-click the Automator app to run your script.

---

## Important Notes

- **Output Visibility:** Scripts executed via double-click may run in the background. For terminal-based output, run the script in a terminal instead.
- **Model used:** "qwen2.5:3b".

---