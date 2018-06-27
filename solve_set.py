#!/usr/bin/env python
"""Solve SET from a game image. Prints the sets found, and optionally
writes and/or displays the game image with the sets indicated.
"""

import argparse
import sys
from SetGame import SetGame
from common import game_img_filename

def get_args():
  parser = argparse.ArgumentParser(description='Solve SET from a game image.')
  parser.add_argument('filename', metavar='filename', type=str, nargs='?')
  parser.add_argument('--game', dest='game_num', type=int)
  parser.add_argument('--write', dest='write', action='store_true')
  parser.add_argument('--display', dest='display', action='store_true')
  return parser.parse_args()

def main():
  args = get_args()
  if args.game_num:
    filename = game_img_filename(args.game_num)
  else:
    filename = args.filename
  game = SetGame(filename)
  game.solve()
  game.print_sets()
  game.draw_sets()
  if args.write:
    game.write_im('solved.jpg')
  if args.display:
    game.display()

if __name__ == "__main__":
  main()
