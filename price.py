from prediction_util import PredictionUtil as xxx

gildong = xxx()

gildong.read('airbnb.csv')

gildong.show_unique_column()

gildong.drop(['id', 'minimum_nights', 'maximum_nights', 'number_of_reviews'])

gildong.heatmap(['accommodates', 'bathrooms', 'bedrooms', 'beds', 'price'])

gildong.plot_3d('bedrooms', 'beds', 'price')

gildong.run_linear_regress(['accommodates', 'bedrooms', 'beds'], 'price')

gildong.run_kneighbor_regress(['accommodates', 'bedrooms', 'beds'], 'price')

gildong.run_decision_tree(['accommodates', 'bedrooms', 'beds'], 'price')

gildong.run_random_forest(['accommodates', 'bedrooms', 'beds'], 'price')

gildong.run_all(['accommodates', 'bedrooms', 'beds'], 'price')

