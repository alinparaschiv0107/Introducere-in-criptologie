LDFLAGS=-lcrypto -ldl
CFLAGS=-Wall -g

.PHONY: all
all: aesgcm

aesgcm: aesgcm.o
	gcc -o $@ $< $(LDFLAGS)

.PHONY: clean
clean:
	rm -vf *.o aesgcm
