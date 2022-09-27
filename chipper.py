import os

from pydub import AudioSegment

directory = os.getcwd()
results = "split"
five_minutes = 300 * 1000
eight_minutes = 480 * 1000


def split_audio(audio_file_name: str) -> None:
    f = os.path.join(directory, audio_file_name)
    r = audio_file_name[:-4]
    source_audio = AudioSegment.from_wav(f)
    first_five_minutes = source_audio[:five_minutes]
    first_five_minutes.export(os.path.join(directory, results, f"{r}_first_5_min.wav"))
    last_three_minutes = source_audio[five_minutes:eight_minutes]
    last_three_minutes.export(os.path.join(directory, results, f"{r}_last_3_min.wav"))


def main() -> None:
    os.mkdir(os.path.join(directory, results))
    for file_name in os.listdir(directory):
        split_audio(file_name)


if __name__ == "__main__":
    main()
