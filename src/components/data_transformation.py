import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utilis import save_object


class Datatransform_Confg:
    preprocessor_ob_file_path =  os.path.join('artifacts',"preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_trasformation_config = Datatransform_Confg()

    def get_data_transformer_object(self): 
        '''this function is just to create all my pickle files which will be responsible for 
        converting all the categorical features to numerical.

        is responsible for data transformation
'''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            
            logging.info(f"Numerical columns: {numerical_columns}")
            logging.info(f"Categorical columns: {categorical_columns}")

            num_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="median")), # to handle the missing values in num features
                    ("scalar", StandardScaler())
                ]


            )
            cate_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy = "most_frequent")),
                    ("one_hot_encoder", OneHotEncoder(sparse_output=False)),
                    ("scaler", StandardScaler(with_mean=False))

                ]

            )
            

            logging.info("Numerical columns standard scaling completed")
            logging.info("Categorical columns standard scaling completed")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cate pipeline", cate_pipeline, categorical_columns)
                ]
            )

            return preprocessor
        
            
        except Exception as e:
            raise CustomException (e,sys)
        

    def initiate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed!!!")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis =1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testiong dataframe."
            )

            input_feature_train_arr =preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.fit_transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]

            logging.info(f"Saved preprocessing object")

            save_object(
                file_path = self.data_trasformation_config.preprocessor_ob_file_path,
                obj = preprocessing_obj
            )

            return (
                train_arr, 
                test_arr, 
                self.data_trasformation_config.preprocessor_ob_file_path,
            )


        except Exception as e:
            raise CustomException(e, sys)
            
