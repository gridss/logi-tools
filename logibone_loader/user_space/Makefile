all: logi_loader

logi_loader: serial_fpga_loader.o
	$(CC) -o logi_loader serial_fpga_loader.o

serial_fpga_loader.o: serial_fpga_loader.c
	$(CC) -c $(CFLAGS) serial_fpga_loader.c

install: logi_loader
	install logi_loader /usr/bin
clean:
	rm -rf *o logi_loader
