# C - Data Types

- Data  types  in c  refer  to  an  extensive  system  used  for declaring  variables  or  functions  of different types.  
- The  type  of a  variable  determines  how  much  space  it occupies in storage  and  how  the  bit pattern stored is interpreted.

> The types in C can be classified as follows:

|**Sr.No.**|**Types & Description**|
| - | - |
|1|<p>**Basic Types**</p><p>They are arithmetic types and are further classified into: (a) integer types and (b) floating- point types.</p>|
|2|<p>**Enumerated types**</p><p>They  are  again  arithmetic  types  and  they  are  used  to  define  variables  that  can  only assign certain discrete integer values throughout the program.</p>|
|3|<p>**The type void**</p><p>The type specifier void indicates that no value is available.</p>|
|4|<p>**Derived types**</p><p>They  include  (a)  Pointer  types,  (b) Array  types,  (c) Structure types,  (d) Union  types  and</p><p>(e) Function types.</p>|

- The  array  types  and  structure types  are  referred collectively  as  the  aggregate types.  The  type  of a function  specifies  the  type  of the  function's  return  value.  
- We will see  the basic  types  in the  following section, where as other types will be covered in the upcoming chapters.

# Integer Types

- The  following table  provides  the  details  of standard integer  types  with their storage sizes  and  value ranges −

|**Type**|**Storage size**|**Value range**|
| - | - | - |
|char|1 byte|-128 to 127 or 0 to 255|
|unsigned char|1 byte|0 to 255|
|signed char|1 byte|-128 to 127|
|int|2 or 4 bytes|-32,768 to 32,767 or -2,147,483,648 to 2,147,483,647|
|unsigned int|2 or 4 bytes|0 to 65,535 or 0 to 4,294,967,295|
|short|2 bytes|-32,768 to 32,767|
|unsigned short|2 bytes|0 to 65,535|
|long|<p>8 bytes or (4bytes</p><p>for 32 bit OS)</p>|-9223372036854775808 to 9223372036854775807|
|unsigned long|8 bytes|0 to 18446744073709551615|
> To get the exact size of a type or a variable on a particular platform, you can use the **sizeof** operator. 
> The expressions sizeof(type) yields the storage size of the object or type in bytes. Given below is an example  to  get  the  size  of various  type  on  a  machine  using  different  constant  defined  in limits.h header file −

[*   Live Demo](http://tpcg.io/FnrxP5)![](Aspose.Words.27693b06-f62b-41db-a645-00f35fc61956.001.png)

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <float.h>

int main(int argc, char** argv) {

    printf("CHAR_BIT    :   %d\n", CHAR_BIT);
    printf("CHAR_MAX    :   %d\n", CHAR_MAX);
    printf("CHAR_MIN    :   %d\n", CHAR_MIN);
    printf("INT_MAX     :   %d\n", INT_MAX);
    printf("INT_MIN     :   %d\n", INT_MIN);
    printf("LONG_MAX    :   %ld\n", (long) LONG_MAX);
    printf("LONG_MIN    :   %ld\n", (long) LONG_MIN);
    printf("SCHAR_MAX   :   %d\n", SCHAR_MAX);
    printf("SCHAR_MIN   :   %d\n", SCHAR_MIN);
    printf("SHRT_MAX    :   %d\n", SHRT_MAX);
    printf("SHRT_MIN    :   %d\n", SHRT_MIN);
    printf("UCHAR_MAX   :   %d\n", UCHAR_MAX);
    printf("UINT_MAX    :   %u\n", (unsigned int) UINT_MAX);
    printf("ULONG_MAX   :   %lu\n", (unsigned long) ULONG_MAX);
    printf("USHRT_MAX   :   %d\n", (unsigned short) USHRT_MAX);

    return 0;
}
```

> When you compile and execute the above program, it produces the following result on Linux:

```c
CHAR_BIT : 8
CHAR_MAX : 127
CHAR_MIN : -128
INT_MAX : 2147483647
INT_MIN : -2147483648
LONG_MAX : 9223372036854775807
LONG_MIN : -9223372036854775808
SCHAR_MAX : 127
SCHAR_MIN : -128
SHRT_MAX : 32767
SHRT_MIN : -32768
UCHAR_MAX : 255
UINT_MAX : 4294967295
ULONG_MAX : 18446744073709551615
USHRT_MAX : 65535
```

# Floating-Point Types
- The  following table provide  the  details  of standard floating-point  types  with storage sizes and  value ranges and their precision −

|**Type**|**Storage size**|**Value range**|**Precision**|
| - | - | - | - |
|float|4 byte|1.2E-38 to 3.4E+38|6 decimal places|
|double|8 byte|2.3E-308 to 1.7E+308|15 decimal places|
|long double|10 byte|3.4E-4932 to 1.1E+4932|19 decimal places|

- The header file float.h defines macros that allow you to use these values and other details about the binary  representation  of real  numbers  in your  programs.  
- The  following example  prints  the  storage space taken by a float type and its range values −

[*   Live Demo](http://tpcg.io/mynMA1)![](Aspose.Words.27693b06-f62b-41db-a645-00f35fc61956.003.png)

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <float.h>

int main(int argc, char** argv) {

    printf("Storage size for float : %d \n", sizeof(float));
    printf("FLT_MAX     :   %g\n", (float) FLT_MAX);
    printf("FLT_MIN     :   %g\n", (float) FLT_MIN);
    printf("-FLT_MAX    :   %g\n", (float) -FLT_MAX);
    printf("-FLT_MIN    :   %g\n", (float) -FLT_MIN);
    printf("DBL_MAX     :   %g\n", (double) DBL_MAX);
    printf("DBL_MIN     :   %g\n", (double) DBL_MIN);
    printf("-DBL_MAX     :  %g\n", (double) -DBL_MAX);
    printf("Precision value: %d\n", FLT_DIG );

    return 0;
}
```

> When you compile and execute the above program, it produces the following result on Linux:

```c
Storage size for float : 4
FLT_MAX : 3.40282e+38
FLT_MIN : 1.17549e-38
-FLT_MAX : -3.40282e+38
-FLT_MIN : -1.17549e-38
DBL_MAX : 1.79769e+308
DBL_MIN : 2.22507e-308
-DBL_MAX : -1.79769e+308
Precision value: 6
```

|**Sr.No.**|**Types & Description**|
| - | - |
|1|<p>**Function returns as void**</p><p>There are various functions in C which do not return any value or you can say they return void. A function  with no return  value  has  the  return  type  as  void. For example,  **void  exit (int status);**</p>|
|2|<p>**Function arguments as void**</p><p>There  are various  functions  in C which  do  not  accept any  parameter. A function  with no parameter can accept a void. For example, **int rand(void);**</p>|
|3|<p>**Pointers to void**</p><p>A pointer of type void \* represents the address of an object, but not its type. For example, a memory allocation function **void  \*malloc(  size\_t size  );** returns a pointer to void which can be casted to any data type.</p>|
