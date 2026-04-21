# whisper-rap-queb

DEMO: https://colab.research.google.com/github/ras0k/whisper-rap-queb/blob/main/whisper_rap_queb_v10.ipynb

This project proposes a study of automatic transcription for Quebec rap lyrics. By leveraging OpenAI’s Whisper model, extracting text via Genius.com, and analyzing the Word Error Rate (WER), this project aims to achieve a statistically significant reduction in Whisper’s WER when applied to rap music. Accuracy will first be evaluated using a specific benchmark designed for this task. Subsequently, a corpus of approximately 500 to 1000 songs will be constructed and used to fine-tune the model. Finally, a report will synthesize the results and statistical analyses. This project serves as an exploratory foundation for other larger-scale fine-tuning efforts, such as "whisper-rap-fr" or simply "whisper-rap".

Trained Model: https://huggingface.co/ras0k/whisper-rap-queb-v10

Dataset: https://huggingface.co/datasets/ras0k/Genius-Quebec-Rap-Top500
