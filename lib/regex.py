import re
patterns = [
    "It's such a lovely day today.",
    "Some weather we're having today, huh?",
    "Maybe today's just not my day."
]
my_pattern = '|'.join(re.escape(pattern) for pattern in patterns)

my_regex = re.compile(my_pattern)

