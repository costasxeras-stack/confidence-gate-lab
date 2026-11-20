# Rebuilding the data

The app only needs `data/results.json`. These scripts recreate it. Run them from this folder.

1. Download the Banking77 files into this folder:
   - https://raw.githubusercontent.com/PolyAI-LDN/task-specific-datasets/master/banking_data/train.csv
   - https://raw.githubusercontent.com/PolyAI-LDN/task-specific-datasets/master/banking_data/test.csv
2. `npm install` in the repo root, then `node scripts/embed.mjs` from this folder. It writes `train.json` and `test.json` with sentence embeddings. Takes about 5 minutes.
3. `python3 model.py` trains both models and prints accuracy and automation at several thresholds. Needs numpy and scikit-learn.
4. `python3 export.py` writes `../data/results.json`.

The intermediate files are ignored by git.
