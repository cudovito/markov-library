from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='markov-library',
    version='0.1.2',
    # Short description
    description='This library contains the code of markov chains',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    # MIT
    license='',
    packages=find_packages(),
    author='Saurabh Waradkar, Rishabh Bhardwaj',
    author_email='waradkarsaurabh@gmail.com, rishabhb932@gmail.com',
    # Search keywords to find library
    keywords=[],
    # Git hub repo url
    url='',
    # https://pypi.org/project/...
    download_url=''
)

# Libraries required with version
install_requires = [
    
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)