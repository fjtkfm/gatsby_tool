import click
import random
import string
import datetime
import os


@click.command()
@click.option('--slug', default='', help='Page Slug')
@click.option('--title', default='', help='Page Title')
@click.option('--tags', default='', help='Page Tags')
@click.option('--path', default=os.getenv('GATSBY_PATH', '.'), help='Page Slug')
def cmd(slug, title, tags, path):
  if slug == '':
    slug = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

  if len(tags) > 0:
    tags = ', '.join(["'{}'".format(tag) for tag in tags.split(',')])
  
  header = []
  header.append('---')
  header.append('title: {}'.format(title))
  header.append('date: {}'.format(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')))
  header.append('tags: [{}]'.format(tags))
  header.append('---')
  header.append('')

  dir_path = '{}/content/blog/{}'.format(path, slug)
  os.makedirs(dir_path)


  with open('{}/index.md'.format(dir_path), 'w') as f:
    f.write('\n'.join(header))


def main():
  cmd()


if __name__ == '__main__':
  main()