import os


class Type:
    def __init__(self):
        pass

    def liste(self):
        ROOT_CHANTIERS = os.environ["ROOT_CHANTIERS"]

        liste = os.listdir(ROOT_CHANTIERS)
        return liste

    def current(self):
        ret = os.environ["TYPE"]
        return ret

    def setcurrent(self, type_name):
        os.environ["TYPE"] = type_name


class Projet:
    def __init__(self):
        pass

    def liste(self):
        ROOT_TYPE = os.environ["ROOT_TYPE"]

        liste = os.listdir(ROOT_TYPE)
        return liste

    def current(self):
        ret = os.environ["PROJET"]
        return ret

    def setcurrent(self, projet_name):
        os.environ["PROJET"] = projet_name


class Folder:
    def __init__(self):
        pass

    def liste(self):
        ROOT_PROJET = os.environ["ROOT_PROJET"]

        liste = os.listdir(ROOT_PROJET)
        return liste

    def current(self):
        ret = os.environ["FOLDER"]
        return ret

    def setcurrent(self, folder_name):
        os.environ["FOLDER"] = folder_name


class Soft:
    def __init__(self):
        pass

    def liste(self):
        ROOT_FOLDER = os.environ["ROOT_FOLDER"]

        liste = os.listdir(ROOT_FOLDER+"/02_work")
        return liste

    def current(self):
        ret = os.environ["SOFT"]
        return ret

    def setcurrent(self, soft_name):
        os.environ["SOFT"] = soft_name
