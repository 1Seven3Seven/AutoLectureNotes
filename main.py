"""
https://blog.devgenius.io/chatgpt-how-to-use-it-with-python-5d729ac34c0d
https://github.com/openai/whisper
https://github.com/openai/openai-python
"""

import openai


def gpt_test():
    openai.api_key = "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"

    models = openai.Model.list()

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role":    "system",
                "content": "You are a student is a lecture taking notes"
            },
            {
                "role":    "user",
                "content": "What are you doing?"
            },
            {
                "role":    "assistant",
                "content": "I am a student taking notes in a lecture. The lecture is about the impact of social media on society. The professor is discussing how social media has changed the way we communicate, share information, and consume media."
            },
            {
                "role":    "user",
                "content": "Can you give me some notes, only two points."
            }
        ]
    )

    print(completion.choices[0].message.content)


def whisper_test():
    pass


def main():
    gpt_test()


if __name__ == "__main__":
    main()
