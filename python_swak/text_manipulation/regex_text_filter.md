[quickstart](https://www.regular-expressions.info/quickstart.html)

[regex101](https://regex101.com/)

Regular expressions (regex) are used to match patterns in strings. Here are some basic search patterns in regex:

1. **Literal Characters**: The most basic pattern is the exact match or literal match.

   ```regex
   python
   ```
   This pattern matches the string "python" exactly.

2. **Metacharacters**: These are special characters that have a unique meaning in regex. They include `. ^ $ * + ? { } [ ] \ | ( )`.

3. **Wildcard Character (`.`)**: The dot `.` is a special character that matches any character except newline (`\n`).

   ```regex
   p.t
   ```
   This pattern matches "pat", "pet", "pit", "pot", "put", and so on.

4. **Character Sets (`[]`)**: A character set matches any one character enclosed in the square brackets.

   ```regex
   [aeiou]
   ```
   This pattern matches any vowel.

5. **Negated Character Sets (`[^]`)**: A negated character set matches any character that is not in the square brackets.

   ```regex
   [^aeiou]
   ```
   This pattern matches any non-vowel character.

6. **Quantifiers (`*`, `+`, `?`, `{}`)**: Quantifiers specify how many instances of a character, group, or character set must be present in the input for a match to be found.

   ```regex
   a*
   ```
   This pattern matches zero or more 'a' characters.

7. **Anchors (`^`, `$`)**: The caret `^` matches the start of the string, and the dollar `$` matches the end of the string.

   ```regex
   ^p
   ```
   This pattern matches any string that starts with 'p'.

8. **Escape Sequences (`\`)**: If you need to match one of the special characters, you can escape it with a backslash `\`.

   ```regex
   \.
   ```
   This pattern matches a period '.'

9. **Groups (`()`)**: Parentheses `()` are used to define groups of characters that can be treated as a single unit.

   ```regex
   (py)+
   ```
   This pattern matches one or more 'py' strings, like 'py', 'pypy', 'pypypy', and so on.

These are just the basics. Regular expressions can be much more complex and powerful, allowing you to match a wide variety of patterns in text.