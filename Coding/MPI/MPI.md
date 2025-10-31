
# MPI Introduction

It is a parallel programming methodology wherein the architecture for cores and memory are required to be distributed. MPI works on shared memory systems also. But it cannot take advantage of the shared memory processes when invoked.

The process is as follows. The program execution is such that all the processes will be running the same program but having different set of data. Information is passed between threads via messages to inform the status. So, it follows SPMD or single program multiple data approach. Data to be shared between threads are explicitly passed between threads via messages.

Sources:

1. High Performance Computing - Prof. Randall J LeVeque, University of Washington, Coursera Course.
2. Sharcnet YouTube channel tutorials

GNU Fortran will have an MPI. MPICH is recommended to be installed and used.

Like fortran, all the variables and subroutines are CASE INSENSITIVE, EVEN IN MPI routines.

## Variables and Terms

**Communicator**:

Only a group of processors communicate.
Processors communicate on a purpose/context.
A communicator is a variable/() used for communicating messages or data between processors on a context.

``MPI_COMM_WORLD`` is a default communicator to communicate to all the processes and processors.

``MPI_COMM_RANK(comm1, proc_num, ierr)`` returns the rank/number/position/label of the processor in the communicator group. The value is given to proc-num

``MPI_COMM_SIZE(comm1, num_proc, ierr)`` returns the number of processors/processes in the communicator group. The value is given to num_proc

``ierr`` is a logical variable to indicate any error. If ierr is zero, then no error. If it is non-zero, then an MPI error is present.

``MPI_INIT(ierr)`` is used for initializing an MPI process.

``MPI_FINALIZE(ierr)`` is used for ending an MPI process.

There are 125+ MPI functions. Some important and main functions other than the above mentioned ones are as follows. They are helpful to do a wide variety of programs.

1. ``MPI_INTEGER``: Used to specify the type of data being sent
2. ``MPI_SUM``: Used for doing sum reduction operation
3. ``MPI_SEND``: Used to send a message
4. ``MPI_RCV``: Used to receive a message
5. ``MPI_BCAST``: Used to broadcast a message to all processors
6. ``MPI_REDUCE``: Used to do a reduction process

## Sample Hello World Program in Fortran

```Fortran
! A sample hello world program in Fortran MPI

program hello_mpi

    use mpi
    implicit none
    integer ierr, pro_num, no_pro

    ! use mpi is used for invoking the MPI subroutines
    ! ierr is an error indicator in MPI processes.
    ! ierr is to be zero. If non-zero, then there is an error.
    ! pro_num is the processor number
    ! no_pro is the number of processors

    call MPI_INIT(ierr)
    ! mpi_init starts the MPI processes
    
    call MPI_COMM_SIZE(MPI_COMM_WORLD, no_pro, ierr)
    ! mpi_comm_size finds the number of processes under use
    
    call MPI_COMM_RANK(MPI_COMM_WORLD, pro_num, ierr)
    ! mpi_comm_rank finds the processor number
    ! MPI_COMM_WORLD is a default communicator used for 
    ! communicating info to all processors

    !print *, "ierr value is:", ierr
    !print *, "MPI_COMM_WORLD value is:", MPI_COMM_WORLD
    print *, "Hello world from processor number", pro_num, "of", no_pro, "Processors"

    call MPI_FINALIZE(ierr)
    ! mpi_finalize ends the MPI processes

end program hello_mpi
```

To compile and create the executable, use
```Bash
mpif90 filename.f90
```
If MPICH is used, use
```bash
mpif90.mpich filename.f90 or mpif90 filename.f90 or .*.f95
```

To execute the file, use
```bash
mpiexec -n 4 ./a.out 
!mpiexec helps to indicate the number of processors to be used.
```

Where -n stands for the number of processors to be used. 4 processors are used here.
If more processors are indicated than what is available, then it wont show an error. Each processor will do two or more processes to meet the number indicated and thus, it won't be parallel. This is recommended when for debugging.

## Creating Communicators

``MPI_COMM_WORLD`` is a communicator for all the processors.

If a subset of processors were to be used, then a new communicator has to be created and used.

## MPI_BCAST

```Fortran
call MPI_BCAST(start, count, datatype, root, comm, ierr)
```

This statement broadcasts variables from one processor thread to all the others.

**start** : the memory address or variable name or an array entry.

**count** : number of variables/data to be sent using the entry in start.

**datatype** : the data type of the value(s) in the start.

**root** : the processor number that sends this variable to all the threads or the process doing the broadcast.

**comm** : communicator under use.

**ierr** : the error variable.

eg: to broad cast a double precision variable, x, from processor 3, to all the processes, then

```Fortran
MPI_BCAST(x,1,MPI_DOUBLE_PRECISION,3,MPI_COMM_WORLD,ierr)
```

For passing array values, it is a bit tricky. A new memory continuous array has to be made and then this array has to be made use for broadcast, or using a loop, the values can be made use for broadcast.

eg: you want to pass the jth column of a matrix/array having nrows and ncols, then the command will be

```Fortran
MPI_BCAST(a(1,j),nrows,MPI_DOUBLE_PRECISION,0,MPI_COMM_WORLD,ierr)
```

where ``a(1,j)`` is the starting address of the jth column and nrows of elements are there continuously in the memory allocation.
This works for passing columns in Fortran because Fortran is column based in memory allocation. This works for passing rows in C.

For passing rows/columns of an array that are not memory contiguous in Fortran/C, a buffer variable is to be created and it has to be allocated with the elements of the row/column using a loop and broadcasted.

``MPI_VECTOR`` is a simple way to do this process.

## MPI_SEND MPI_RECV

**MPI_SEND** and **MPI_RECV** are used for sending and receiving particular parts of data to and from other processes.

``MPI_SEND`` is used for sending data from one process to another

``MPI_RECV`` is used for receiving the data from the ``MPI_SEND`` call.

While sending and receiving multiple data between processes , to ensure the correct data is sent and received (simply to check the match) all around, an identifier is needed. This identifier is called a tag. ``MPI_SEND`` will be read by the MPI_RECV command having the same tag.

Tag is usually an integer, but can be used as a meaningful info, like row/column number.

```Fortran
call MPI_SEND(start, count, datatype, dest, tag, comm, ierr)
```

**start** = Starting address or the variable name or the array element

**count** = No. of variables in continuous order to send

**datatype** = type of each element (int, float etc.,)

**dest** = destination process

**tag** = identifier tag (0 to 32767)

**comm** = communicator

**ierr** = error variable

```Fortran
call MPI_RECV(start, count, datatype, source, tag, comm, status, ierr)
```

**start** = Starting address or the variable name or the array element

**count** = No. of variables in continuous order to send

**datatype** = type of each element (int, float etc.,)

**source** = process from where data is coming

**tag** = identifier tag (0 to 32767)

**comm** = communicator

**status** = integer array of length MPI_STATUS_SIZE. Has a lot of uses.

status array/vector has an inbuilt size namely **MPI_STATUS_SIZE**.

status array has to be defined explicitly as:

```Fortran
    integer, dimension(MPI_STATUS_SIZE) :: status
```

``ierr`` = error variable

A source can match any source with the keyword **MPI_ANY_SOURCE**

A tag can match any tag with the keyword **MPI_ANY_TAG**

eg:
```Fortran
if (proc_num == 4) then
    i = 55
    call MPI_SEND(i, 1, MPI_INTEGER, 3, 21, MPI_COMM_WORLD, ierr)
end if
if (proc_num == 3) then
    call MPI_RECV(j, 1, MPI_INTEGER, 4, 21, MPI_COMM_WORLD, status, ierr)
    print *, "j = ",j  ! Process 3 Will print j = 55
end if
```

In this example, i is sent from process number 4 and received by process number 3 as j. The Tag is 21. The receive call will not accept messages from other sent calls.

This is a **blocking MPI_RECV**. This subroutine will not return or complete its job until it receives a call from MPI_SEND with the tag 21. So, the next statement will not run unless it is finished called. Similarly, it will wait till all the other processes are done that calls and sends a message to it. Can lead to code hangups if not done properly.

eg:

```Fortran
!This piece of code will pass value of i from process 0 to 1 to 2 to ... to num_proc - 1

if (proc_num == 0) then
    i = 55
    call MPI_SEND(i, 1, MPI_INTEGER, 3, 21, MPI_COMM_WORLD, ierr)

else if (proc_num < num_procs - 1) then
    call MPI_RECV(i, 1, MPI_INTEGER, proc_num-1, 21, MPI_COMM_WORLD, status, ierr)

     call MPI_SEND(i, 1, MPI_INTEGER, proc_num+1, 21, MPI_COMM_WORLD, ierr)

else if (proc_num == num_procs - 1) then
    call MPI_RECV(i, 1, MPI_INTEGER, proc_num-1, 21, MPI_COMM_WORLD, status, ierr)
    print *, "i = ",i  ! Process proc_num-1 Will print i = 55
end if
```

## Status and Tags in MPI_RECV

``Status`` is a parameter in ``MPI_RECV``.

Used for knowing from where the data was received from and what data is received. Especially when ``MPI_ANY_SOURCE`` or ``MPI_ANY_TAG`` are used.

Status is an array of integers. It has one element indexed with the keyword ``MPI_SOURCE``. Denoted as status (``MPI_SOURCE``). This will return a number from which the source of the message can be found.

Using this, we can find if ``MPI_ANY_SOURCE`` was used or not.

Similarly, ``status(MPI_TAG)`` will return the tag of the source message. Using this, we can find if MPI_ANY_TAG was used or not.

eg:

```Fortran
! Master processor 0 sends the jth column of an array to the jth 
! worker and gets the 1-norm to store in anorm(j) j = 1, 2, 3, ..., ncols

! code for master processor = 0
if (proc_num == 0) then
    do j = 1, n
          call MPI_SEND(a(1, j) , nrows, MPI_DOUBLE_PRECISION, j, j, MPI_COMM_WORLD, ierr)
    end do

    do j = 1, n
          call MPI_RECV(colnorm, 1, MPI_DOUBLE_PRECISION, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, status, ierr)

          jj = status(MPI_TAG)
          anorm(jj) = colnorm
    end do
end if
```

Explanation:
The master processor will make n send calls. Each call will pass the jth column fully. a(1,j) is the beginning address of the column j. nrows indicate the n consecutive values in the array. The source is j itself. J denotes both the processor under consideration and the iteration number. The tag is again j. So, for each column sent, the tag used is the column number itself.

In the second do loop, the master processor gets n receive calls. These calls will be in any order. They will receive the column norm from other processes in any order. The code for slave processors does the column norm calculation. So, instead of waiting to receive the message in a regular order, the keyword MPI_ANY_SOURCE ensures that any of the finished processors can send the data to be received by processor 0. To ensure the same, the keyword MPI_ANY_TAG does the same. It assists any finished processor to come accordingly. Note that for a particular SOURCE, the corresponding TAG alone will be received. No mix and match.

But, to know which TAG has popped up or been received, the MPI_TAG element in status has the memory of the TAG received. So, this will say the column norm of which column was calculated and returned. jj gets the tag received and using that, the array anorm is filled with the column norm pertaining to the column, tag and source j.

The code that does the column norm calculation is given below.

```Fortran
! code for the slave processors
if (proc_num /= 0) then

     call MPI_RECV(colvect, nrows, MPI_DOUBLE_PRECISION, 0, MPI_ANY_TAG, MPI_COMM_WORLD, status, ierr)

     j = status(MPI_TAG)
    colnorm = 0.d0
    do i = 1, nrows
          colnorm = colnorm + abs(colvect(i))
    end do

    call MPI_SEND(colnorm, 1, MPI_DOUBLE_PRECISION, 0, j, MPI_COMM_WORLD, ierr)

end if
```

The ``MPI_RECV`` call receives each call from the master processor n times. Each call is received by one slave processor. To ensure that the call can be received in any order, ``MPI_ANY_TAG`` are used.

```j = status(MPI_TAG)``` gets the tag and the column number under consideration from the sent message. The do loop calculates the column norm and the result colnorn is sent by each of the n processors once through the ``MPI_SEND`` call. When sent, the source is made as 0 and the tag is sent as j, to indicate that the values are going to process 0 and the value corresponds to the column j.

## MPI_ABORT

To terminate or abort a program abruptly or in case of any error condition, use the **MPI_ABORT** call.

```Fortran
    call MPI_ABORT(MPI_COMM_WORLD, 1)
```

1 is the error value
