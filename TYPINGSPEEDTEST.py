import time
def calculation_typing_speed(text, timetaken):
    word = len(text.split())
    letters = len(text)
    wpm = (word / timetaken) * 60
    lpm = (letters / timetaken) * 60
    return wpm, lpm
def typing_speedtest():
    print("Welcome to the Typing Speed Test!")
    input("PRESS ENTER TO START...")
    text_type = "This is a sample text that you can use to test your typing speed. Try to type it as accurately and quickly as possible."
    print("\nText_type:")
    print(text_type)
    input("Press Enter when you are ready to start typing...")
    starttime = time.time()
    userinput = input("Start typing: ")
    endtime = time.time()
    timetaken = endtime - starttime
    wpm, lpm = calculation_typing_speed(text_type, timetaken)
    print("\nYou typed:")
    print(userinput)
    print("\nTyping Speed Results:")
    print(f"Words per Minute (WPM): {wpm:.2f}")
    print(f"Characters per Minute (LPM): {lpm:.2f}")
if __name__ == "__main__":
    typing_speedtest()
