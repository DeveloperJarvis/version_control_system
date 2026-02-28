# LLD of Version control system

covering:

- Object storage
- Hashing
- Commit DAG
- Branching
- Diffing
- File system modeling

No code — only structure, responsibilities, and data flow.

---

# 1⃣ Functional Requirements

### Core Features

1. `init` – initialize repository
2. `add` – stage files
3. `commit` – create snapshot
4. `log` – show commit history
5. `diff` – show changes
6. `branch` – create branch
7. `checkout` – switch branch

---

# 2⃣ High-Level Architecture

Mini Git is fundamentally:

> A content-addressable object store + DAG of commits

---

# 3⃣ Core Concepts

## A) Content Addressable Storage (CAS)

Every object is stored by:

```
hash(content)
```

This guarantees:

- Immutability
- Deduplication
- Integrity

We use SHA-1 or SHA-256.

---

## B) Objects in the System

Git stores 3 core object types:

| Type   | Purpose             |
| ------ | ------------------- |
| Blob   | File content        |
| Tree   | Directory structure |
| Commit | Snapshot pointer    |

We will replicate that.

---

# 4⃣ Object Model (LLD)

## 1. Repository

### Responsibilities

- Manage object store
- Maintain HEAD pointer
- Manage branches
- Coordinate commands

### Attributes

- `.vcs/objects/`
- `.vcs/refs/heads/`
- `.vcs/HEAD`
- staging area (index)

---

## 2. Object Store

### Responsibility

- Store and retrieve objects by hash
- Deduplicate identical content

### Methods

- `write_object(obj) → hash`
- `read_object(hash)`
- `exists(hash)`

### Storage Format

```
.vcs/
    objects/
        ab/
            cdef1234...
```

(hash split for scalability)

---

## 3. Blob

Represents file content.

### Fields

- content (bytes)
- hash

### Hash Computation

```
hash("blob" + content)
```

Immutable.

---

## 4. Tree

Represents directory snapshot.

### Fields

- list of entries

Each entry:

```
{
    name,
    type (blob/tree),
    hash
}
```

Tree hash:

```
hash("tree" + sorted(entries))
```

Important:
Sorting ensures deterministic hashing.

---

## 5. Commit

Represents snapshot.

### Fields

- tree_hash
- parent_hash(es)
- author
- message
- timestamp

### Commit Hash

```
hash("commit" + tree_hash + parents + metadata)
```

This forms a DAG.

---

# 5⃣ DAG Structure

Commits form:

```
A → B → C
      ↘ D
```

Each commit stores:

- pointer to parent(s)

This creates:

- linear history
- branching
- merging support

---

# 6⃣ Staging Area (Index)

The index tracks:

```
file_path → blob_hash
```

Workflow:

```
add → update index
commit → convert index into tree
```

Index is mutable.
Commits are immutable.

---

# 7⃣ Branch Model

Branches are just pointers.

Example:

```
refs/heads/main → commit_hash
refs/heads/feature → commit_hash
```

HEAD contains:

```
ref: refs/heads/main
```

Branch creation:

```
new_branch → copy current commit hash
```

Branch switching:

- Update HEAD pointer
- Restore working directory from commit tree

---

# 8⃣ Command Design (LLD)

---

## 1⃣ init

### Steps:

- Create `.vcs/`
- Create objects directory
- Create refs/heads
- Set HEAD → main
- Create empty index

---

## 2⃣ add

### Steps:

1. Read file
2. Create Blob
3. Store blob in object store
4. Update index mapping

---

## 3⃣ commit

### Steps:

1. Build tree from index
2. Store tree object
3. Create commit object
4. Store commit
5. Update branch pointer
6. Clear index

---

## 4⃣ log

Traverse commit graph:

```
current = HEAD
while current:
    print commit
    current = parent
```

---

## 5⃣ diff

Two strategies:

### A) Working Directory vs HEAD

Compare:

- Current file content
- Blob content from HEAD tree

### B) Commit vs Commit

Compare tree hashes:

- If blob hash differs → file changed

Line-level diff:

- Use LCS (Longest Common Subsequence)
- Or Myers diff algorithm

---

## 6⃣ branch

Create new ref:

```
refs/heads/new_branch → current_commit_hash
```

---

## 7⃣ checkout

Steps:

1. Update HEAD reference
2. Load commit tree
3. Rewrite working directory to match tree

---

# 9⃣ Class Diagram (Conceptual)

```
Repository
 ├── ObjectStore
 ├── Index
 ├── RefManager
 ├── WorkingDirectory
```

---

## ObjectStore

- write(obj)
- read(hash)

## Index

- add(file)
- clear()
- get_entries()

## Commit

- serialize()
- deserialize()

## Tree

- build_from_index()
- serialize()

## RefManager

- get_head()
- update_head()
- create_branch()

---

# 🔟 Storage Layout

```
project/
    file1.txt
    file2.txt
    .vcs/
        objects/
        refs/
            heads/
                main
        HEAD
        index
```

---

# 1⃣1⃣ How Branching Actually Works

When branching:

```
main → C
feature → C
```

After committing on feature:

```
main → C
feature → D
```

Because commit D points to C.

No duplication needed.

Just pointer manipulation.

---

# 1⃣2⃣ Complexity Analysis

### Hashing

O(file_size)

### Commit creation

O(number_of_files)

### Log traversal

O(number_of_commits)

### Diff

O(n\*m) for naive LCS
O(ND) for Myers algorithm

---

# 1⃣3⃣ Immutability Guarantees

Objects never change.
Only references move.

This is the core design strength.

---

# 1⃣4⃣ Interview-Level Insights

Strong candidates mention:

- Content addressable storage
- Immutability
- DAG for history
- Branch = pointer
- Merge commit has 2 parents
- Deterministic hashing via sorted entries
- Object deduplication

---

# 1⃣5⃣ How This Scales

Real Git adds:

- Pack files
- Delta compression
- Garbage collection
- Reflog
- Merge algorithms
- Rebase

But core architecture remains identical.

---

# 🎯 Final Architecture Summary

Mini Git =

```
Content Addressable Object Store
+ DAG of Commits
+ Mutable Branch References
+ Working Directory Sync
+ Diff Engine
```

## Next Steps

Now we move from **“toy Git”** → to a **real VCS architecture**:

- Working directory restoration design
- Full tree traversal diff design
- Merge algorithm design
- Rebase algorithm design
- Remote push/pull architecture
- Clean LLD for each
- Exact modifications needed in your existing structure

No hand-waving. Real system design.

---

# 1⃣ Fully Implement Working Directory Restoration (Checkout Properly)

## 🎯 Goal

When user runs:

```
mini-vcs checkout feature
```

We must:

1. Switch HEAD pointer
2. Read commit
3. Traverse tree recursively
4. Recreate files exactly as snapshot
5. Delete files not in snapshot

---

## 🔧 Required Changes

### Repository.checkout(branch_name)

### Steps

### Step 1: Get target commit hash

```text
commit_hash = refs.get_branch_commit(branch_name)
```

---

### Step 2: Read commit object

Parse commit:

- Extract tree_hash

---

### Step 3: Rebuild Working Directory

We must implement:

```
_restore_tree(tree_hash, base_path)
```

---

## 🌳 Tree Traversal Algorithm

```
function restore_tree(tree_hash, current_path):
    read tree object
    for each entry:
        if blob:
            read blob
            write file to disk
        if tree:
            create directory
            recursively restore subtree
```

---

## ⚠ Critical Step: Remove Old Files

Before restore:

```
delete everything except .vcs/
```

To avoid stale files.

---

## 🧠 Edge Cases

- Nested directories
- Deleted files
- Empty tree
- Binary files

---

# 2⃣ Implement Full Tree Traversal Diff

Currently diff only handles text blobs.

We must implement:

### A) Commit vs Commit Diff

### Algorithm

```
function diff_commits(commitA, commitB):
    treeA = load_tree(commitA.tree_hash)
    treeB = load_tree(commitB.tree_hash)

    compare_trees(treeA, treeB)
```

---

## 🌲 Tree Comparison Algorithm

```
function compare_trees(treeA, treeB):
    filesA = flatten_tree(treeA)
    filesB = flatten_tree(treeB)

    for file in union(filesA, filesB):
        if file only in A:
            -> deleted
        if file only in B:
            -> added
        if both:
            if blob_hash different:
                -> modified (use LCS)
```

---

## 📌 flatten_tree()

Convert recursive tree into:

```
{
  "dir/file.txt": blob_hash
}
```

This simplifies diff logic.

---

# 3⃣ Add Merge Support

Now we enter serious territory.

---

## 🎯 Goal

```
merge feature
```

We must:

1. Find merge base
2. Do 3-way merge
3. Create merge commit (2 parents)

---

## 🔍 Step 1: Find Merge Base

We need:

```
lowest common ancestor (LCA) in DAG
```

Algorithm:

```
collect all ancestors of branch A
collect all ancestors of branch B
first common commit encountered = merge base
```

This works for small systems.

---

## 🔀 Step 2: 3-Way Merge

We compare:

- base version
- current branch version
- incoming branch version

For each file:

| Case                              | Action       |
| --------------------------------- | ------------ |
| Only changed in one branch        | Take changed |
| Changed differently in both       | Conflict     |
| Same change                       | Safe         |
| Deleted in one, modified in other | Conflict     |

---

## ⚠ Conflict Handling

Insert conflict markers:

```
<<<<<<< HEAD
current content
=======
incoming content
>>>>>>> feature
```

---

## 🧠 Merge Commit Structure

```
Commit(
    tree_hash=new_tree,
    parent_hashes=[current_head, feature_head]
)
```

This creates true DAG branching.

---

# 4⃣ Add Rebase Support

Rebase rewrites history.

---

## 🎯 Goal

```
rebase main
```

We:

1. Find commits unique to current branch
2. Replay them on top of target branch

---

## 🔍 Algorithm

```
find fork point
collect commits from fork → HEAD
reset branch pointer to target branch commit
replay commits one by one:
    apply diff
    create new commit
```

---

## ⚠ Important

Rebase creates new commit hashes.

Old commits become unreachable (garbage).

---

## 🔄 Replay Logic

For each commit:

```
diff = diff(parent, commit)
apply diff to new base
create new commit with:
    parent = last_replayed_commit
```

---

# 5⃣ Add Remote Push/Pull Simulation

Now we simulate distributed VCS.

---

## 🏗 Remote Architecture

Add:

```
.vcs/remotes/
```

Each remote stores:

```
remote_url
remote_refs
```

---

## 📡 Push

Push means:

1. Compare remote HEAD and local HEAD
2. Send missing objects
3. Update remote branch pointer

---

### Algorithm

```
find commits in local not in remote
send all related objects
update remote refs
```

Objects are content-addressed → safe to copy.

---

## 📥 Pull

Pull means:

1. Fetch missing objects
2. Merge remote branch into local

Pull = fetch + merge

---

## 🌍 Remote Simulation

We simulate remote as:

```
another directory path
```

So push = copying objects directory.

---

# 🔥 Required Structural Additions

Add:

```
vcs/
  merge.py
  rebase.py
  remote.py
```

---

# 🧠 Final Architecture After Upgrade

Mini VCS becomes:

```
Content Addressable Storage
+ Commit DAG
+ Branch References
+ Tree Snapshots
+ Working Directory Sync
+ 3-Way Merge
+ Rebase Engine
+ Remote Sync
```

This is now conceptually 70% of real Git.

---

# ⚡ Complexity Overview

| Feature  | Complexity           |
| -------- | -------------------- |
| Checkout | O(files)             |
| Diff     | O(n + LCS)           |
| Merge    | O(files + conflicts) |
| Rebase   | O(commits × diff)    |
| Push     | O(new_objects)       |

---

# 🚀 At This Point You Have Built

- Snapshot-based VCS
- DAG history model
- Branch pointer system
- 3-way merge engine
- History rewriting (rebase)
- Distributed object sync

This is advanced backend engineering.

---

# 🏁 Next Evolution Options

If you want to go truly elite:

- Garbage collection
- Packfile compression
- Delta encoding
- Shallow clone
- Conflict resolution engine
- Binary merge strategy
- Partial clone
- Large file support (LFS style)
- Concurrency locking
- Performance optimization
- File system abstraction layer
- Hook system
- Plugin architecture
