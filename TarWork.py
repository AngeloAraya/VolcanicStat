import tarfile

def extract_file(path, to_directory):
    if (path.endswith("tar.gz")):
        tar = tarfile.open(path, "r:gz")
        tar.extractall(to_directory)
        tar.close()
    else:
        print("Archivo sin extension requerida, recuerde ingresar archivo tar.gz")