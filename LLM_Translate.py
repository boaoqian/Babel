from zhipuai import ZhipuAI
import yaml, json, re


class Translate:
    def __init__(self):
        """read model.yaml"""
        api_key = ""
        self.llm_name = ""
        with open('./model.yaml', 'r') as file:
            data_from_file = yaml.load(file, Loader=yaml.FullLoader)
            api_key = data_from_file['api_key']
            self.llm_name = data_from_file['llm_name']
        self.client = ZhipuAI(api_key=api_key)

    def translate(self, text, src_lang, tgt_lang):
        response = self.client.chat.completions.create(
            model=self.llm_name,
            messages=[
                {"role": "user",
                 "content": f"""你是一个多语言翻译助手，请帮助我将以下文本从 [{src_lang}] 翻译成 [{tgt_lang}]。翻译完成后，请以 JSON 格式输出
                 ，其中包含源语言和目标语言的标签，以及翻译结果。JSON 对象应该包含 ‘source_language’、‘target_language’ 和 ‘translation’ 
                 三个键,需要翻译的文本为{text}"""}])
        match = re.search(r"""```json$(.*?)^```""", response.choices[0].message.content, re.MULTILINE | re.DOTALL)
        result = json.loads(match.group(1))
        return result["translation"]
