import click
import random
import string
import datetime


@click.command()
@click.option('--slug', default='', help='Page Slug')
@click.option('--title', default='', help='Page Title')
@click.option('--tags', default='', help='Page Tags')
def cmd(slug, title, tags):
  if slug == '':
    slug = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

  if len(tags) > 0:
    tags = ', '.join(["'{}'".format(tag) for tag in tags.split(',')])

  header = []
  header.append('---')
  header.append('title: {}'.format(title))
  header.append('date: {}'.format(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')))
  header.append('tags: {}'.format(tags))
  header.append('---')
  header.append('')

  with open('./{}.md'.format(slug), 'w') as f:
    f.write('\n'.join(header))


def main():
  cmd()


if __name__ == '__main__':
  main()