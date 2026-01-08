def palindromes (words_list):
    return [word for word in words if word == word[::-1]]

words = input().split()
palindrome_word = input()


result = palindromes(words)

print(result)
print(f"Found palindrome {result.count(palindrome_word)} times")