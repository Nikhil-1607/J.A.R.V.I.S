import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime
import openai
from config import apikey

speaker = win32com.client.Dispatch("SAPI.SpVoice")
chatStr = ""


def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"User: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    speaker.Speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for prompt{prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/{''.join(prompt.split('Jarvis')[1:]).strip()}.txt", "w") as f:
        f.write(text)
    # speaker.Speak(f"Sir the time is {text}")


# func to take input from mic
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from JARVIS."


def main():
    speaker.Speak("Hello, I am JARVIS. How can I help you")
    while True:
        print("Listening...")
        query = takeCommand()

        # used to open systems sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"]]  # todo: add more items in list
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]}...")
                webbrowser.open(site[1])

        # used to open applications
        applis = [["chrome", "chrome.exe"], ["Valorant", "valorant.exe"]]  # todo: add more items in list
        for appli in applis:
            if f"open {appli[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {appli[0]}...")
                os.system(f"start {appli[1]}")

        # used to open applications, problem is file should be in the folder of this project
        files = [["transcript", "transcript.pdf"]]  # todo: add more items in list
        for file in files:
            if f"open {file[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {file[0]}...")
                os.system(f"start {file[1]}")

        # time
        if "the time".lower() in query.lower():
            strftime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strftime)
            speaker.Speak(f"Sir the time is {strftime}")

        # chatgpt
        elif "chat G.P.T".lower() in query.lower():
            prompt = query
            ai(prompt)

        elif "Jarvis quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr=""

        else:
            print("Chatting...")
            chat(query)


if __name__ == "__main__":
    main()
