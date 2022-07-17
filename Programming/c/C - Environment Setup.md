# [C Tutorial](https://www.tutorialspoint.com/cprogramming/c_environment_setup.htm) - Environment Setup

> If you want to set up your environment for C programming language, you need the following two software tools available on your computer, (a) `Text Editor` and (b) The `C Compiler`.

# Text Editor
- This will be used to type your program. Examples of few a editors include `Windows Notepad`, OS Edit command, Brief, Epsilon, `EMACS`, and `vim` or `vi`.
- The name and version of text editors can vary on different operating systems. 
  - For example, `Notepad` will be used on Windows, and `vim` or `vi` can be used on windows as well as on Linux or UNIX.
- The files you create with your editor are called the source files and they contain the program source codes. 
- The source files for C programs are typically named with the extension "`.c`".
- Before starting your programming, make sure you have one text editor in place and you have enough experience to write a computer program, save it in a file, compile it and finally execute it.

# The C Compiler
- The source code written in source file is the human readable source for your program. 
- It needs to be "compiled", into machine language so that your CPU can actually execute the program as per the instructions given.
- The compiler compiles the source codes into final executable programs. 
- The most frequently used and free available compiler is the GNU C/C++ compiler, otherwise you can have compilers either from HP or Solaris if you have the respective operating systems.
- The following section explains how to install GNU C/C++ compiler on various OS. 
- We keep mentioning C/C++ together because GNU gcc compiler works for both C and C++ programming languages.

# Installation on UNIX/Linux
- If you are using Linux or UNIX, then check whether GCC is installed on your system by entering the following command from the command line −
```sh
gcc -v
```
- If you have GNU compiler installed on your machine, then it should print a message as follows −
```sh
# In RedHat OS
$ gcc -v
Using built-in specs.
Target: i386-redhat-linux
Configured with: ../configure --prefix=/usr .......
Thread model: posix
gcc version 4.1.2 20080704 (Red Hat 4.1.2-46)

# In MacOS 
$ gcc -v
Apple clang version 13.1.6 (clang-1316.0.21.2.5)
Target: x86_64-apple-darwin21.5.0
Thread model: posix
InstalledDir: /Library/Developer/CommandLineTools/usr/bin
```



