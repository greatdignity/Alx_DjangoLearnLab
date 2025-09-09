
**retrieve.md**
```markdown
# Retrieve Operation
# Retrieve Book

```python
from bookshelf.models import Book

# Retrieve the book by its title
book = Book.objects.get(title="1984")
book


# Output:
# 1984 George Orwell 1949
