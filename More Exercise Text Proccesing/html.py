title = input()
content = input()

print(f"<h1>\n\
    {title}\n\
</h1>")

print(f"<article>\n\
    {content}\n\
</article>")

command = input()
while command != "end of comments":
    print(f'<div>\n\
    {command}\n\
</div>')

    command = input()

