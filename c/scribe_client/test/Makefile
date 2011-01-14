CURRENT_DIR = $(shell pwd)
COMPILE_DIR = $(CURRENT_DIR)/../

CFLAGS = -fPIC -g -pipe -m64
LDFLAGS = -L$(COMPILE_DIR) -lscribe_utils
INCLUDES = -I$(COMPILE_DIR)

CC = gcc

all: scribe 

scribe:
	$(CC) scribe_client.c $(CFLAGS)  $(LDFLAGS) $(INCLUDES) -o scribe_client

run:	
	LD_LIBRARY_PATH=$(COMPILE_DIR) ./scribe_client localhost 1463 test test

clean: 
	rm -f *.o scribe_client


