#include <openssl/md5.h>
#include <stdio.h>
#include <string.h>
// -O3 optimizes away the string stuff, don't do it pls

// one is /dev/urandom output, two is one xored with the flag
// also do a bit of trolling ghidra users
const char iVar1[] =
    "\xbe\x3f\xd4\x33\xaf\x51\x01\x61\xa0\xdb\x1d\x8e\xb3\x3b\xa9\x8c\xfc\xd4"
    "\x1c\x04\x54\x72\x13\x72\xad\x75\x28\x1d\x70\x76\x55\xc6\xb4\xac\xc4\x53"
    "\xe8\x86\xbd\xe8\xc4\x33\x16\xda\xa1\xc5";
const char lVar1[] =
    "\xed\x6b\x91\x7e\x9d\x65\x7a\x54\x93\xb8\x68\xfc\x80\x64\xca\xbd\x8c\xbc"
    "\x2f\x76\x0b\x43\x26\x2d\xc7\x00\x1d\x2a\x2f\x0e\x65\xb4\xeb\x94\xf3\x24"
    "\xb7\xe3\x84\x8c\xfd\x06\x77\xef\x96\xb8";

// i_hope_you_didn't_try_cracking_this
const unsigned char h[] =
    "\xd8\xbd\x3a\x2e\x8e\x74\xb4\xe8\x85\xc8\xe6\xe8\x9a\xaa\xf1\x11";

void secure_cipher(char *res) {
  for (int i = 0; i < 46; i++) {
    res[i] = (iVar1[i] | lVar1[i]) - (iVar1[i] & lVar1[i]);
  }
}

int main() {
  char input[100];
  unsigned char hash[16];

  printf("What's the password?\n");
  fgets(input, sizeof(input), stdin);
  
  // so what if it's deprecated. you think i care?
  MD5((unsigned char *)input, strlen(input), hash);
  // zero if good, something else if not good
  int isGood = 0;

  for (int i = 0; i < 16; i++) {
    // a teeny tiny obfuscation
    isGood |= hash[i] - h[i];
  }
  if (!isGood) {
    printf("Correct! Here's your flag:\n");
    // STEM24{53cur3_c1ph3r_15_ju57_x0r_87w_e9d95a57}
    char three[46];
    secure_cipher(three);
    printf("%s\n", three);

  } else {
    printf("Wrong!\n");
  }

  return 0;
}
