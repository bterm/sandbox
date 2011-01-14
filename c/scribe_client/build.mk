UNAME=$(shell uname)
CURRENT_DIR = $(shell pwd)

LIBRARY=libscribe_utils.so

CC = gcc
CXX = g++
CFLAGS=-fPIC -g -pipe -m64

THRIFT_INCLUDES=-I/usr/include/thrift -I/usr/include/thrift/fb303
COMMON_INCLUDES=
COMMON_LDFLAGS= -L/usr/lib64
SHARED_LDFLAGS=-shared

CPP_INCLUDES= $(THRIFT_INCLUDES) -I$(CURRENT_DIR)/gen-cpp
CPP_LDFLAGS=-lthrift -lfb303 -levent -lpthread -lboost_system

C_INCLUDES = 
C_LDFLAGS = 

INCLUDES := $(C_INCLUDES) $(COMMON_INCLUDES) $(CPP_INCLUDES) -I$(CURRENT_DIR)
LDFLAGS := $(MYSQL_FLAGS) $(COMMON_LDFLAGS) $(C_LDFLAGS) $(CPP_LDFLAGS) 

# Directories containing c++
CPP_DIRECTORIES = gen-cpp scribe
CPP_OBJFILES =  $(patsubst %.cpp, %.o, $(foreach SUBDIRECTORIES, $(CPP_DIRECTORIES), $(wildcard $(SUBDIRECTORIES)/*.cpp)))

# Directories containing c
#DIRECTORIES = $(shell find $(SOURCE_DIR) -type d \( ! -iname ".*" \))
DIRECTORIES = 
OBJFILES := $(patsubst %.c, %.o, $(foreach SUBDIRECTORIES, $(DIRECTORIES), $(wildcard $(SUBDIRECTORIES)/*.c)))

all: clean $(LIBRARY)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $< $(INCLUDES)

%.o: %.cpp
	$(CXX) $(CFLAGS) -c -o $@ $< $(INCLUDES)

$(LIBRARY): $(OBJFILES) $(CPP_OBJFILES)
	$(CC) $(SHARED_LDFLAGS) -o $(LIBRARY) $^ $(INCLUDES) $(LDFLAGS)

clean: force
	$(shell find . -name '*.o' -exec rm -f {} \;)
	rm -f $(LIBRARY) 

.PHONY: all force
