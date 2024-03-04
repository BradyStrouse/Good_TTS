# Change directory to the specified path
Set-Location -Path "C:\Coding_Projects\tts\coqui_tts"

# Activate the virtual environment
./Scripts/activate

# Set the model variable
$model = "tts_models/en/ljspeech/tacotron2-DDC"

# Run the tts-server.exe command with the model name parameter
$process = Start-Process -FilePath "tts-server.exe" -ArgumentList "--model_name $model" -NoNewWindow -PassThru

# Wait for the tts-server.exe process to initialize (adjust the duration as needed)
Start-Sleep -Seconds 10  # Adjust the duration based on your requirements

# Specify the URL of the website
$websiteUrl = "http://localhost:5002"

# Wait until the server is ready
while ((Test-NetConnection -ComputerName "localhost" -Port 5002 -InformationLevel Quiet) -eq $false) {
    Start-Sleep -Seconds 1
}

# Open the website in the default web browser
Start-Process $websiteUrl