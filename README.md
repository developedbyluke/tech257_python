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

![Git Three Stages](C:\Users\luke\Downloads\image.png)

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
