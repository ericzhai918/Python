import re

WORD_RE = re.compile(r'\w+')

for match in WORD_RE.finditer(
        "The United Nations' Human Rights Council has given China a passing grade in its latest review of China's human rights development."):
    word = match.group()
    column_no = match.start() + 1
    print(word, column_no)
