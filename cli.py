import click

from github_utils import get_assets_link


@click.group()
def cli():
    pass


@cli.command()
@click.argument('pecha_num')
def asset(**kwargs):
    asset_links = get_assets_link(kwargs['pecha_num'])
    click.echo(asset_links)
