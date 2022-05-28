from predict_day_night import predict_day_night_algos
import argparse

#### Getting the user inputs ###
my_parser = argparse.ArgumentParser()
my_parser.add_argument('--imgpath',action='store',type = str)
my_parser.add_argument('--algochoice',action='store',type=str)
args = my_parser.parse_args()

img_file_path = args.imgpath
algo_to_use = int(args.algochoice)

###creating an instance of the class###
predict_obj = predict_day_night_algos(img_file_path,algo_to_use)
scenario = predict_obj.select_algorithm()

print("Scenario of the given image:",scenario)