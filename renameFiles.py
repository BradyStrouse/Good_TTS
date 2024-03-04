import os
"""
This file is used to rename the output files from the TTS model from output_batch_0.txt to output_batch_000.wav, 
this is used the combine_wav_files function in main.py to combine the files into a single output.wav file.
"""
def rename_files(script_directory):
    # Specify the base filename
    base_filename = "output_batch_"

    # Iterate over files in the directory
    for filename in os.listdir(script_directory):
        if filename.startswith("output_batch_") and filename.endswith(".txt"):
            # Extract the number from the original filename
            original_number = int(filename.split("_")[-1].split(".")[0])

            # Create the new filename with 3 digits
            new_filename = f"{base_filename}{original_number:03d}.wav"

            # Build the full paths
            original_path = os.path.join(script_directory, filename)
            new_path = os.path.join(script_directory, new_filename)

            # Rename the file
            os.rename(original_path, new_path)

if __name__ == "__main__":
    # Get the directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Call the function to rename files
    rename_files(script_directory)