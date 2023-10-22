import transformers
import numpy as np

class ChatBot():
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name

    def text_input(self, user_input):
        self.text = user_input

    def respond(self):
        nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")

        ## wake up
        if self.wake_up(self.text):
            res = "Hello, I am Dave the AI. What can I do for you?"
        ## action time
        elif "time" in self.text:
            res = self.action_time()
        ## respond politely
        elif any(i in self.text for i in ["thank", "thanks"]):
            res = np.random.choice(["You're welcome!", "Anytime!", "No problem!", "Cool!", "I'm here if you need me!", "You're welcome!"])
        elif any(i in self.text for i in ["exit", "close"]):
            res = np.random.choice(["Tata", "Have a good day", "Bye", "Goodbye", "Hope to meet soon", "Peace out!"])
        ## conversation
        else:
            if self.text == "ERROR":
                res = "Sorry, come again?"
            else:
                chat = nlp(transformers.Conversation(self.text), pad_token_id=50256)
                res = str(chat)
                res = res[res.find("bot >> ") + 6:].strip()
        return res

    def wake_up(self, text):
        return True if self.name in text.lower() else False

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')

if __name__ == "__main__":
    ai = ChatBot(name="dev")
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side='left')

    
    ex = True
    while ex:
        user_input = input("You: ")

        user_input = "[PAD] " + user_input

        ai.text_input(user_input)
        response = ai.respond()
        print(f"Dev: {response}")
        if any(i in ai.text for i in ["exit", "close"]):
            ex = False
    print("----- Closing down Dev -----")
