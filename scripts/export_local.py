#!/usr/bin/env python3
"""Build the official Assignment 1 export zip on your own computer, for when Colab will not start.

It runs the notebook's own export code (retrieve_homework_data) on your log database,
so the zip is the same one the notebook would make.

1. In Google Drive, download My Drive > oai_assignment01 > oai_assignment01.db
2. In Colab, File > Download > Download .ipynb (your own copy of the notebook)
3. Run:  python3 scripts/export_local.py <notebook.ipynb> <oai_assignment01.db> [output_folder]

The zip (oai_assignment01_team2_<time>.zip) is written to output_folder (default: the current folder).
Upload it to your own folder in company_b_1. Do not rename it or zip it again.
"""
import json
import os
import shutil
import sys
import tempfile

if len(sys.argv) < 3:
    sys.exit(__doc__)
nb_path, db_path = sys.argv[1], sys.argv[2]
out_dir = os.path.abspath(sys.argv[3] if len(sys.argv) > 3 else '.')
os.makedirs(out_dir, exist_ok=True)

nb = json.load(open(nb_path))
sources = [''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'code']
tools = next(s for s in sources if s.startswith('#@title Assignment tools'))

work = tempfile.mkdtemp(prefix='oai_export_')
shutil.copy(db_path, os.path.join(work, 'oai_assignment01.db'))   # never touch the original

g = {'__name__': 'export'}
exec('import csv, os, re, json, time, sqlite3, subprocess, hashlib, zipfile, shutil, platform, inspect, '
     'textwrap, random, math, base64, zlib\nfrom collections import Counter, defaultdict\n'
     'from datetime import datetime, timezone', g)
g['FINAL_PROJECT_TEAM_NUMBER'] = 2
exec(tools, g)
g.update(BASE_DIR=work, DB_PATH=os.path.join(work, 'oai_assignment01.db'), AUTO_SNAPSHOT=False)

# Task titles come from each module's "Hints and references" cell.
for s in sources:
    if 'register_task(' in s and not s.startswith('#@title'):
        try:
            exec(s, g)
        except Exception:
            pass

g['status']()
g['retrieve_homework_data'](upload_dir=out_dir, download=False)
