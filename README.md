# customer-segmentation-unsupervised-sreejagirijala
In this project, I worked on customer segmentation using the Online Retail dataset.
The main aim of this project is to group the customers based on their purchasing behavior using unsupervised machine learning techniques.

Customer segmentation helps businesses to understand the different types of customers and improve marketing strategies.
### Dataset which used
Dataset Name       : Online Retail II
Number of Records  : 6000+ (here i used sample because the git doesnot allow the dataset whhich the memory shouldnot greaterthan 25mb )
Important Features : InvoiceNo
                    Quantity
                    UnitPrice
                    InvoiceDate
                    CustomerID
                    Country    
  Before applying the machine learning algorithms , I cleaned the datset and prepared the dataset properly.
  
 ### Data Preprocessing
##### I performed the following 5 steps:
1.Removed missing values
2.Removed negative quantities
3.Converted date column into proper format
4.Created RFM features:
     4.1.Recency (how recently customer purchased)
     4.2.Frequency (how often customer purchased)
     4.3.Monetary (how much customer spent)
5.Applied feature scaling

### Algorithms which i implemented in this are-
In this project, I applied multiple clustering algorithms:
1.K-Means Clustering
2.Hierarchical Clustering
3.DBSCAN
4.Gaussian Mixture Model (GMM)
here i have used the Elbow Method to determine the optimal number of clusters.

### Visualizations
I created:
1.Elbow method graph
2.PCA cluster visualization
3.Cluster distribution plots
All output images are kept in the results folder.

### What I Learned from the Results
From the clustering results,
I understood that:
 Some customers buy products very often and spend a lot of money.
 Some customers buy products only sometimes.
 Some customers have not purchased anything recently and may need discounts or special offers.
This grouping helps businesses understand their customers better and plan marketing strategies more effectively.
### Tools Used
Python
Pandas and NumPy
Matplotlib
Scikit-learn
Google Colab

### Conclusion

Through this project, I learned how to clean real-world data and apply different clustering algorithms.
This project helped me understand how machine learning can be used in real business applications.
