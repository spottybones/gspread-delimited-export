"""
cli.py - generate the CLI
"""

import click


@click.command()
def cli():
    click.echo("Hello world")