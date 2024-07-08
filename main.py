from voicevox import text_to_voice
from whisper import voice_to_text
from gpt import chat

def main():
    text_to_voice("私はあなたのパーソナルアシスタントです。何かご用ですか？")

    messages = [
        {"role":"user","content":"あなたはパーソナルアシスタントです。"},
        {'role': 'assistant', 'content':"私はあなたのパーソナルアシスタントです。何かご用ですか？"}
    ]

    while True:
        text = voice_to_text()
        messages.append(
            {'role':'user', 'content':text}
        )

        print(text)
        res = chat(messages)
        print(res)

        messages.append(
            {'role':'assistant', 'content':res}
        )
        text_to_voice(res)

if __name__ == "__main__":
    main()