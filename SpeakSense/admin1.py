from tkinter import *
from tkinter import messagebox, filedialog
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
import speech_recognition as sr
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

class AdminHome:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Home")
        self.master.geometry("1200x700")

        self.duration = StringVar()
        self.fpath = StringVar()
        self.lbl_text = StringVar(value="Waiting")

        large_font = ("Verdana", 20)

        Label(master, text="Duration", font=large_font).place(x=650, y=30)
        Entry(master, textvariable=self.duration, width=5, font=large_font).place(x=850, y=30)

        Button(master, text="RECORD VOICE", font=large_font,
               command=self.recordvoice).place(x=650, y=90)

        Label(master, text="Select Voice File", font=large_font).place(x=650, y=200)
        Entry(master, textvariable=self.fpath, width=30, font=("Verdana", 14)).place(x=650, y=270)

        Button(master, text="Browse", font=("Verdana", 14),
               command=self.browsefunc).place(x=1000, y=265)

        Button(master, text="VIEW EMOTION", font=large_font,
               command=self.viewemotion).place(x=650, y=350)

        Label(master, textvariable=self.lbl_text, font=large_font).place(x=100, y=200)

        Button(master, text="Exit", font=large_font,
               command=master.destroy).place(x=650, y=500)

    def recordvoice(self):
        try:
            tme = int(self.duration.get().strip())

            if tme <= 0:
                messagebox.showerror("Error", "Enter valid duration")
                return

            fs = 44100
            messagebox.showinfo("Recording", "Recording started")

            record_voice = sd.rec(int(tme * fs), samplerate=fs, channels=2)
            sd.wait()

            write("out.wav", fs, record_voice)

            data, samplerate = sf.read("out.wav")
            sf.write("new.wav", data, samplerate, subtype="PCM_16")

            self.fpath.set("new.wav")
            messagebox.showinfo("Done", "Voice recording finished")

        except Exception as e:
            messagebox.showerror("Recording Error", str(e))

    def browsefunc(self):
        filename = filedialog.askopenfilename(
            filetypes=[("WAV files", "*.wav")]
        )

        if filename:
            self.fpath.set(filename)

    def viewemotion(self):
        path = self.fpath.get().strip()

        if path == "":
            messagebox.showerror("Error", "Please select audio file")
            return

        try:
            r = sr.Recognizer()

            with sr.AudioFile(path) as source:
                audio_text = r.record(source)

            text = r.recognize_google(audio_text)
            print("Text:", text)

            lines_list = tokenize.sent_tokenize(text)

            sid = SentimentIntensityAnalyzer()

            neg = 0
            neu = 0
            pos = 0

            for sentence in lines_list:
                score = sid.polarity_scores(sentence)
                neg += score["neg"]
                neu += score["neu"]
                pos += score["pos"]

            if neg > neu and neg > pos:
                emotion = "Negative Emotion"
            elif pos > neg and pos > neu:
                emotion = "Positive Emotion"
            else:
                emotion = "Neutral Emotion"

            self.lbl_text.set(emotion)
            messagebox.showinfo("Emotion Result", emotion)

        except Exception as e:
            messagebox.showerror("Emotion Error", str(e))