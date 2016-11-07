from alembic import util
from alembic.script import ScriptDirectory
from graphviz import Digraph


def get_revisions(config, rev_range=None):
    script = ScriptDirectory.from_config(config)

    if rev_range is not None:
        if ":" not in rev_range:
            raise util.CommandError("History range requires [start]:[end], [start]:, or :[end]")
        base, head = rev_range.strip().split(":")
    else:
        base = head = None

    return script.walk_revisions(
        base=base or "base",
        head=head or "heads",
    )


def generate_revision_graph(revisions, format):
    dot = Digraph(format='png')
    for revision in revisions:
        dot.node(revision.revision)
        if revision.down_revision is None:
            dot.edge('base', revision.revision)
            continue
        if isinstance(revision.down_revision, basestring):
            dot.edge(revision.down_revision, revision.revision)
            continue
        for down_revision in revision.down_revision:
            dot.edge(down_revision, revision.revision)
    return dot
