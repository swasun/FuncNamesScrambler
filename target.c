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
