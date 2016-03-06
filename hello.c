/* Hello World program */
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
int length = 457;
int identification = 457;
int checksum = 200;
int sourceAddress = 34916;
int destinationAddress = 40567;

void IP(unsigned char * packet){
	
	
	
unsigned char * ipMod = malloc(sizeof(unsigned char)*5*4+ sizeof(unsigned char)*64);	
unsigned char * NewStr = malloc(sizeof(unsigned char)*5*4+ sizeof(unsigned char)*64);	



unsigned char  VersionAndheaderLength = 0x45;
unsigned char  typeOfService = 0x00;
unsigned char  totalLengthMSB = (unsigned char)((length >> 8)&0xff);//most sig byte
unsigned char  totalLengthLSB = (unsigned char)((length >> 0)&0xff);//least sig byte
unsigned char  identificationLSB =(unsigned char)((identification >> 0)&0xff);//least sig byte
unsigned char  identificationMSB;(unsigned char)((identification >> 8)&0xff);//most sig byte
unsigned char  flagsEvilAndMSHalfFragOffset = 0x00;
unsigned char  LSHalfFragOffset = 0x00;
unsigned char  timeToLive = 0x40;
unsigned char  protocol = 0x11;
unsigned char  headerChecksumMSB = (unsigned char)((checksum >> 8)&0xff);//most sig byte
unsigned char  headerChecksumLSB = (unsigned char)((checksum >> 0)&0xff);//least sig byte
unsigned char  sourceAddress0=(unsigned char)((sourceAddress >> 24)&0xff);
unsigned char  sourceAddress1=(unsigned char)((sourceAddress >> 16)&0xff);
unsigned char  sourceAddress2=(unsigned char)((sourceAddress >> 8)&0xff);
unsigned char  sourceAddress3=(unsigned char)((sourceAddress >> 0)&0xff);
unsigned char  destinationAddress0=(unsigned char)((destinationAddress >> 24)&0xff);
unsigned char  destinationAddress1=(unsigned char)((destinationAddress >> 16)&0xff);
unsigned char  destinationAddress2=(unsigned char)((destinationAddress >> 8)&0xff);
unsigned char  destinationAddress3=(unsigned char)((destinationAddress >> 0)&0xff);
ipMod[0] = VersionAndheaderLength;
ipMod[1] = typeOfService;
ipMod[2] = totalLengthMSB;
ipMod[3] = totalLengthLSB;
ipMod[4] = identificationMSB;
ipMod[5] = identificationLSB;
ipMod[6] = flagsEvilAndMSHalfFragOffset;
ipMod[7] = LSHalfFragOffset;
ipMod[8] = timeToLive;
ipMod[9] = protocol;
ipMod[10] = headerChecksumMSB;
ipMod[11] = headerChecksumLSB;
ipMod[12] = sourceAddress0;
ipMod[13] = sourceAddress1;
ipMod[14] = sourceAddress2;
ipMod[15] = sourceAddress3;
ipMod[16] = destinationAddress0;
ipMod[17] = destinationAddress1;
ipMod[18] = destinationAddress2;
ipMod[19] = destinationAddress3;

//packet = NewStr;
int i = 0;
int j = 0;
  printf("begin new str \n");
   printf("this is it size of ip mod %d\n",(int)strlen(ipMod));
  
  	for (i = 0; i<20; i++){
		
		packet[i] = ipMod[i];
    
 }
 	//~ for (i = 0; i<80; i++){
		//~ 
		//~ printf ("%i 0x%2X\n",i,packet[i]);
		//~ 
    //~ 
 //~ }
 
 printf("end \n");
//&packet=&ipMod;
}

int main(void)
{
    printf("Hello World\n");
	unsigned char TXT[] = { 0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
                          0x01,0x60,0x6E,0x11,0x02,0x0F,
                          0x08,0x00,0x11,0x22,0x33,0x44,
                          0x55,0x66,0x77,0x88,0x99,0xAA,
                          0x55,0x66,0x77,0x88,0x99,0xAA,
                          0x55,0x66,0x77,0x88,0x99,0xAA,
                          0x55,0x66,0x77,0x88,0x99,0xAA,
                          0x55,0x66,0x77,0x88,0x99,0xAA,
                          0x55,0x66,0x77,0x88,0x99,0xAA,
                          0x55,0x66,0x77,0x88,0x99,0xAA};
	//~ int i = 0;
	//~ printf("begin \n");
	//~ for (i = 0; i<64; i++){
     //~ printf ("0x%2X\n",TXT[i]);
 //~ }
 //~ printf("end \n");
    //~ 
  //~ 
  //~ IP(TXT);
   unsigned char * htp = malloc(sizeof(unsigned char)*80);
  int i = 0;
  int j = 0;
  printf("begin \n");
  	for (i = 20; i<80; i++){
		j = i - 20;
		htp[i] = TXT[j];
    // printf ("0x%2X\n",TXT[i]);
     
    
 }
IP(htp);
  printf("begin i be a printing \n");
  	for (i = 0; i<80; i++){
     printf ("% i 0x%2X\n",i,htp[i]);
     
    
 }
 printf("end \n");
 //IP(TXT);
 //printf("this is it %d\n",(int)sizeof(TXT));
 }



