CC      = gcc
CFLAGS  = -g -O3 -Wall -Wextra
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
day_06: day_06.c
	$(CC) $(CFLAGS) -o day_06 day_06.c
day_07: day_07.c
	$(CC) $(CFLAGS) -o day_07 day_07.c
day_08: day_08.c
	$(CC) $(CFLAGS) -o day_08 day_08.c
day_09: day_09.c
	$(CC) $(CFLAGS) -o day_09 day_09.c
day_10: day_10.c
	$(CC) $(CFLAGS) -o day_10 day_10.c
day_11: day_11.c
	$(CC) $(CFLAGS) -o day_11 day_11.c
clean veryclean:
	$(RM) main