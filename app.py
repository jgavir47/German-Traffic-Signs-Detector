import click
import urllib.request

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)
#
# if __name__ == '__main__':
#     hello()
# /////////////////////////////////////////////////////////////////////
#
#  def dowload ()
#x = [[10,15],[13,16],[14,17],[32,4],[5,2],[22,10]]
#y= [0,0,1,1,0,1]
@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('I was invoked without subcommand')
    else:
        click.echo('I am about to invoke %s' % ctx.invoked_subcommand)

@cli.command()
def download():
    urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/6/63/African_elephant_warning_raised_trunk.jpg","elephant")
    urllib.request.urlretrieve("FullIJCNN2013.zip")

if __name__=='__main__':
    cli()
