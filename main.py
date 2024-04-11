from LLM_Translate import Translate
from Speech2Text import Speech2Text
import click


@click.group()
def cli():
    global s2t
    global translator
    s2t = Speech2Text()
    translator = Translate()


@click.command()
@click.option('-f', help='File to translate')
@click.option('-tgt', help='Target language :zh,en,俄语,阿拉伯语...etc')
def translate(f, tgt):
    text, src_lang = s2t.file2text(f)
    result = translator.translate(text, src_lang, tgt)
    print(f"src {src_lang}: \n{text}:")
    print("translation:\n", result)


cli.add_command(translate)
if __name__ == '__main__':
    cli()
