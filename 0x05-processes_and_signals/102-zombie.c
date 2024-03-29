#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
/**
 * infinite_while - generate infinite while loop.
 *
 * Return: 0
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
 * main - generate zombie process using fork function
 *
 * Return: 0.
 */
int main(void)
{
	pid_t child_pid;
	int i = 0;

	while (i < 5)
	{
		child_pid = fork();
		if (child_pid > 0)
			printf("Zombie process created, PID: %d \n", getpid());
		else
			exit(0);
		i++;
	}
	infinite_while();
	return (0);
}

