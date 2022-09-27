import os
from pydub import AudioSegment

root_directory = "experiment"
source_directory = "source"
result_directory = "split"
five_minutes = 300 * 1000
eight_minutes = 480 * 1000


def split_audio(audio_file_name: str):
    f = os.path.join(root_directory, source_directory, audio_file_name)
    source_audio = AudioSegment.from_wav(f)
    first_five_minutes = source_audio[:five_minutes]
    first_five_minutes.export(
        os.path.join(
            root_directory, result_directory, f"{audio_file_name}_first_5_minutes.wav"
        )
    )
    last_three_minutes = source_audio[five_minutes:eight_minutes]
    last_three_minutes.export(
        os.path.join(
            root_directory, result_directory, f"{audio_file_name}_last_3_min.wav"
        )
    )


def main() -> None:
    for file_name in os.listdir(f"{root_directory}/{source_directory}"):
        f = os.path.join(root_directory, source_directory, file_name)
        split_audio(f)


if __name__ == "__main__":
    main()
