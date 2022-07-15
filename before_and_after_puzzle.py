"""Given a list of phrases, generate a list of Before and After puzzles.

A phrase is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

Before and After puzzles are phrases that are formed by merging two phrases where the last word of the first phrase is the same as the first word of the second phrase.

Return the Before and After puzzles that can be formed by every two phrases phrases[i] and phrases[j] where i != j. Note that the order of matching two phrases matters, we want to consider both orders.

You should return a list of distinct strings sorted lexicographically."""

source_url = 'https://leetcode.com/problems/before-and-after-puzzle/'

title = 'Before and After Puzzle'

card_url = 'https://www.brainscape.com/decks/11570817/cards/390225909/edit'

import collections

def answer(phrases):
  first_word_to_phrase_dict = collections.defaultdict(list)
  last_word_to_phrase_dict = collections.defaultdict(list)
  for pi, phrase in enumerate(phrases):
    words = phrase.split()
    first_word_to_phrase_dict[words[0]].append((words, pi))
    last_word_to_phrase_dict[words[-1]].append((words[:-1], pi))

  final_phrase_list = []
  for key, words_list in last_word_to_phrase_dict.items():
    for words, pi1 in words_list:
      for matching_words, pi2 in first_word_to_phrase_dict[key]:
        if pi1 != pi2:
          final_phrase_list.append(' '.join(words+matching_words))
  return sorted(set(final_phrase_list))


class Solution:
  def beforeAndAfterPuzzles(self, *args, **kwargs):
    return answer(*args, **kwargs)


def test_case1():
  args = (["writing code","code rocks"],)
  expected_result = ["writing code rocks"]
  result = answer(*args)
  assert expected_result == result


def test_case2():
  args = ([
    "mission statement",
    "a quick bite to eat",
    "a chip off the old block",
    "chocolate bar",
    "mission impossible",
    "a man on a mission",
    "block party",
    "eat my words",
    "bar of soap"
  ],)
  expected_result = [
    "a chip off the old block party",
    "a man on a mission impossible",
    "a man on a mission statement",
    "a quick bite to eat my words",
    "chocolate bar of soap"
  ]
  result = answer(*args)
  assert expected_result == result


def test_case3():
  args = (["a","b","a"],)
  expected_result = ["a"]
  result = answer(*args)
  assert expected_result == result


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])