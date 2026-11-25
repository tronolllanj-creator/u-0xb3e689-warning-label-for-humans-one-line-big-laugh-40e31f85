# warning-label-for-humans: one funny safety label, written to entry.txt.
import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir, 'entry.txt')

with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write('WARNING: Structural integrity relies heavily on mysterious leftover screws that definitely were not supposed to be optional.')
