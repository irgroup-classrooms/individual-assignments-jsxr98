# **Linuyjourney.com Documentation**

## **1. The Shell**

### **1.1 What is the Shell?**

- The shell is a program that interprets commands from the user and communicates them to the operating system. It’s commonly accessed through terminal programs like “Terminal” or “Console.”
- In this course, you'll focus on **Bash (Bourne Again Shell)**, the default shell in most Linux distributions. Other shells exist (e.g., `ksh`, `zsh`), but they won’t be covered here.

### **1.2 Understanding the Shell Prompt**

- **Typical Shell Prompt Format:**  
  `username@hostname:current_directory`
- **Example Prompt:**  
  ```bash
  pete@icebox:/home/pete $
  ```
  The `$` symbol indicates a standard user prompt in Bash, Bourne, or Korn shells. It’s automatically displayed and should not be typed when entering commands.

### **1.3 Basic Command: `echo`**

- **Usage**: The `echo` command displays text or variables to the screen.
- **Example**:
  ```bash
  $ echo Hello World
  ```
  This command prints "Hello World" to the display, demonstrating basic shell interaction.

---
**Exercise**  
Try other Linux commands and observe their outputs:
```bash
$ date
$ whoami
```
![Shell Prompt Example](https://github.com/user-attachments/assets/6c0ca40d-89c5-4e64-92ae-6b24a5a2f9bb)

**Quiz**  
*What should be outputted to the display when you type `echo Hello World`?*  
Answer: `Hello World`



## **2. `pwd` (Print Working Directory)**

### **2.1 Everything is a File**

- In Linux, all elements (files, directories) are treated as files, organized in a hierarchical structure starting from the **root directory** (`/`).

### **2.2 Directory Tree**

- Files and directories are arranged in a tree structure:
  ```plaintext
  /
  |-- bin
  |-- etc
  |   |-- file3
  |   `-- directory1
  |-- home
  |-- var
  ```

### **2.3 Paths**

- **Absolute Path**: Shows the location of files and directories, building from the root.  
  Example: `/home/pete/Movies` specifies the path to the "Movies" folder.

### **2.4 `pwd` Command**

- Use `pwd` (Print Working Directory) to check your current location in the directory structure.
  ```bash
  $ pwd
  ```
---
**Quiz**  
*How do I find the current directory you are in?*  
Answer: `pwd`


## **3. `cd` (Change Directory)**

### **3.1 Paths**

- **Absolute Path**: Starts from the root directory `/`, giving the full location (e.g., `/home/pete/Desktop`).
- **Relative Path**: Starts from your current directory, using shorter references.

### **3.2 Change Directory (`cd`)**

- Use `cd [path]` to move to a different directory.
  ```bash
  $ cd /home/pete/Pictures
  ```

### **3.3 Path Shortcuts**

- `.` = Current directory
- `..` = Parent directory (one level up)
- `~` = Home directory (e.g., `/home/pete`)
- `-` = Previous directory

---

**Exercise**  
Run `cd` without any flags; where does it take you?

![Change Directory Example](https://github.com/user-attachments/assets/f40107b7-f160-40fa-840b-4447bb8a4ab1)

**Quiz**  
*If you are in `/home/pete/Pictures` and want to go to `/home/pete`, what shortcut would you use?*  
Answer: `cd ..`


## **4. `ls` (List Directories)**

### **4.1 Purpose of `ls` Command**

- The `ls` command lists files and directories within the current directory.
  ```bash
  $ ls
  $ ls /path/to/directory
  ```

### **4.2 Using Flags for Enhanced Listing**

- **Hidden Files (`-a` flag)**: Shows hidden files.
  ```bash
  $ ls -a
  ```
- **Detailed List (`-l` flag)**: Provides extended file information.
  ```bash
  $ ls -l
  ```
- **Combining Flags (`-la` or `-al`)**: Displays hidden files with detailed information.
  ```bash
  $ ls -la
  ```
---
**Exercise**  
Run `ls` with different flags and observe the output.

```bash
ls -R  # Recursively list directory contents
ls -r  # Reverse order while sorting
ls -t  # Sort by modification time, newest first
```

![List Directories Example](https://github.com/user-attachments/assets/455c2d14-9bb4-4594-83a1-539625c96859)

**Quiz**  
*What command would you use to list directory contents with detailed information?*  
Answer: `ls -l`


## **5. `touch`**

### **5.1 Creating New Files**

- Use the `touch` command to create an empty file.
  ```bash
  $ touch filename
  ```

### **5.2 Updating Timestamps**

- `touch` also updates the modification timestamp without altering content.  
  Example:
  ```bash
  $ touch filename
  ```
---
**Exercise**  
1. Create a new file.
2. Note the timestamp.
3. Touch the file again and check the timestamp.

![Touch Command Example](https://github.com/user-attachments/assets/d68439d4-7e80-44c6-a3e7-a94b0d756161)

**Quiz**  
*How do you create a file called `myfile`?*  
Answer: `touch myfile`



## **6. `file`**

### **6.1 File Naming in Linux**

- Linux filenames don’t necessarily indicate file type, so a file called `banana.jpeg` may not actually be a JPEG image.

### **6.2 Using the `file` Command**

- The `file` command reveals the file’s actual contents and type.
  ```bash
  $ file filename
  ```
- **Example**:
  ```bash
  $ file banana.jpg
  ```


---
**Exercise**  
Run the `file` command on different files and directories to see their types.

![File Command Example](https://github.com/user-attachments/assets/15589a9b-f766-45f5-b3f4-a4070e8ac3d5)

**Quiz**  
*What command do you use to find the type of a file?*  
Answer: `file`
