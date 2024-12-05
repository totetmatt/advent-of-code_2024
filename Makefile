CC      = gcc
CFLAGS  = -g -Wall -Wextra
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
day_05: day_05.c
	$(CC) $(CFLAGS) -o day_05 day_05.c
clean veryclean:
	$(RM) main