CC=clang++
CFLAGS=-Wall -Werror -ggdb

main: src/main.cc
	$(CC) $(CFLAGS) src/main.cc -o build/main