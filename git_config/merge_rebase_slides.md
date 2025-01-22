---
marp: true
---

# Merge, Rebase and Bisect
[Why?](https://gitlab.cc-asp.fraunhofer.de/code-and-coffee/fraunhofer-htl-pypackage-gitlab-template/-/network/master?ref_type=heads)

---

## Git Intro

![](https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/main/01_version_control/figs/history_linear/fig.png)

- Commits are snapshots + pointer to parent, not diffs
- Each (normal) commit has one parent commit
    - `c05f012` <-- `c05f017`
    - Pointer to parent commit goes into hash

---

## Merge Commits

- `git checkout main && git merge feature`
    ![](https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/main/01_version_control/figs/history_merge/fig.png)
- A merge commit (normally) has two parent commits `M^1` and `M^2`
    - First parent relative to the branch you are on (`M^1` = `C`, `M^2` = `E`)
    - Can't show unique diff
- `git show`
    - `git show`: *"combined diff"*
    - `git show -m`: separate diff to all parents

---

## What is the problem with nonlinear history?

- A merge takes all commits from `feature` to `main` (on `git log`).
  --> Hard to understand
- Developers often follow projects by reading commits (reading the diffs).
  --> Harder to read (where/what/...)
- Tracing bugs easier with linear history (`git bisect`)

> **Demo**: https://learngitbranching.js.org/

---

## How to get a Linear History?

- Most merge commits include no conflicts
- Linear history := no merge commits
- No changes on `main`, `git merge` does a *"fast-forward"* merge (no merge commit)
- If there are changes on `main`, rebase `feature` branch.

---

## Rebase

- `git checkout feature && git rebase main`
    ![](https://raw.githubusercontent.com/Simulation-Software-Engineering/Lecture-Material/main/01_version_control/figs/history_rebase/fig.png)
- Commits change (and new parents) --> history is **rewritten**
- If `feature` is already on remote,
    it needs a force push `git push --force-with-lease myfork feature`
- Be careful: Only use rebase if **only you** work on a branch (a local branch or a branch on your fork).
- For local branches very helpful: `git pull --rebase` (fetch & rebase)
> **Demo**: https://learngitbranching.js.org/

---

## GitLab PR Merge Variants

- GitLab offers three ways to merge a non-conflicting (no changes in same files) PR:
    - Merge commit
        Every merge creates a merge commit
    - Merge commit with semi-linear history
        Every merge creates a merge commit
        Merging is only allowed when the source branch is up-to-date with its target
        When semi-linear merge is not possible, the user is given the option to rebase
    - **Fast-forward merge**
        No merge commits are created
        Fast-forward merges only
        When there is a merge conflict, the user is given the option to rebase

> https://gitlab.cc-asp.fraunhofer.de/sha79396/merge-rebase-bisect-demo/-/settings/merge_requests

---

## Summary and Final Remarks

- Try to keep a linear history with rebasing whenever reasonable
- Don't use rebase on a public/shared branch during development
- Squash before merging if reasonable
- Delete `feature` branch after merging
- Local view: `git log --graph`

---

## Further Reading

- [Merge methods on GitLab](https://docs.gitlab.com/ee/user/project/merge_requests/methods/)
- [Bitbucket docs: "Merging vs. Rebasing"](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)
- [Hackernoon: "What's the diff?"](https://hackernoon.com/git-merge-vs-rebase-whats-the-diff-76413c117333)
- [GitHub Blog: "Commits are snapshots, not diffs"](https://github.blog/2020-12-17-commits-are-snapshots-not-diffs/)
- [Stack Overflow: "Git show of a merge commit"](https://stackoverflow.com/questions/40986518/git-show-of-a-merge-commit?)
- [Rebase and force push](https://docs.gitlab.com/ee/topics/git/git_rebase.html)
- [git rebase vs git merge --ff-only](https://stackoverflow.com/questions/28140434/is-there-a-difference-between-git-rebase-and-git-merge-ff-only)


---

## Bisect

![bg fit](800px-Bisection_method.svg.png)

---

## Bisect
```
mkdir git_bisect_tests
cd git_bisect_tests
git init
```

```
echo row > test.txt && git add -A && git commit -m "Adding first row"
echo row >> test.txt && git add -A && git commit -m "Adding second row"
echo row >> test.txt && git add -A && git commit -m "Adding third row"
echo your >> test.txt && git add -A && git commit -m "Adding the word 'your'"
echo boat >> test.txt && git add -A && git commit -m "Adding the word 'boat'"
echo gently >> test.txt && git add -A && git commit -m "Adding the word 'gently'"
sed -i -e 's/boat/car/g' test.txt 
git add -A && git commit -m "Changing the word 'boat' to 'car'"
echo down >> test.txt && git add -A && git commit -m "Adding the word 'down'"
echo the >> test.txt && git add -A && git commit -m "Adding the word 'the'"
echo stream >> test.txt && git add -A && git commit -m "Adding the word 'stream'"
cat test.txt
```
---

## Bisect
- `git log`
- `git bisect start`
- `git bisect bad commit-id`
- `git bisect good commit-id`
- `cat test.txt`
- `git bisect good`, `git bisect bad`
- `git bisect reset`
<br>
> `git bisect run ./test.sh`

---

## Further Reading

- [How To Use Git Bisect](https://initialcommit.com/blog/git-bisect)
- [Git bisect automation](https://gist.github.com/cheeming/2976658)
