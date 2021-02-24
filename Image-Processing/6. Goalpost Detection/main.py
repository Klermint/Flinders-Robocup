import cv2                                                          # importing cv2 to read files
from fastai.vision.all import *
import matplotlib.pyplot as plt
from PIL import Image
# from fastbook import *                                              # import all fastai.vision library
# from fastai.vision.widgets import *

# """
# determine if img 'is_cat'
path = untar_data(URLs.PETS)/'images'                               # downloads a standard dataset from the fast.ai dataset collection
                                                                    # and returns a path to that location


def is_cat(x): return x[0].isupper()                                # label cats based on a filename rule by the dataset creators


dls = ImageDataLoaders.from_name_func(                              # tells fastai what kind of dataset and structure
    path, get_image_files(path), num_workers=0, valid_pct=0.2,
    seed=42, label_func=is_cat, item_tfms=Resize(224), bs=16)

learn = cnn_learner(dls, resnet34, metrics=error_rate)              # training image recognizer to create a CNN and specify what architecture to use
learn.fine_tune(2)                                                  # how to fit the model

# learn.save('model', pickle_protocol=4)

# learn.export()                                                     # export model
# path = Path()                                                      # test if the file exists
# print({path.ls(file_exts='.pkl')})
# learn_inf = load_learner(path/'export.pkl')                        # create inference learner from exported file

uploader = cv2.imread('cat.png')                                   # upload the picture of cat
print(learn.predict(uploader))
# output = learn.show_results()
# print()
# k = cv2.waitKey(1) & 0xFF

# img = PILImage.create(uploader.data[0])
# print(learn.predict(img))                                          # print the outcome
# """

"""
# car, outcome:
path = untar_data(URLs.CAMVID_TINY)
dls = SegmentationDataLoaders.from_label_func(
    path, bs=4, fnames = get_image_files(path/"images"), num_workers=0,
    label_func = lambda o: path/'labels'/f'{o.stem}_P{o.suffix}',
    codes = np.loadtxt(path/'codes.txt', dtype=str)
)

img = dls.show_batch()

learn = unet_learner(dls, resnet34)
learn.fine_tune(1)

# learn.export(os.path.abspath('./my_export.pkl'))
# learn_inf = load_learner(os.path.abspath('./my_export.pkl'))
car = cv2.imread('car.png')
print(learn.predict(car))
print(learn.show_results())
# learn.show_results settings = max_n=6, figsize=(7,8)


cv2.waitKey(0)

"""

"""
# movie review outcome:
dls = TextDataLoaders.from_folder(untar_data(URLs.IMDB), valid='test', num_workers=0)
learn = text_classifier_learner(dls, AWD_LSTM, drop_mult=0.5, metrics=accuracy)
learn.fine_tune(4, 1e-2)

learn.predict("I really liked that movie!")
"""

"""
# bear
key = os.environ.get('AZURE_SEARCH_KEY', '186041215d9a49388c5976b62b1f0203')

bear_types = 'grizzly','black','teddy'
path = Path('bears')

if not path.exists():
    path.mkdir()
    for o in bear_types:
        dest = (path/o)
        dest.mkdir(exist_ok=True)
        results = search_images_bing(key, f'{o} bear')
        download_images(dest, urls=results.attrgot('contentUrl'))

fns = get_image_files(path)
print(fns)

failed = verify_images(fns)
print(failed)

failed.map(Path.unlink);

bears = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=Resize(128))

bears = bears.new(
    item_tfms=RandomResizedCrop(224, min_scale=0.5),
    batch_tfms=aug_transforms())
dls = bears.dataloaders(path, num_workers=0)

learn = cnn_learner(dls, resnet18, metrics=error_rate)
learn.fine_tune(1)

black = cv2.imread('black.jpg')
print(learn.predict(black))
"""

"""
# soccer post
key = os.environ.get('AZURE_SEARCH_KEY', '186041215d9a49388c5976b62b1f0203')

path = Path('soccer goal')

if not path.exists():
    path.mkdir()
    dest = (path)
    dest.mkdir(exist_ok=True)
    results = search_images_bing(key, f'soccer goal')
    download_images(dest, urls=results.attrgot('contentUrl'))

fns = get_image_files(path)
print(fns)

failed = verify_images(fns)
print(failed)
failed.map(Path.unlink)

goal = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files, 
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=Resize(128))

goal = goal.new(
    item_tfms=RandomResizedCrop(224, min_scale=0.5),
    batch_tfms=aug_transforms())

dls = goal.dataloaders(path)
dls.valid.show_batch(max_n=4, nrows=1)

learn = cnn_learner(dls, resnet18, metrics=error_rate)
learn.fine_tune(1)

goal = cv2.imread('goal.jpg')
img = PILImage.create(goal)
soccer_goal,_,probs = learn.predict(img)
print({soccer_goal}, {probs[0].item()})

learn.show_results(max_n=6, figsize=(7,8))

cv2.waitKey(0)

"""