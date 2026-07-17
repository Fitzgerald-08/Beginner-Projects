from pathlib import Path
import click


@click.command()
@click.argument(
    "paths",
    # The nargs argument is used for passing in multiple arguments to the program, specifically
    # it must have the value -1
    nargs=-1,
    type=click.Path(exists=True, file_okay=False, readable=True, path_type=Path,)
)
def cli(paths):
    # Obtain the index of every element to keep track of the last item
    for i, path in enumerate(paths):
        if len(paths) > 1:
        # Simulate the behaviour of the ls command in Linux
            click.echo(f"{path}/:")
        # Iterate through the contents of every directory
        for entry in path.iterdir():
            click.echo(f"{entry.name} ", nl=False)

        # As long as the element is not the last one, keep on adding newline characters
        if i < len(paths) - 1:
            click.echo("\n")
        # If it is the last element in the list, do not add anything else other than one blank line
        else:
            click.echo()


if __name__ == "__main__":
    cli()