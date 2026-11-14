print("Hello, Git!")

print("Version 2 — updated output")

<<<<<<< HEAD

print("Output from main branch")

=======

print("Output from feature-branch")

>>>>>>> feature-branch

<<<<<<< HEAD → everything between here and ======= is the current branch (main) version

======= → divider between the two conflicting versions

>>>>>>> feature-branch → everything between ======= and here is the incoming branch versionprint("Hello, Git!")
print("Version 2 — updated output")
<<<<<<< HEAD
print("Output from main branch")
=======
print("Output from feature-branch")
>>>>>>> feature-branch

