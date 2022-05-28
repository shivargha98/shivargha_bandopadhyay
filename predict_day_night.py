import numpy as np
from PIL import Image

class predict_day_night_algos:

    def __init__(self,img_path,algorithm_choice):
        self.img_path = img_path
        self.algorithm_choice = algorithm_choice

    def select_algorithm(self):
        """
         the function selects which algorithm,
         based on the user input
        """
        algo_choices = ["intensity_based","pixel_based"]
        if algo_choices[self.algorithm_choice] == "intensity_based":
            print("Using Intensity based method")
            intensity_value = self.intensity_algorithm()
            if intensity_value >= 0.35:
                return "day"
            else:
                return "night"


        elif algo_choices[self.algorithm_choice] == "pixel_based":
            print("Using pixel based method")
            percentage_darker_pixels = self.pixel_percentage_algorithm()
            if percentage_darker_pixels > 0.75:
                return "night"
            else:
                return "day"

    
    def intensity_algorithm(self):
        """
        description :the function calculates the intensity based on HSI model,
                     intensity = (R+G+B)/3, where R,G,B are all normalised arrays/bands
        input params : the image path
        return : intensity value of the image(single value)
        """
        ### Reading the images ####
        img = Image.open(self.img_path)
        ###converting to numpy array###
        arr = np.array(img)
        ###normalising the bands individually###
        Rn,Gn,Bn = (arr[:,:,0]/255),(arr[:,:,1]/255),(arr[:,:,2]/255)
        ###calculating the Intensity based on HSI model####
        intensity_arr = (Rn+Gn+Bn)/3
        #### taking average of the intensity array based on number of pixels in the intensity array ##
        intensity_value = np.sum(intensity_arr)/(intensity_arr.shape[0]*intensity_arr.shape[1])
        return intensity_value

    
    def pixel_percentage_algorithm(self):
        """
        description : this function calculates the percentage of darker pixels,
                      more the darker pixels tends to darker intensity in the image.
        input params : the image path
        return : percentage of number of pixels
        """
        ### Reading the images ####
        img = Image.open(self.img_path)
        ###converting to numpy array###
        arr = np.array(img)
        ### Calculating the number of pixels in the range 0--40, pixels in this range refer to darker intensity ###
        num_darker_pixels = np.sum(np.unique(arr,return_counts=True)[1][0:40])
        ###Calculating the percentage ####
        percentage_darker_pixels = (num_darker_pixels)/(arr.shape[0]*arr.shape[1]*arr.shape[2])
        ##### Rounding the percentage value #####
        percentage_darker_pixels = round(percentage_darker_pixels,2)
        return percentage_darker_pixels
