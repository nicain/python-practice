"""Given an array of strings emails where we send one email to each emails[i], 
return the number of different addresses that actually receive mails.

Every valid email consists of a local name and a domain name, separated by the 
'@' sign. Besides lowercase letters, the email may contain one or more '.' or 
'+'

If you add periods '.' between some characters in the local name part of an 
email address, mail sent there will be forwarded to the same address without 
dots in the local name. Note that this rule does not apply to domain names.

If you add a plus '+' in the local name, everything after the first plus sign 
will be ignored. This allows certain emails to be filtered. Note that this 
rule does not apply to domain names."""

source_url = 'https://leetcode.com/problems/unique-email-addresses/'

card_url = None

from typing import List

def answer(emails: List[str]) -> int:
  emails_received = set()
  for email in emails:
    prefix, suffix = email.split("@")
    prefix = prefix.replace('.','')
    prefix_split_list = prefix.split('+')
    prefix = prefix_split_list[0]
    repaired_email = f'{prefix}@{suffix}'
    emails_received.add(repaired_email)
  return len(emails_received)


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        return answer(emails)


def test_case1():
  emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
  expected_result = 2
  assert expected_result == answer(emails)


def test_case2():
  emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
  expected_result = 3
  assert expected_result == answer(emails)


if __name__ == "__main__":
  import pytest
  pytest.main([__file__])