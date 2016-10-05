from subprocess import call

print('type \'y\' to host on github publicly (otherwise bitbucket)')
prompt = '> '

on_github = input(prompt) == 'y'
print(on_github)
if on_github:
    call(['cygstart', 'https://github.com/new'])
else:
    call(['cygstart', 'https://bitbucket.org/repo/create'])
