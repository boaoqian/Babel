import whisper
import yaml


class Speech2Text:
    def __init__(self):
        with open('./model.yaml', 'r') as file:
            data_from_file = yaml.load(file, Loader=yaml.FullLoader)
            model_name = data_from_file['whisper_name']
        self.model = whisper.load_model(model_name)

    def file2text(self,path):
        audio = whisper.load_audio(path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
        _, probs = self.model.detect_language(mel)
        options = whisper.DecodingOptions()
        result = whisper.decode(self.model, mel, options)
        return result.text, max(probs, key=probs.get)  #text, src_lang
