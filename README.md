# Python and Markdown

## Markdown basics

The `print()` function prints something to the screen: `print("Hello world!)`

```python
# Print message to the screen
print("Hello world!")
```

### Highlighting text

Wrap something in asterisks or underscores to get *italics*<br>
Wrap something in double asterisks to get **bold text**

### Lists

**Bullet points**
- Hello
  - Hello
  - Hello
- Hello

**Numbered List**
1. Hello
2. Hello
3. Hello

# Git

Git is a distributed version control system.

### Centralised vs Distributed VCS

- A **Centralised VCS** stores all project files on a central server, with developers downloading files to work on them. This creates a single point of failure which increases the risk of data loss.
- A **Distributed VCS** allows each developer to have a complete copy of the entire project, making it possible to work together simultaneously as well as reducing the risk of data loss.

![Centralised vs Distributed VCS](https://www.researchgate.net/profile/Sofia-Feist/publication/316553817/figure/fig2/AS:669480740982806@1536628055836/Centralized-Version-Control-vs-Distributed-Version-Control.ppm)

### Three Stages of Git

1. **Modified**: Changes made to files.
2. **Staged**: Files marked for inclusion in the next commit.
3. **Committed**: Data securely stored in your local repository.

### Common Workflow Commands

```
git init                 # Initialize a new Git repo
git add .                # Stage all modified files
git commit -m "message"  # Commit your changes
git push                 # Push changes to remote repo
git pull                 # Update local repo with remote changes
git log                  # View commit history
git diff <id> <id>       # View the difference between two commits
git checkout <id>        # SAFE revert locally to a previous commit to review files
git checkout <branch>    # Switch to a different branch
git reset --hard <id>    # DANGEROUS revert to previous commit id's state and destroy all changes since
git rm --cached          # Remove something from the git cache
```

### Branching

Branching in Git lets developers separate from the main line of development to continue to work independently without interfering with each other's changes.

Branching allows developers to work on new features or bug fixes in isolation from the main codebase.

Branching also allows developers to experiment with new ideas or approaches without the risk of affecting the main branch if something goes wrong.

## Difference Between Git and GitHub

While Git and GitHub are often mentioned together, they serve different roles in the development process. Git is a version control system that allows you to track changes, revert to previous stages, and collaborate on code. GitHub, on the other hand, is a hosting service for Git repositories, providing a web-based graphical interface. It offers several collaboration features such as bug tracking, feature requests, task management, and continuous integration.

**Git**  is a tool you install locally on your machine to manage your codebase, while **GitHub**  is a service you use online to store your Git-managed projects and collaborate with others.
### Syncing Local and Remote Repositories

There are primarily two methods to sync your local repository with a remote repository: 
1. **git push** : This command sends your committed changes to a remote repository. It's used to update the remote repository with the changes you've made locally. 
2. **git pull** : This command fetches the changes from a remote repository and merges them into your local repository. It's used to keep your local repository up-to-date with the remote repository.
### Syncing Local Repo to Remote Repo

1. **Initialise a local Git repository**:

```
git init
``` 
2. **Add the remote repository**:

```
git remote add origin <url>
```
3. **Push your changes to the remote repository**:

```
git push -u origin main
```

```
Local Repo (Your machine)
       |
       | git push
       ↓
Remote Repo (GitHub)
       |
       | git pull
       ↓
Local Repo (Collaborator's machine)
```


### Removing a Folder/File from Remote Repository

1. **Delete the folder/file locally**:

```
git rm -r <folder-name>
git rm <file-name>
``` 
2. **Commit**:

```
git commit -m "Remove specific folder/file"
``` 
3. **Push the changes to the remote repository**:

```
git push
```
### Using a .gitignore File

The `.gitignore` file is used to tell Git which files or directories to ignore in a project. To use a `.gitignore` file: 
1. create a `.gitignore` file in your project's root directory.
2. Add patterns for the files/directories to ignore: 
   - For example, to ignore all `.txt` files, add `*.txt` to the `.gitignore` file. 
   - To ignore a specific directory, add the path to the directory.
3. Commit:

```
git add .gitignore
git commit -m "Add .gitignore file"
```
