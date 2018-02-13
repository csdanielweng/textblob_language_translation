import os
import argparse
from textblob import TextBlob


def main(FLAGS):
  input_file = FLAGS.input_file
  output_file = FLAGS.output_file
  language_from = FLAGS.language_from
  language_to = FLAGS.language_to

  current_dir = os.getcwd()

  if input_file == '':
    print('use default input file input' + language_from + '.txt')
    input_file = current_dir + "/input_" + language_from + ".txt"
    
  if output_file == '':
    output_file = current_dir + "/output_" + language_to + '.txt'  

  f_in = open(input_file, 'r')
  f_out = open(output_file, 'w')

  input_lines = [line for line in f_in]

  for i in range(len(input_lines)):
    t = TextBlob(input_lines[i])
    output = str(t.translate(from_lang=language_from, to=language_to))
    f_out.write(output + "\n")

  f_in.close()
  f_out.close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--language_from',
      type=str,
      default='en',
      help='Specify the translation from which language.')   
  parser.add_argument(
      '--language_to',
      type=str,
      default='zh-TW',
      help='Specify the tanslation to which language.')   
  parser.add_argument(
      '--input_file',
      type=str,
      default='',
      help='Specify the input file.')      
  parser.add_argument(
      '--output_file',
      type=str,
      default='',
      help='Specify the output file.')
      
  FLAGS, unparsed = parser.parse_known_args()
  
  main(FLAGS)
