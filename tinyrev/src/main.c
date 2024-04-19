#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>

void secure_cipher(const char *array1, const char *array2, char *result, int length) {
    for (int i = 0; i < length; i++) {
        result[i] = array1[i] ^ array2[i];
    }
}


int main() {
    char input[100];
    unsigned char hash[16];
    // i_hope_you_didn't_try_cracking_this
    unsigned char expected_hash[] = "\xd8\xbd\x3a\x2e\x8e\x74\xb4\xe8\x85\xc8\xe6\xe8\x9a\xaa\xf1\x11"; 

    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);

    MD5((unsigned char*)input, strlen(input), hash);
    int isGood = 1;

    for (int i = 0; i < 16; i++) {
        if (hash[i] != expected_hash[i])
            isGood = 0; 
    }
    if (isGood) {
        printf("Correct! Here's your flag:\n");
        // STEM24{53cur3_c1ph3r_15_ju57_x0r_87w_e9d95a57}
        unsigned char one[] = "\xbe\x3f\xd4\x33\xaf\x51\x01\x61\xa0\xdb\x1d\x8e\xb3\x3b\xa9\x8c\xfc\xd4\x1c\x04\x54\x72\x13\x72\xad\x75\x28\x1d\x70\x76\x55\xc6\xb4\xac\xc4\x53\xe8\x86\xbd\xe8\xc4\x33\x16\xda\xa1\xc5";
        unsigned char two[] = "\xed\x6b\x91\x7e\x9d\x65\x7a\x54\x93\xb8\x68\xfc\x80\x64\xca\xbd\x8c\xbc\x2f\x76\x0b\x43\x26\x2d\xc7\x00\x1d\x2a\x2f\x0e\x65\xb4\xeb\x94\xf3\x24\xb7\xe3\x84\x8c\xfd\x06\x77\xef\x96\xb8";
        unsigned char 
        printf("STEM24{53cur3_c1ph3r_15_ju57_x0r_87w_e9d95a57}");
        
    } else {
        printf("Wrong!\n");
    }

    return 0;
}
