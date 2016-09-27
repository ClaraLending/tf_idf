# Term Frequency - Inverse Document Frequency: Practice Repo

## Setup

1. If necessary, register for a Cloud9 IDE account. (http://c9.io/)
2. Sign into Cloud9 IDE. Create a new workspace.
    1. Name the workspace in the `Workspace name` field. For example: `tf_idf`. Add a description if you like.
    2. Set the repo in the `Clone from Git or Mercurial URL` field to `https://github.com/WomenWhoCode/tf_idf.git`.
    3. Click `Create Workspace`.
3. If necessary, open the workspace.
4. Prepare the Cloud9 virtual machine.
    1. `sudo pip3 install -r requirements.txt`
    2. Download the NLTK sample corpora.
        1. `python3`
        2. `import nltk`
        3. `nltk.download()`
        4. Exit the Python interpreter (press `Ctrl-D`).

## Development

1. Run `rake test`. Make the tests pass!
2. Run `python3 -m tf_idf.main` to run the webserver to see results.