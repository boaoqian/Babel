# Babel: 多语言翻译工具
Babel是一个基于Python的多语言翻译工具，它利用了最新的语言模型和语音识别技术，可以将音频文件翻译成多种语言。该工具提供了命令行接口，方便用户进行操作。
## 安装
在开始使用Babel之前，请确保您的系统中已安装了Python。然后，您可以通过以下命令安装Babel及其依赖库：
```bash

```
确保安装了以下库：
- `PyYAML`: 用于处理YAML文件。
- `whisper`: 用于语音识别。
- `ZhipuAI`: 用于调用LLM
- `click`: 用于创建命令行界面。
## 使用方法
Babel的使用非常简单，只需通过命令行传递相应的参数即可。
### 翻译音频文件
要将音频文件翻译成指定语言，请使用以下命令：
```bash
babel-translate -f <file> -tgt <target_language>
```
其中，`<file>`是您要翻译的音频文件路径，`<target_language>`是您要翻译成的目标语言代码，例如`zh`、`en`、`ru`（俄语）、`ar`（阿拉伯语）等。
例如，要将一个名为`example.wav`的音频文件翻译成中文，请使用以下命令：
```bash
babel-translate -f example.wav -tgt zh
```
## 示例
以下是一个使用Babel将英语音频文件翻译成中文的示例：
1. 准备一个英语音频文件，例如`example.wav`。
2. 使用以下命令将音频文件翻译成中文：
```bash
babel-translate -f example.wav -tgt zh
```
3. Babel将输出翻译结果，如下所示：
```
src en:
This is an example.
translation:
这是一个例子。
```
## 支持的语言
Babel支持多种语言，您可以通过传递相应的语言代码作为`<target_language>`参数来指定目标语言。
您可以传递语言的全称，或者简写。

## 许可证
Babel是开源软件，遵循[MIT License]。
祝您使用愉快！
