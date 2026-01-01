# How to Update Files in GitHub

This guide explains how to update files in your GitHub repository.

## Quick Update Process

### Step 1: Check Current Status
See what files have been modified:
```bash
git status
```

### Step 2: Add Files to Staging
Add specific files:
```bash
git add filename.txt
```

Or add all modified files:
```bash
git add .
```

### Step 3: Commit Changes
Create a commit with a descriptive message:
```bash
git commit -m "Description of your changes"
```

### Step 4: Push to GitHub
Upload your changes to GitHub:
```bash
git push
```

If it's your first push or branch changed:
```bash
git push -u origin main
```

## Complete Workflow Example

Here's a complete example of updating a file:

```bash
# 1. Make your changes to files (edit, add, delete)

# 2. Check what changed
git status

# 3. Add all changes
git add .

# 4. Commit with message
git commit -m "Updated README with new information"

# 5. Push to GitHub
git push
```

## Common Scenarios

### Scenario 1: Update a Single File

```bash
# Edit your file (e.g., README.md)
git add README.md
git commit -m "Updated README"
git push
```

### Scenario 2: Update Multiple Files

```bash
# Make changes to multiple files
git add file1.txt file2.txt file3.txt
git commit -m "Updated multiple files"
git push
```

### Scenario 3: Add New Files

```bash
# Create new files
git add newfile.txt
git commit -m "Added new file"
git push
```

### Scenario 4: Delete Files

```bash
# Delete a file
git rm oldfile.txt
git commit -m "Removed old file"
git push
```

## Useful Git Commands

### View Changes
```bash
# See what changed in files
git diff

# See commit history
git log

# See current status
git status
```

### Undo Changes (Before Committing)
```bash
# Discard changes to a file
git checkout -- filename.txt

# Unstage a file (remove from git add)
git reset HEAD filename.txt
```

### Update from GitHub (Pull Changes)
If someone else made changes or you edited on GitHub:
```bash
git pull
```

## Best Practices

1. **Write Clear Commit Messages**: Describe what you changed and why
   - Good: `"Added Looker Studio dashboard link"`
   - Bad: `"update"`

2. **Commit Often**: Make small, logical commits rather than one big commit

3. **Check Status First**: Always run `git status` before committing

4. **Pull Before Push**: If working with others, pull first:
   ```bash
   git pull
   git push
   ```

## Troubleshooting

### Error: "Your branch is ahead of 'origin/main'"
This means you have local commits not pushed yet. Just run:
```bash
git push
```

### Error: "Updates were rejected"
Someone else pushed changes. Pull first:
```bash
git pull
# Resolve any conflicts if needed
git push
```

### Error: "Nothing to commit"
All your changes are already committed. Check with:
```bash
git status
```

## Quick Reference Card

```
Make Changes → git add . → git commit -m "message" → git push
     ↓              ↓              ↓                    ↓
  Edit files    Stage files    Save locally      Upload to GitHub
```

## Example: Updating README

```bash
# 1. Edit README.md in your editor

# 2. Check status
git status
# Output: modified: README.md

# 3. Add the file
git add README.md

# 4. Commit
git commit -m "Updated README with project status"

# 5. Push
git push
```

That's it! Your changes are now on GitHub.

