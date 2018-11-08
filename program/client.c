#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <time.h>


static void usage(const char* proc)
{
    printf("usage:%s [ip] [port]\n",proc);
}

int main(int argc,char* argv[])
{
   time_t time1;
   time1=time(NULL);

   if(argc!=3)
    {
        usage(argv[0]);
        return 3;
    }

    int sock=socket(AF_INET,SOCK_STREAM,0);
    if(sock<0)
    {
        perror("socket");
        exit(1);
    }

    struct sockaddr_in server;
    server.sin_family=AF_INET;
    server.sin_port=htons(atoi(argv[2]));
    server.sin_addr.s_addr = inet_addr(argv[1]);

    if(connect(sock,(struct sockaddr*)&server,(socklen_t)sizeof(server))<0)
    {
        perror("connect");
        exit(2);
    }

    char buf[1024];

    //while(1)
    int i=0;
    for(i=0;i<100000;i++)
    {
	//printf("send#");
        fflush(stdout);
        //ssize_t _s=read(0,buf,sizeof(buf)-1);
	//ssize_t _s=100;
        //buf[_s-1]=0;
	//printf("%s\n",buf);
	//printf("%d\n",_s);
	sprintf(buf, "%d" ,i);
        write(sock,buf,strlen(buf));
	usleep(50);


	/*
	int i=0;
	for(i=0;i<100;i++){
		fflush(stdout);
		sprintf(buf, "%d" ,i);
		buf[strlen(buf)]="0";
		write(sock,buf,strlen(buf));
	}
	*/

    }

    close(sock);

    time_t time2;
    time2=time(NULL);
    printf("Spent time : %ds\n",time2-time1);

    return 0;

}

