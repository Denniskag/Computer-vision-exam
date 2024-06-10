import os
import shutil
from sklearn.model_selection import train_test_split


data_dir = 'training data' 
categories = ['motorcycles', 'saloon_cars']
train_dir = 'data_A/train'
test_dir = 'data_A/test'


os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

for category in categories:
    category_path = os.path.join(data_dir, category)
    images = os.listdir(category_path)
    images = [os.path.join(category_path, img) for img in images]

    
    train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)

    
    train_category_path = os.path.join(train_dir, category)
    test_category_path = os.path.join(test_dir, category)
    os.makedirs(train_category_path, exist_ok=True)
    os.makedirs(test_category_path, exist_ok=True)

    
    for img in train_images: 
        shutil.copy(img, os.path.join(train_category_path, os.path.basename(img)))

    
    for img in test_images:
        shutil.copy(img, os.path.join(test_category_path, os.path.basename(img)))

    print(f'{category}: {len(train_images)} images copied to train, {len(test_images)} images copied to test')

print('Data splitting and copying to Google Drive complete.')
