# 🎙️ Audio Transcription with Python and AI (Whisper)

## 📌 About the Project

This repository contains a simple and effective solution for **automatic audio transcription using OpenAI’s Whisper model**, implemented in a Google Colab Jupyter Notebook.

Designed to be beginner-friendly and highly adaptable, the notebook allows you to upload audio files (like `.mp3`, `.wav`, etc.) and receive fast, high-accuracy transcriptions — without needing to install anything locally.

You can also extend this solution with tools like **Microsoft Copilot** or **custom AI prompts** to generate summaries, meeting minutes, evaluations, and more.


## 🚀 Features
- ✅ Audio transcription (.mp3, .wav, etc.) <br>
- ✅ Batch transcription of multiple files <br>
- ✅ Multi-language support (Portuguese, English, etc.) <br>
- ✅ Powered by open source Whisper model <br>
- 🔄 Ready for future AI-based transcription assessment <br>

## 🧰 Requirements

To run this project on Google Colab, you don't need to install anything locally. The notebook handles all dependencies.

For local execution:

- Python 3.8+
- `whisper` (install via pip)
- `ffmpeg`
- Jupyter Notebook (or any notebook-compatible environment)

Install dependencies locally with:

```bash
pip install git+https://github.com/openai/whisper.git
sudo apt update && sudo apt install ffmpeg
```

## ▶️ How to Use (on Google Colab)

1. **Open the notebook:**  
   [**Access on GitHub**](https://github.com/fabiosousaf/whisper-audio-transcription/blob/main/google_colab.ipynb)

2. **Upload your audio file(s):**  
   The notebook supports common formats such as `.mp3`, `.wav`, `.m4a`, and more.

3. **Run the cells:**  
   The notebook will:
   - Install the necessary dependencies (`whisper`, `ffmpeg`)
   - Load the Whisper model (`tiny`, `base`, `small`, `medium`, or `large`)
   - Transcribe your audio file(s)
   - Save the transcription as `.txt`
   - Automatically offer the file for download

4. **Optional enhancements:**  
   You can modify the notebook to:
   - Choose different model sizes
   - Display transcription previews
   - Export to subtitle formats (`.srt`, `.vtt`)
   - Combine with AI tools (e.g., Microsoft Copilot) for summarization or automated evaluations

---

## 🧠 Use Case Ideas

- 📋 **Meeting transcription:** Automatically convert meeting recordings into text or minutes.
- 📢 **Customer service analysis:** Transcribe and analyze support call recordings.
- 📚 **Educational content:** Convert lecture audio into written notes.
- 📝 **Evaluations and assessments:** Generate structured evaluations based on spoken answers (e.g., in interviews or training).
- 🎬 **Subtitles for videos:** Use Whisper with timestamps for subtitle generation.
- 🎧 **Podcast and interview processing:** Turn conversations into readable summaries.

---

## 🤝 Contributions

Contributions are welcome! If you want to improve this project, feel free to:

- Fork the repository
- Submit a pull request
- Suggest new features or report issues via GitHub Issues

This project is intended to be a simple, accessible, and learning-oriented open-source initiative.  
Let’s build better tools together!
