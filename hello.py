import sys
# Default is 'World'
name = sys.argv[1] if len(sys.argv) == 2 else "World"
print "Hello", name
