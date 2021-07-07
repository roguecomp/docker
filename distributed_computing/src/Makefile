all:
	g++ -O3 main.cpp -o main
	mpiexec --allow-run-as-root -machinefile /home/src/machinefile -np 12 /home/src/main

clean:
	rm main
