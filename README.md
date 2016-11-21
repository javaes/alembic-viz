####Installation
`pip install alembic-viz --user`

####Usage
```bash
Usage: alembic-viz [OPTIONS]

Options:
  --config TEXT           path to alembic config file
  --name TEXT             name of the alembic ini section
  --filename TEXT         output file name without file extension
  --format [png|svg|pdf]  output file format
  --help                  Show this message and exit.
```
  
####Todo
* add revision commit messages to graph
* handle `depends_on` relationships properly
* add test cases
* ...