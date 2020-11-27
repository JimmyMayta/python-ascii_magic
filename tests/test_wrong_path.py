from context import ascii_magic

output = ascii_magic.from_image_file('nope.jpg')
ascii_magic.to_terminal(output)