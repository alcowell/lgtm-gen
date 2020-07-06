import click


@click.command
def cli():
    """LGTM画像生成ツール"""
    lgtm()
    click.echo("lgtm")  # 動作確認用


def lgtm():
    pass
