OBJS	= main.o parser.o
SOURCE	= main.cc parser.cc
HEADER	= parser.h
OUT	= output.out
CC	 = g++
FLAGS	 = -g -c -Wall
LFLAGS	 = 

all: $(OBJS)
	$(CC) -g $(OBJS) -o $(OUT) $(LFLAGS)

main.o: main.cc
	$(CC) $(FLAGS) main.cc -std=c++17

parser.o: parser.cc
	$(CC) $(FLAGS) parser.cc -std=c++17


clean:
	rm -f $(OBJS) $(OUT)