"""
https://blog.devgenius.io/chatgpt-how-to-use-it-with-python-5d729ac34c0d
https://github.com/openai/whisper
https://github.com/openai/openai-python
"""

import openai


def gpt_test():
    with open("api_key.txt") as f:
        openai.api_key = f.readline().strip()

    with open("TranscriptExample.txt") as f:
        transcript = f.read()

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role":    "system",
                "content": "Provide a brief summary of what a transcript contains"
            },
            {
                "role":    "user",
                "content": transcript
            },
        ]
    )

    print(completion.choices[0].message.content)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role":    "system",
                "content": "Convert a transcripts into brief dot points that outline the main points presented"
            },
            {
                "role":    "user",
                "content": transcript
            },
        ]
    )

    print(completion.choices[0].message.content)


def whisper_test():
    pass


def main():
    gpt_test()


if __name__ == "__main__":
    main()
