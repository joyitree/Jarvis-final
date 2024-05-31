import time
import multiprocessing
from engine.command import speak, greetUser
from user_authentication.face_recognition import user_authenticate

# To run Jarvis
def startJarvis():
    # Code for process 1 
    print("Process 1 is running.")
    from main import start
    start()

# To run hotword
def listenHotword():
    # Code for process 2
    print("Process 2 is running.")
    from engine.features import hotword
    hotword()

# Driver Code 
if __name__ == '__main__':
    speak("Initializing Jarvis", use_eel=False)
    print("Loading J.A.R.V.I.S ⌛")
    speak("Starting all system applications", use_eel=False)
    speak("All systems have beeen activated", use_eel=False)
    
    # time.sleep(2)
    
    print("System is online 🤖")
    speak("Ready for face biometrics", use_eel=False)
    
    speak("Performing user authentication", use_eel=False)
    print("Please look at the [◉°]")
    check, user = user_authenticate() # Face Recognition

    
    # Start both processes
    if check == True:
        print("👤「 ✔ ᵛᵉʳᶦᶠᶦᵉᵈ 」")
        speak("User authentication successful !!", use_eel=False)
        
        
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start()
        greetUser(user)
        p2.start()
        p1.join() # checking whether jarvis is closed (i.e X button is triggered)

        if p2.is_alive():
            p2.terminate()
            p2.join()
        speak("system stop", use_eel=False)
        print("system stop")
        
        
    else:
        speak("User authentication failed", use_eel=False)
        print("User authentication failed 👤❌")
