from transformers import pipeline
import click


generator = pipeline("summarization", model="t5-base")


def summarize(text):
    result = generator(text, max_length=100)
    click.echo("Summarization complete!")
    click.echo("=" * 80)
    return result[0]["summary_text"]

@click.command()
@click.argument('path', type=click.Path(exists=True))
def main(path):
    with open(path, 'r') as _f:
        text = _f.read()
    click.echo(f"Summarized text path: {path}")
    click.echo(summarize(text))
    
if __name__ == "__main__":
    main()