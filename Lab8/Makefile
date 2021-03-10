LDFLAGS=-LLab8/lib -lcrypto
CFLAGS=-Wall -g -ILab8/include

.PHONY: all
all: birthday

birthday: birthday.o
	gcc -o $@ $< $(LDFLAGS)

.PHONY: clean
clean:
	rm -vf *.o birthday
