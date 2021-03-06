#!/usr/bin/env python3
"""
simple broadcast script
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

if rank == root:
	data = "pesce"
else:
	data = None
data = comm.bcast(data)
if rank != root:
	print(str(rank) + ": " + data)
