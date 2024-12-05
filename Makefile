CC      = gcc
CFLAGS  = -g  -O3 -Wall -Wextra
RM      = rm -f

default: all

all: day_01 day_02 day_03

day_01: day_01.c
	$(CC) $(CFLAGS) -o day_01 day_01.c
day_02: day_02.c
	$(CC) $(CFLAGS) -o day_02 day_02.c
day_03: day_03.c
	$(CC) $(CFLAGS) -o day_03 day_03.c
day_04: day_04.c
	$(CC) $(CFLAGS) -o day_04 day_04.c
clean veryclean:
	$(RM) main