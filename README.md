## Example

We have the file `target.c` with the following content:

```c
#include <stdio.h>

void foo() {
	printf("foo()\n");
}

void bar() {
    printf("bar()\n");
}

int main() {
	bar();

	foo();

	foo();

	return 0;
}
```

Run this simple test:

```bash
python3 test.py --file target.c --password password
```

Example of output:

```c
#include <stdio.h>

void fb9a40b7b7cc8877f4fbeec894f3b99a() {
	printf("fb9a40b7b7cc8877f4fbeec894f3b99a()\n");
}

void 30bea02020d22fade1eb20442399c9bb() {
	printf("30bea02020d22fade1eb20442399c9bb()\n");
}

int main() {
	30bea02020d22fade1eb20442399c9bb();

	fb9a40b7b7cc8877f4fbeec894f3b99a();

	fb9a40b7b7cc8877f4fbeec894f3b99a();

	return 0;
}
```

The content scrambled function names will change at each run.

## Dependency

pycparser is a parser for the C langage.

```bash
sudo apt-get install python3-pip && pip3 install pycparser --user
```
