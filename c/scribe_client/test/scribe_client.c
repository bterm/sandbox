#include <stdio.h>
#include <stdlib.h>

#include "scribe/scribe_utils.h"

int main(int argc, char **argv) 
{
	if (argc != 5)
	{
		printf("Usage: %s host port category message", argv[0]);
		exit(1);
	}
	
	printf("Sending msg to scribe\n");
	
	int result = scribe_send_msg(argv[1], atoi(argv[2]), argv[3], argv[4]);
	printf("Result: [%d]\n", result);
	
	return 0;
}

