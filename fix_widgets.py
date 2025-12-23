import nbformat

files = [
    "Model_MNB.ipynb",
    "Model_SVM.ipynb"
]

for path in files:
    try:
        nb = nbformat.read(path, as_version=4)

        if "widgets" in nb.metadata:
            del nb.metadata["widgets"]
            nbformat.write(nb, path)
            print(f"[OK] Widgets metadata dihapus: {path}")
        else:
            print(f"[SKIP] Tidak ada widgets metadata: {path}")

    except FileNotFoundError:
        print(f"[ERROR] File tidak ditemukan: {path}")