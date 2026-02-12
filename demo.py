import os
import json
import datetime
import time
import threading
import webbrowser
import random

def get_screen_coords():
  
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                coords = f.read().strip().split(",")
                return int(coords[0]), int(coords[1])
        except Exception as e:
            print(f"Error reading config: {e}")
            return setup_screen_coords()
    else:
        return setup_screen_coords()

def setup_screen_coords():
 
    speak("Set your caller button point for the first time")
    try:
        bu = int(input("Set your screen Width value: "))
        cu = int(input("Set your screen Height value: "))
        with open(CONFIG_FILE, "w") as f:
            f.write(f"{bu},{cu}")
        return bu, cu
    except ValueError:
        print("Invalid input. Using default coordinates (100, 100)")
        return 100, 100

# ===== LEARNING SYSTEM =====
            
            else:
                print("\nThinking...\n")
                ai_reply = get_ai_response(query)
                print(f"{assistant_name}: {ai_reply}")
                speak(ai_reply)
                save_conversation(query, ai_reply)
        
        except KeyboardInterrupt:
            print("\n\nShutting down...")
            speak("Shutting down. Goodbye!")
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            continue

if __name__ == "__main__":
    main()
