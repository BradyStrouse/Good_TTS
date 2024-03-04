import torch
from TTS.api import TTS


from pydub import AudioSegment
import os

def text_to_speech():
    # Get device, if they are able to use cuda (GPU), use it, otherwise use cpu
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(device)

    # Open the file in read mode ('r')
    with open('paste_text_here.txt', 'r', encoding="utf-8") as file:
        # Read all lines into a list
        all_lines = file.readlines()

    # Init TTS with the target model name
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DCA", progress_bar=True).to(device)

    # Number of lines to process in each batch
    batch_size = 10

    # Split lines into batches
    for i in range(0, len(all_lines), batch_size):
        # Extract a batch of lines
        batch_lines = all_lines[i:i+batch_size]
        
        # Concatenate the batch of lines into a single string
        file_contents = ''.join(batch_lines)

        try:
            # Run TTS for each batch and save to a different output file
            output_file_path = f"output_batch_{i//batch_size}.wav"
            tts.tts_to_file(text=file_contents, file_path=output_file_path)

            print(f"Generated {output_file_path}")
        except RuntimeError as e:
            print(f"Error processing batch {i//batch_size}: {e}")

    combine_wav_files()

def combine_wav_files(output_filename='output.wav', input_prefix='output_batch_'):
    # Get a list of all WAV files in the current directory with the specified prefix
    wav_files = [file for file in os.listdir() if file.startswith(input_prefix) and file.endswith('.wav')]

    if not wav_files:
        print(f"No '{input_prefix}' WAV files found in the current directory.")
        return

    # Combine the WAV files
    combined_audio = AudioSegment.from_wav(wav_files[0])
    for wav_file in wav_files[1:]:
        combined_audio += AudioSegment.from_wav(wav_file)

    # Export the combined audio to a new WAV file
    combined_audio.export(output_filename, format="wav")

     # Delete the old WAV files
    for wav_file in wav_files:
        os.remove(wav_file)
        print(f"Deleted '{wav_file}'.")

    print(f"Combined {len(wav_files)} '{input_prefix}' WAV files into '{output_filename}'.")



if __name__ == "__main__":
    text_to_speech()