CURRENT_DIR = $(shell pwd)

all: clean gen build

gen:
	make -f $(CURRENT_DIR)/gen.mk

build:
	make -f $(CURRENT_DIR)/build.mk
	make -C $(CURRENT_DIR)/test
	
clean:
	make -f $(CURRENT_DIR)/gen.mk clean
	make -f $(CURRENT_DIR)/build.mk clean
	make -C $(CURRENT_DIR)/test clean
	
.PHONY: all clean force
