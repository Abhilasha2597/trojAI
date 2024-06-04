from trojai.datagen.image_entity import ImageEntity
from trojai.datagen.transform_interface import ImageTransform
from trojai.datagen.insert_merges import InsertAtLocation
from trojai.datagen.xform_merge_pipeline import XFormMerge
from trojai.datagen.experiment import ClassicExperiment
from trojai.datagen.image_affine_xforms import RandomRotateXForm
import numpy as np

class RandomRectangularPattern:
    def __init__(self, width_range=(5, 10), height_range=(5, 10)):
        self.width_range = width_range
        self.height_range = height_range

    def generate_pattern(self):
        width = np.random.randint(self.width_range[0], self.width_range[1] + 1)
        height = np.random.randint(self.height_range[0], self.height_range[1] + 1)
        return {'width': width, 'height': height}


class CustomImageEntity(ImageEntity):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def get_data(self):
        # Implement the logic to get image data here
        return self._data

    def get_mask(self):
        # Implement the logic to get image mask here
        pass
    
    
    
class ImageTransform:
 def __init__(self, entity, transforms):
        self.entity = entity
        self.transforms = transforms
        def apply_transformations(self, image):
            for transform in self.transforms:
               image = transform.apply(image)
               return image
            def transform(self):
               original_image = self.entity.get_data()
               transformed_image = self.apply_transformations(original_image)
               return transformed_image
    
class RandomRotateXForm:
 def apply(self, image):
  return image

        # Implement logic to apply random rotation to the image
        # For example, you can use image processing libraries like OpenCV
       
class UniformScaleXForm:
    def apply(self, image):
        # Implement logic to apply uniform scaling to the image
        # For example, you can use image processing libraries like OpenCV
        return image
# Use it in your code
trojan_pattern = RandomRectangularPattern()
trojan_pattern_data = trojan_pattern.generate_pattern()

# Define the dataset and trojan characteristics
clean_dataset_path = r'D:\trojai\trojai\scripts\datagen\mnist.py'
poisoned_dataset_path = 'D:\\trojai\\trojai\\poisoned_dataset'

num_poisoned_samples = 100  # Number of samples with trojans to generate


# Load the clean dataset
clean_data = []
with open(clean_dataset_path, 'r') as file:
  for line in file:
    clean_data.append(line.strip())  # Load the clean dataset using your preferred method

# Define the trojan Entity
trojan_entity = CustomImageEntity(data=trojan_pattern_data) 

# Define the Transform for the trojan
trojan_transforms = [RandomRotateXForm(), UniformScaleXForm()]  # Define trojan transformations

# ...

# Define the Transform for the trojan
trojan_transform = ImageTransform(entity=trojan_entity, transforms=trojan_transforms)


# Apply transformations to the image
transformed_image = trojan_transform.entity.get_data()  # Get the original image

for transform in trojan_transform.transforms:
   transformed_image = transform.apply(transformed_image)
# Define the Merge operation (e.g., insert the trojan in the center)
merge_operation = InsertAtLocation(1,2)

# Create the pipeline to generate the trojaned dataset
trojan_pipeline = XFormMerge(xform_list=[trojan_transform.transforms], merge_list=[merge_operation])

# Assuming you have your trojan_pipeline and trojaned_data from the previous code
# Replace 'your_data_root_dir' and 'your_trigger_label_xform' with the actual values you want to use.
experiment = ClassicExperiment(data_root_dir='experiment.data_root_dir', trigger_label_xform='experiment.trigger_label_xform')





# Execute the script to generate the poisoned dataset
# For example, add print statements to check the trojan pattern data
print("Trojan Pattern Data:", trojan_pattern_data)

# Add print statements to check the state of the images and transformations
print("Clean Data:", clean_data)
print("Trojan Transforms:", trojan_transforms)
