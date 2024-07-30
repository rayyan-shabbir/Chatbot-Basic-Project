import openai

class Chatbot:
    def __init__(self):
        # openai.api_key = "sk-None-lnp23pyKDnGNTBDltjGuT3BlbkFJC4yl3Jl5cCZFIo7eXP1t"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-devinci-003",
            prompt=user_input,
            max_token=4000,
            temperature=0.5
        ).choices[0].text



if __name__ == "__main__":
    chatbot = Chatbot()
    reponse = chatbot.get_response("Write a joke about birds.")
    print(response)
