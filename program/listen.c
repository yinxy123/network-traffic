#include <pcap.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
 
void getPacket(u_char * arg, const struct pcap_pkthdr * pkthdr, const u_char * packet)
{
  FILE *fpt;
  fpt=fopen("/home/yxy/Desktop/s.txt","a+");

  int i;
  for(i=0; i<pkthdr->len; ++i)
  {
    fprintf(fpt," %02x", packet[i]);
    if( (i + 1) % 16 == 0 )
    {
      fprintf(fpt,"\n");
    }
  }
  
  fprintf(fpt,"\n\n");
  fclose(fpt);
}
 
int main()
{
  char errBuf[PCAP_ERRBUF_SIZE], * devStr;
  
  /* get a device */
  devStr = pcap_lookupdev(errBuf);
  
  if(devStr)
  {
    printf("success: device: %s\n", devStr);
  }
  else
  {
    printf("error: %s\n", errBuf);
    exit(1);
  }
  
  /* open a device, wait until a packet arrives */
  pcap_t * device = pcap_open_live(devStr, 65535, 1, 0, errBuf);
  
  if(!device)
  {
    printf("error: pcap_open_live(): %s\n", errBuf);
    exit(1);
  }

  /* wait loop forever */
  int id = 0;
  pcap_loop(device, -1, getPacket, (u_char*)&id);
  
  pcap_close(device);
 
  return 0;
}

