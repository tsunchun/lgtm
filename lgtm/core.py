import click


@click.command()
@click.option('--message', '-m', default='LGTM',
              show_default=True, help='画像に乗せる文字列')
def cli():
    """LGTM画像生成ツール"""
    lgtm()
    click.echo('lgtm')


def lgtm():
    pass
