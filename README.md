This has the assignment.cu which should be run using the run.sh file which automatically puts in different parameters for the threads and blocks to see differences in timing.  The assignment2.cu file is the cuda file that uses the two libraries and no libraries in an attempt to multiple random numbers.  It uses rand to create the variables, curand to create the random variables with the GPU, and finally rand combined with cublas for vector multiplication.  A sample run and the timings are in the output Module 8 Output.pdf file

-Jared Seifter# horse_or_dog
