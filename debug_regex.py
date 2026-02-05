import re

text = "“早在 1980 年，我与刘青峰就提出了传统中国社会的超稳定系统假说，反对从西方中心论的视角解读中国历史。 $ ^{①} $ 自 20 世纪 90 年代开始"

print(f"Original: {text!r}")

# The regex I used
regex_old = r"\$\s*\^\{([①-⑳])\}\s*\$"
match_old = re.search(regex_old, text)
print(f"Old Regex Match: {match_old}")

# Let's inspect the chars around the footnote
start_marker = "历史。"
end_marker = "自"
start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    snippet = text[start_idx + len(start_marker) : end_idx]
    print(f"Snippet between markers: {snippet!r}")
    print("Chars in snippet:")
    for char in snippet:
        print(f"  {char!r} U+{ord(char):04X}")

# Try a more flexible regex
regex_new = r"\$\s*\^\{([^}]+)\}\s*\$"
match_new = re.search(regex_new, text)
print(f"New Regex Match: {match_new}")
if match_new:
    print(f"New Regex Group 1: {match_new.group(1)!r}")
