> בס״ד

# Examples

### Content
- [Variables](#variables)
  - [Assign Values to Variables](#assign-values-to-variables)
  - [Declare and Assign Value together](#declare-and-assign-value-together)
  - [Print Variables](#print-variables)
  - [Print double Variables](#print-double-variables)

- [Problem Description](#problem-description)


---
# Variables

# Assign Values to Variables
- Once we declare a variable, we can assign a value to it. 
> Let's see how to do that.
```c
// declare the variable
int age;

// assign the data 25 to it
age = 25;
```

- Here, we have used the `=` operator to assign the value `25` to the `age` variable.

---

# Declare and Assign Value together
- We can also assign values to variables during their declaration. 
> Let's see how:
```c
int age = 25;
```

- Here, we have created a variable and assigned a value to it in a single statement.

---

# Print Variables
- We use the `printf()` function to print variables in C programming.
> For now, let's just see an example to print variables.
```c
#include <stdio.h>
 
int main() {
 
  // create a variable
  int age = 25;
 
  // print the variable
  printf("%d", age);
  
  return 0;
}
```

- The `printf()` function prints anything present inside the quotation marks. 
- However, instead of `%d`, we are getting `25` (value of the age variable).
- This is because, in C, we use format specifiers to print variables. 
- Here, `%d` is a format specifier which is replaced by the value of the age variable (`25`).

![image](https://user-images.githubusercontent.com/51442719/179797020-57d3d026-8cff-4e74-a976-8febf72b8ea0.png)

> 💡 Note: The `%d` format specifier can only be used to print int variables. <br> To print double variables, we use `%lf`, which we will see next.



---

# Print double Variables
- Now that we know how to print variables, let's use the same concept to print a `double` variable.
```c
#include <stdio.h>
 
int main() {
 
  // create double type variable
  double number= 36.43;
 
  // print the variable
  printf("%lf ", number);
  
  return 0;
}
 
// Output: 36.430000
```

- Here, we have used `%lf` to print number (a `double` variable).



---

# Problem Description

- Create a program to print the variable.
  - Create two variables `number1` with value `34` and `number2` with value `78.32`.
  - Print `number1` and `number2` with a space in between.
```c
#include <stdio.h>

int main() {
  
  int number1 = 34;
  double number2 = 78.32;

  printf("%d", number1);
  printf(" %lf", number2);

  return 0;
}
``` 

---





- [Learn C Programming](https://app.programiz.pro/course/learn-c-programming)


