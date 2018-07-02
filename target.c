#include <stdio.h>

void foo() {
	printf("Pouet\n");
}

int main() {
	bar();

	foo();

	foo();

	return 0;
}
