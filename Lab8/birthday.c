#include <openssl/sha.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include<math.h>
#include <string.h>
#include <time.h>

/* We want a collision in the first 4 bytes = 2^16 attempts */
#define N_BITS  16
struct node{
    int key;
    char* val;
    struct node *next;
};
struct table{
    int size;
    struct node **list;
};
struct table *createTable(int size){
    struct table *t = (struct table*)malloc(sizeof(struct table));
    t->size = size;
    t->list = (struct node**)malloc(sizeof(struct node*)*size);
    int i;
    for(i=0;i<size;i++)
        t->list[i] = NULL;
    return t;
}
int hashCode(struct table *t,int key){
    if(key<0)
        return -(key%t->size);
    return key%t->size;
}
void insert(struct table *t,int key,char* val){
    int pos = hashCode(t,key);
    struct node *list = t->list[pos];
    struct node *newNode = (struct node*)malloc(sizeof(struct node));
    struct node *temp = list;
    while(temp){
        if(temp->key==key){
            temp->val = val;
            return;
        }
        temp = temp->next;
    }
    newNode->key = key;
    newNode->val = val;
    newNode->next = list;
    t->list[pos] = newNode;
}
int lookup(struct table *t,int key){
    int pos = hashCode(t,key);
    struct node *list = t->list[pos];
    struct node *temp = list;
    while(temp){
        if(temp->key==key){
            return temp->val;
        }
        temp = temp->next;
    }
    return -1;
}

int raw2int4(unsigned char * digest) {
    int i;
    int sum = 0;

    for (i = 0; i < 3; i++) {
        sum += sum * 256 + digest[i];
    }

    return sum;
}

void hexdump(unsigned char * string, int length) {
    int i;
    for (i = 0; i < length; i++) {
        printf("%02x", string[i]);
    }
}

int main(int argc, char * argv[]) {
    uint32_t attempt;     /* Iterate through 16 bits of the 32; use the rest to run different attacks */
    unsigned char md[20]; /* SHA-1 outputs 160-bit digests */

    /* Try to find a collision on the first 4 bytes (32 bits) */

    /* Step 1. Generate 2^16 different random messages */


    /* Step 2. Compute hashes */

    /* Step 3. Check if there exist two hashes that match in the first four bytes */

    /* Step 3a. If a match is found, print the messages and hashes */

    /* Step 3b. If no match is found, repeat the attack with a new set of random messages */
    // char buffer[15];
    // int i;
    srand(time(NULL));
    char *string_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.-#'?!";
    struct table *t = createTable(pow(2,16));

    for (int i = 0; i< pow(2,16); i++) {
        short key1;
        char * randomString = malloc(sizeof(char) * (64 +1));

        for (int j=0; j < 64; j++) {
            key1 = rand() % strlen(string_set);          
            randomString[j] = string_set[key1];
        }

        randomString[64] = '\0';

        SHA_CTX context;
        SHA1_Init(&context);
        SHA1_Update(&context,randomString,64);
        SHA1_Final(md, &context);
        
        int first_bytes = raw2int4(md);
        
        if (lookup(t,first_bytes) != -1)
            insert(t,first_bytes,randomString);
        else
        {
            printf("COLLISION\n");
            printf(randomString);
            printf("\n");
            printf("%d\n" , first_bytes);
            break;
        }
        
}
}
