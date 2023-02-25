#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - Infinite whilte
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Create five zombie processes
 * Return: Always 0
 */
int main(void)
{
	int i;
	pid_t cpid;

	for (i = 0; i < 5; i++)
	{
		cpid = fork();
		if (cpid > 0)
			printf("Zombie process created, PID: %i\n", cpid);
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
