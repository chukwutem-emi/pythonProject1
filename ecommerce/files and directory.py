from pathlib import Path

path = Path("ecommerce")
print(path.exists())

pass

# example:
from pathlib import Path

path = Path("email")
print(path.mkdir())

# NB: mkdir = make directory.


# example:
from pathlib import Path

path = Path("ecommerce")
print(path.rmdir())


# NB:     rmdir = remove directory


from pathlib import Path

path = Path()
for file in path.glob("*.py"):
    print(file)

# NB: for file in path.glob("*.py")  is used to find all files.

