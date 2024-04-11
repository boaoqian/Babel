# Babel: A Multilingual Translation Tool
Babel is a Python-based multilingual translation tool that leverages the latest language models and speech recognition technology to translate audio files into multiple languages. This tool provides a command-line interface for easy user operation.
## Installation
Before using Babel, ensure that Python is installed on your system. Then, you can clone Babel and install its dependent libraries with the following command:
```bash
pip install -r requirements.txt
```
Make sure the following libraries are installed:
- `PyYAML`: For handling YAML files.
- `whisper`: For speech recognition.
- `ZhipuAI`: For calling the LLM.
- `click`: For creating a command-line interface.
## ZhipuAI API Key

To use the LLM, you need to obtain an API key. Follow these steps to get your key:

    Visit the ZhipuAI website and sign up for an account.
    Once you have an account, navigate to the API key section.
    Generate a new API key or use an existing one.

After obtaining your API key, you need to add it to the Babel configuration file. This file is typically named model.yaml and is located in the root directory of the Babel project.

Open model.yaml in a text editor and add your API key under the ZhipuAI section:
```yaml
api_key: #your_api_key_here
llm_name: glm-3-turbo
whisper_name: small
```
Replace 'your_api_key_here' with the actual API key you obtained from ZhipuAI.
## Usage
Babel is very simple to use; just pass the appropriate parameters through the command line.
### Translating Audio Files
To translate an audio file into a specified language, use the following command:
```bash
python main.py translate  -f <file> -tgt <target_language>
```
Where `<file>` is the path to the audio file you want to translate, and `<target_language>` is the target language code, such as `zh`, `en`, `ru` (Russian), `ar` (Arabic), etc.
For example, to translate an audio file named `example.wav` into Chinese, use the following command:
```bash
python main.py translate -f example.wav -tgt zh
```
## Example
Here is an example of using Babel to translate an English audio file into Chinese:
1. Prepare an English audio file, such as `example.wav`.
2. Use the following command to translate the audio file into Chinese:
```bash
python main.py translate  -f example.wav -tgt zh
```
3. Babel will output the translation result, as shown below:
```
src en:
This is an example.
translation:
这是一个例子。
```
## Supported Languages
Babel supports multiple languages. You can specify the target language by passing the corresponding language code as the `<target_language>` parameter.
You can pass the full name of the language or its abbreviation.
## License
Babel is open-source software, licensed under the [MIT License].
Enjoy using Babel!
