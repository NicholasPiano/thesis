# word counts and tree structure

import os
from os.path import join, isdir

def word_count(file_path):
  count = 0
  with open(file_path) as f:
    for line in f.readlines():
      count += len(line.split(' '))

  return count

root_path = '/Users/nicholaspiano/Documents/Employment/Cambridge/thesis/main'
progress_path = join(root_path, 'progress.txt')

# for each folder in root directory
with open(progress_path, 'w+') as progress_file:
  total_words = 0
  for section in [s for s in os.listdir(root_path) if ('.DS' not in s and isdir(join(root_path, s)))]:

    section_path = join(root_path, section)
    section_total_words = 0
    progress_file.write('{}\n'.format(section))

    for subsection in [s for s in os.listdir(section_path) if ('.DS' not in s)]:

      subsection_path = join(section_path, subsection)
      subsection_total_words = 0

      if isdir(subsection_path):
        progress_file.write('-- {}\n'.format(subsection))
        for subsubsection in [s for s in os.listdir(subsection_path) if ('.DS' not in s)]:

          subsubsection_path = join(subsection_path, subsubsection)
          subsubsection_total_words = word_count(subsubsection_path)
          progress_file.write('-- -- {} words -- {}\n'.format(subsubsection_total_words, subsubsection))
          subsection_total_words += subsubsection_total_words

        progress_file.write('-- {} words\n'.format(subsection_total_words))
        progress_file.write('\n')

      else:
        subsubsection_total_words = word_count(subsubsection_path)
        subsection_total_words += subsubsection_total_words
        progress_file.write('-- {} words -- {}\n'.format(subsubsection_total_words, subsection))
        progress_file.write('\n')

      section_total_words += subsection_total_words

    total_words += section_total_words

    progress_file.write('{} words\n'.format(section_total_words))
    progress_file.write('\n')
    progress_file.write('\n')

  progress_file.write('{} words\n'.format(total_words))
