0x05. Processes and signals


PID (Process ID):
PID stands for Process ID. It is a unique numerical identifier assigned to each running process on a computer system. 
The PID is used by the operating system to manage and control processes.

Process:
In computing, a process is an instance of a program that is being executed by a computer.
It has its own memory space, system resources, and is managed independently by the operating system. 
Processes are fundamental to multitasking operating systems, allowing multiple tasks to run concurrently.

Finding a Process’ PID:
You can find a process's PID using various commands. On Unix-like systems, the ps command is commonly used. For example:

ps aux | grep "process_name"


Killing a Process:
To terminate or kill a process, you can use the kill command followed by the PID. For example:

kill PID


Alternatively, you can use the pkill command to kill a process by its name:

pkill "process_name"


Signal:
In the context of processes, a signal is a software interrupt delivered to a process to notify it to
 perform a specific action. Signals are used for interprocess communication and process control.

Two Signals that Cannot be Ignored:

SIGKILL (9): This signal immediately terminates a process. It cannot be caught or ignored by the process,
 making it a forceful way to stop a running program.

SIGSTOP (19 or 17): This signal suspends the execution of a process. Like SIGKILL, it cannot be caught or
 ignored. The process remains in a stopped state until it receives a SIGCONT signal.
