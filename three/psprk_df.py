from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("ProductsAndCategories").getOrCreate()

products = spark.createDataFrame([(1, 'milk'),
                                  (2, 'water'),
                                  (3, 'meat'),
                                  (4, 'juice')], ['product_id', 'product_name'])

categories = spark.createDataFrame([(1, 'drinking'),
                                    (2, 'snacks'),
                                    (3, 'fruits')], ['category_id', 'category_name'])

product_category = spark.createDataFrame([(1, 1),
                                        (2, 1),
                                        (4, 1),
                                        (4, 3),
                                        (3, None)], ['product_id', 'category_id'])

all_products_with_category = ((product_category.join(products, 'product_id', 'left')
             .join(categories, 'category_id', 'left'))
             .select(products['product_name'], categories['category_name']))

products_no_categories = ((products.join(product_category, 'product_id', 'left')
                          .filter(col('category_id').isNull()))
                          .select(products['product_name']))

all_products_with_category.show() # все продукты и их категории, даже если не заданы
products_no_categories.show()  #  все продукты без категорий

spark.stop()
