import os
import argparse
import click

@click.command()
@click.option('--dir/--no-dir', '-d', default=False)
@click.argument('name')

def main(dir, name):
    if dir:
        def dir_output(path, symbol=''):
                print('{}├── {}'.format(symbol, os.path.basename(path)))
                for item in os.listdir(path):
                    p = os.path.join(path, item)
                    if os.path.isdir(p):
                        dir_output(p, symbol + '| ')
        dir_output(name)
    else:
        def dir_output(path, symbol=''):
                print('{}├── {}'.format(symbol, os.path.basename(path)))
                for item in os.listdir(path):
                    p = os.path.join(path, item)
                    if os.path.isdir(p):
                        dir_output(p, symbol + '| ')
                    else:
                        print('{}│  ├──  {}'.format(symbol, item))
        dir_output(name)

if __name__ == '__main__':
    main()
