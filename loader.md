::Scriptura Loader (Multi-Version Runtime)::

1. Fetch https://raw.githubusercontent.com/drf3rd/scriptura/main/versions.json
2. Parse default_version (v08.01-law).
3. Offer user choice; default to the stable one after timeout.
4. Fetch that version’s manifest.json and initialize all declared layers.
