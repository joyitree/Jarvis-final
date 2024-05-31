import multiprocessing

# 1st to run jarvis
def startJarvis():
    # Code for process 1 
    print("Process 1 is running.")
    from main import start
    start()

# 2nd To run hotword
def listenHotword():
    # Code for process 2
    print("Process 2 is running.")
    from engine.features import hotword
    hotword()
    
# Driver Code 
if __name__ == '__main__':
        # Start both processes
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start()
        p2.start()
        p1.join() # checking whether jarvis is closed (i.e X button is triggered)

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("System stop")
        