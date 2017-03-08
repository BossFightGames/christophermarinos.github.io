#include donuts.h//for rings, sem, shared mem idint		shmid, semid[3];
void		sig_handler (int);

int main(int argc, char *argv[])
{
	int	in_ptr [NUMFLAVORS];
	int	serial [NUMFLAVORS];
	struct donut_ring *shared_ring;
	struct timeval randtime;
	int shmid, semid[3];

	for(i = 0; i < NUMFLAVORS; i++){
		in_ptr [i] = 0;
		serial [i]  = 0;
	}




//use signals to avoid DOSing mercury

   void        sig_handler ( int );  /* declare signal handler function */
   sigset_t   mask_sigs;
   int  i, nsigs;
   int sigs [] = {SIGHUP, SIGINT, SIGQUIT, SIGBUS,
                        SIGTERM, SIGSEGV, SIGFPE};

   struct sigaction new_act;
   nsigs = sizeof (sigs) / sizeof (int)
   sigemptyset (&mask_sigs);
   for(i=0; i< nsigs; i++)
       sigaddset (&mask_sigs, sigs [i]);       .
   for(i = 0; i <  nsigs; i++){
      new_act.sa_handler 	= sig_handler;
      new_act.sa_mask 	= mask_sigs;
      new_act.sa_flags 	= 0;
      if(sigaction (sigs [i], &new_act, NULL) == -1){
         perror("can't set signals: ");
         exit(1);
      }
   }



/*** begin syscall shmget comment for shared memory
     #include <sys/types.h>
     #include <sys/ipc.h>
     #include <sys/shm.h>

     int shmget(key_t key, size_t size, int shmflg)

************* end syscall shmget comment ******/


	if((shmid = shmget (MEMKEY, sizeof(struct donut_ring),
			            IPC_CREAT | 0600)) == -1){//0600 so others cannot get access
		perror("shared get failed: ");
		exit(1);
	}

/***  begin syscall shmat comment for shared memory
     #include <sys/types.h>
     #include <sys/ipc.h>
     #include <sys/shm.h>

     void *shmat (int shmid, const void *attach_addr,
					   int shmflg);

************* end syscall shmat comment ******/

	if((shared_ring = (struct donut_ring *)
			   shmat (shmid, NULL, 0)) == -1){
		perror("shared attach failed: ");
		sig_handler(-1);
	}



/***  begin syscall semget comment for semaphores
     #include <sys/types.h>
     #include <sys/ipc.h>
     #include <sys/sem.h>

     int semget (key_t key, int nsems, int semflg);

************* end syscall semget comment ******/


	for(i=0; i<NUMSEMIDS; i++)
		if ((semid[i] = semget (SEMKEY+i, NUMFLAVORS,
					 IPC_CREAT | 0600)) == -1){
		perror("semaphore allocation failed: ");
		sig_handler(-1);
	}



/***  begin syscall gettimeofday comment for time seed
     #include <sys/time.h>

     int gettimeofday (struct timeval *tp, struct timezone *tzp);

     struct timeval {
		long    tv_sec;         	/* seconds
        	long    tv_usec;        	/* and microseconds
     }

********* end syscall gettimeofday comment ******/


	gettimeofday (&randtime, (struct timezone *)0);

/* use microsecond component for uniqueness */

	unsigned short xsub1[3];
        xsub1[0] = (ushort) randtime.tv_usec;
        xsub1[1] = (ushort)(randtime.tv_usec >> 16);
        xsub1[2] = (ushort)(getpid());

/* use nrand48 with xsub1 to get 32 bit random number */

      /*  j=nrand48(xsub1) & 3;*/


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
int don_ind = 0;
	while(1)//time to make the donuts
	{
        int randon = nrand48(xsubl)&3;
		p(semid[don_ind], don_ind);//lock if we are at 0, ie if we have placed ten donuts and cons has taken 0

		shared_ring->flavor[don_ind][inptr[don_ind]] = randon;
		in_ptr[don_ind] = (in_ptr[don_ind] + 1) % NUMSLOTS;
		v(semid[CONSUMER], don_ind;
	}


}//close main

void    sig_handler(int sig)
{
	int	i,j,k;

	printf("In signal handler with signal # %d\n",sig);

	if(shmctl(shmid, IPC_RMID, 0) == -1){
		perror("handler failed shm RMID: ");
	}
	for(i = 0; i < NUMSEMIDS; i++){
	  if(semctl (semid[i], 0,
 			    IPC_RMID, (union semun)0) == -1){
		perror("handler failed sem RMID: ");
	  }
	}
        exit(5);
}


