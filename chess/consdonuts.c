//memset(array, 0, sizeof(array[0][0]) * m * n);
//use to 0 out
#define NUMLOOPS 10
#define NUMDONUTS 2
#include donuts.h//for rings, sem, shared mem idint		shmid, semid[3];

int main(int argc, char *argv[])
{
	int	in_ptr [NUMSLOTS];
	//int	serial [NUMFLAVORS];
	int	i,j,k;
	int donut_box[NUMFLAVORS][12];
	struct donut_ring *shared_ring;
	struct timeval randtime;
	int shmid, semid[3];


	for(i = 0; i < NUMFLAVORS; i++){
		in_ptr [i] = 0;
		serial [i]  = 0;
	}








	if((shmid = shmget (MEMKEY, 0,0)) == -1){
		perror("shared get failed: ");
		exit(1);
	}



	if((shared_ring = (struct donut_ring *)
			   shmat (shmid, NULL, 0)) == -1){
		perror("shared attach failed: ");
		sig_handler(-1);
	}




	for(i=0; i<NUMSEMIDS; i++)
		if ((semid[i] = semget (SEMKEY+i, NUMFLAVORS,
					 IPC_CREAT | 0600)) == -1){
		perror("semaphore allocation failed: ");
		sig_handler(-1);
	}






	gettimeofday (&randtime, (struct timezone *)0);

/* use microsecond component for uniqueness */

	unsigned short xsub1[3];
        xsub1[0] = (ushort) randtime.tv_usec;
        xsub1[1] = (ushort)(randtime.tv_usec >> 16);
        xsub1[2] = (ushort)(getpid());

/* use nrand48 with xsub1 to get 32 bit random number */

        j=nrand48(xsub1) & 3;


/* use the semsetall utility to set initial semaphore values */

	if(semsetall (semid [PROD],
			   NUMFLAVORS, 	NUMSLOTS) == -1){
                perror("semsetsall failed: ");
                sig_handler(-1);
	}
	if(semsetall (semid [CONSUMER],
			   NUMFLAVORS, 	0) == -1){
                perror("semsetsall failed: ");
                sig_handler(-1);
        }
	if(semsetall (semid [OUTPTR],
			   NUMFLAVORS, 	1) == -1){
                perror("semsetsall failed: "0)
                sig_handler(-1);
        }
/*  the rest of the producer/consumer code follows,   */
/*  including the producer signal handler below       */
	for(i = 0; i < NUMLOOPS; i++)//time to make the donuts
	{
        for(j = 0; j < 12; j++)//dozen does not vary so magic number is acceptable
        {
        int randonut = nrand48(xsubl) & 3;
		p(semid[OUTPTR], randonut);//lock outptr
		p(semid[OUTPTR], j;//lock
		int donut = shared_ring->outptr[randonut]
		//unlock outptr
		//unlock producer
        }
	}
printf("all done can you see me?\n");

}//close main


