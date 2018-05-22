import click
import urllib.request
import glob
import cv2
from sklearn import linear_model
import numpy as np
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('Invoked command: ')
    else:
        click.echo('Invoked command:  %s' % ctx.invoked_subcommand)

@cli.command()
def download():
    #urllib.request.urlretrieve ("https://t2.uc.ltmcdn.com/images/5/0/6/img_como_saber_si_un_gato_es_macho_o_hembra_con_fotos_10605_600.jpg", "images/cat.jpg")
    urllib.request.urlretrieve("http://benchmark.ini.rub.de/Dataset_GTSDB/FullIJCNN2013.zip", "images/FullIJCNN2013.zip")

@cli.command()
def regresion():
    path_model = "model.pkl"
    images_names = read_images()
    x, y = read_data(images_names)
    X = np.asarray(x)
    X = X.flatten().reshape(X.shape[0], X.shape[1]*X.shape[2]*X.shape[3])
    Y = np.asarray(y)
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    logreg = linear_model.LogisticRegression()

    logreg.fit(x_train, y_train)
    joblib.dump(logreg, path_model)
    model = joblib.load(path_model)
    testeo  = cv2.resize(cv2.imread("./images/FullIJCNN2013/40/00000.ppm"), (32,32))
    testeo = testeo.flatten().reshape(1, 32*32*3)
    #print(model.predict(x_test[0].reshape(1, -1)))
    print(model.predict(testeo))



def read_images():
    images_directory_path = "./images/FullIJCNN2013/"
    images = []
    for i in range(43):
        if(i < 10):
            class_path = images_directory_path + "0" + str(i) + "/*.ppm"
        else:
            class_path = images_directory_path + str(i) + "/*.ppm"

        images_path = glob.glob(class_path)
        images.extend(images_path)
    return images

def read_data(images_names):
    x = []
    y = []
    for image_path in images_names:
        image = cv2.resize(cv2.imread(image_path), (32,32))
        x.append(image)
        y.append(int(image_path.split("/")[-2]))
    return x,y
