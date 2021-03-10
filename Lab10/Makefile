all:
	gcc -I/usr/local/include -L/usr/local/lib -lcrypto dhe.c -o dhe -lcrypto
	gcc -I/usr/local/include -L/usr/local/lib -lcrypto dhe_server.c -o dhe_server -lcrypto

start_client:
	./dhe

start_server:
	./dhe_server

clean:
	rm dhe dhe_server


