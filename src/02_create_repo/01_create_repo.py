from subprocess import call

print('type \'y\' to host on github publicly (otherwise bitbucket)')
prompt = '> '

on_github = raw_input(prompt) == 'y'
print(on_github)
if on_github:
    call(['cygstart', 'https://github.com/new'])
else:
    call(['cygstart', 'https://bitbucket.org/repo/create'])
print('name of repository:')
repo_name = raw_input(prompt)

if on_github:
    call(['bash', '-x', 'src/02_create_repo/02_init.sh', repo_name, 'github'])
else:
    call(['bash', '-x', 'src/02_create_repo/02_init.sh', repo_name, 'bitbucket'])
