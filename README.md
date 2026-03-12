# Mini Version Control System (Mini Git)

A lightweight educational implementation of a Version Control System inspired by Git.

This project demonstrates how modern version control systems work internally using:

- Content Addressable Storage
- Cryptographic Hashing
- Directed Acyclic Graphs (DAG)
- Immutable Snapshots
- Branch Pointers
- Diff Algorithms

---

## 📌 Objective

To build a simplified Git-like system from scratch in Python to deeply understand:

- How commits are stored
- How branches work internally
- How diffs are computed
- How history forms a DAG
- How immutability enables safety and performance

This is not a full Git replacement — it is a learning-focused implementation.

---

## 🧠 Core Concepts Implemented

### 1⃣ Content Addressable Storage (CAS)

Every object is stored by the hash of its content.

```
hash(content) → storage key
```

Benefits:

- Deduplication
- Integrity verification
- Immutable storage

---

### 2⃣ Object Types

The system models three fundamental Git objects:

#### Blob

- Represents file contents
- Immutable
- Identified by hash

#### Tree

- Represents directory structure
- Contains references to blobs and other trees
- Deterministic hashing via sorted entries

#### Commit

- Represents a snapshot
- Contains:
  - Tree reference
  - Parent commit(s)
  - Author
  - Timestamp
  - Message

Commits form a Directed Acyclic Graph (DAG).

---

### 3⃣ Commit DAG

```
A → B → C
      ↘ D
```

Each commit references its parent(s), creating a history graph.

This allows:

- Branching
- Merging
- Time travel (checkout)

---

### 4⃣ Branching Model

Branches are lightweight pointers:

```
refs/heads/main → commit_hash
refs/heads/feature → commit_hash
```

Branching does not duplicate history.
It simply creates a new reference.

---

### 5⃣ Staging Area (Index)

The index tracks:

```
file_path → blob_hash
```

Workflow:

```
add → update index
commit → snapshot index
```

---

### 6⃣ Diff Engine

Supports:

- Working directory vs last commit
- Commit vs commit comparison

File-level diff:

- Compare blob hashes

Line-level diff:

- Longest Common Subsequence (LCS) based algorithm

---

## 📂 Repository Structure

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

## ⚙ Core Commands (Conceptual)

| Command  | Description           |
| -------- | --------------------- |
| init     | Initialize repository |
| add      | Stage file            |
| commit   | Create snapshot       |
| log      | Show history          |
| branch   | Create branch         |
| checkout | Switch branch         |
| diff     | Show changes          |

---

## 🏗 Architecture Overview

```
Repository
 ├── ObjectStore
 ├── Index
 ├── RefManager
 ├── WorkingDirectory
```

### ObjectStore

- Stores objects by hash
- Prevents duplication

### Index

- Tracks staged files

### RefManager

- Manages HEAD
- Manages branch pointers

### Commit

- Immutable snapshot
- Forms DAG

---

## 🔐 Why Hashing Matters

Each object’s identity is derived from its content:

```
hash("type" + content)
```

This guarantees:

- Integrity
- Immutability
- Tamper detection
- Efficient storage

---

## 📈 Complexity Considerations

| Operation       | Complexity |
| --------------- | ---------- |
| Hash file       | O(n)       |
| Commit creation | O(files)   |
| Log traversal   | O(commits) |
| Diff (naive)    | O(n × m)   |

---

## 🎯 Skills Demonstrated

- Data Structures
- Directed Acyclic Graphs
- File System Design
- Hashing & Cryptographic Concepts
- Immutable Data Modeling
- Snapshotting
- Algorithmic Diff Computation
- System Design Thinking

---

## 🚀 Learning Outcomes

By building this project, you will understand:

- Why Git is fast
- Why commits are immutable
- Why branches are cheap
- How distributed version control works
- How object deduplication works
- How merge commits form multi-parent DAGs

---

## 🔮 Future Enhancements

- Merge support
- Rebase support
- Packfile compression
- Garbage collection
- Remote push/pull simulation
- Conflict resolution engine
- Binary file handling
- Performance optimizations
- fast O(1) staging

```md
vcs status
vcs merge
vcs reset
vcs clone
.vcsignore
```

---

## 📜 License

This project is licensed under the GNU General Public License v3.0 or later.

See: [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

SPDX-License-Identifier: GPL-3.0-or-later

---

## 👤 Author

Developer Jarvis _(Pen Name)_
GitHub: [https://github.com/DeveloperJarvis](https://github.com/DeveloperJarvis)
