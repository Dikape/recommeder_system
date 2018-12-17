# import numpy as np
#
# from sklearn import metrics
# from sklearn import preprocessing
#
# DIPLOMA_PATH = '/home/dkasyanchik/projects/diploma'
# f = open(f"{DIPLOMA_PATH}/rand.csv")
# header = f.readline()
# print(header)
# names = ['id','age_range','birthday','gender','first_name','last_name','location_lat','location_lng','home_town_lat','home_town_lng']
# formats = [('id', '<f8'), ('age_range', '<i8'), ('birthday', '<U'), ('gender', '<i8'), ('first_name', '<U'), ('last_name', '<U'),
# 		   ('location_lat', '<f8'), ('location_lng', '<f8'), ('home_town_lat', '<f8'), ('home_town_lng', '<f8')]
# cols_to_clustering  = ['age_range','gender','location_lat','location_lng','home_town_lat','home_town_lng']
# used_indexes = [i for i, v in enumerate(names) if v in cols_to_clustering]
# data = np.genfromtxt(f, delimiter=',')#, usecols=used_indexes)
#
# print(type(data))
# print(f'ndim = {data.ndim}')
# print(f'shape = {data.shape}')
# print(f'size = {data.size}')
# print(f'dtype = {data.dtype}')
# print(f'itemsize = {data.itemsize}')
# print(f'data = {data.data}')
# print(data)
#
# min_max_scaler = preprocessing.MinMaxScaler()
# new_data = min_max_scaler.fit_transform(data)
# # krya = []
# # for obj in new_data:
# # 	new_obj = []
# # 	new_obj.append(obj[0]*10)
# # 	new_obj.append(obj[1])
# # 	new_obj.append(obj[2]*10)
# # 	new_obj.append(obj[3]*10)
# # 	new_obj.append(obj[4]*10)
# # 	new_obj.append(obj[5]*10)
# # 	krya.append(new_obj)
# # new_data = np.array(krya)
# print(new_data)
#
#
# from sklearn.cluster import AffinityPropagation, MeanShift, estimate_bandwidth, KMeans
#
#
# # bandwidth = estimate_bandwidth(data, quantile=0.2, n_samples=20)
#
# # ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
# # ms.fit(data)
# # labels = ms.labels_
# # cluster_centers = ms.cluster_centers_
#
# # labels_unique = np.unique(labels)
# # n_clusters_ = len(labels_unique)
#
# # print("number of estimated clusters : %d" % n_clusters_)
#
# # # #############################################################################
# # # Plot result
# # import matplotlib.pyplot as plt
# # from itertools import cycle
#
# # plt.figure(1)
# # plt.clf()
#
# # colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
# # for k, col in zip(range(n_clusters_), colors):
# #     my_members = labels == k
# #     cluster_center = cluster_centers[k]
# #     plt.plot(data[my_members, 0], data[my_members, 1], col + '.')
# #     plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
# #              markeredgecolor='k', markersize=14)
# # plt.title('Estimated number of clusters: %d' % n_clusters_)
# # plt.show()
#
# clustering = AffinityPropagation(max_iter=1000).fit(new_data)
# print(clustering)
# labels = clustering.labels_
# print(labels)
# print(clustering.cluster_centers_)
# cluster_centers_indices = clustering.cluster_centers_indices_
# n_clusters_ = len(cluster_centers_indices)
# print(n_clusters_)
#
# print('Estimated number of clusters: %d' % n_clusters_)
# # print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
# # print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
# # print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
# # print("Adjusted Rand Index: %0.3f"
# #       % metrics.adjusted_rand_score(labels_true, labels))
# # print("Adjusted Mutual Information: %0.3f"
# #       % metrics.adjusted_mutual_info_score(labels_true, labels))
# print("Silhouette Coefficient: %0.3f"
#       % metrics.silhouette_score(data, labels, metric='sqeuclidean'))
#
# # predicition = clustering.predict([[42,1, 40.222, 37.1222, 40.222, 37.1222], [34,0, -40.222, 37.1222, 40.222, 37.1222]])
# # print(f'[92, 1, 40.222, 37.1222, 40.222, 37.1222] is a part of cluster {predicition[0]} with cssenter {data[cluster_centers_indices[predicition[0]]]}')
# # print(f'[21, 1, -40.222, 37.1222, 40.222, 37.1222] is a part of cluster {predicition[1]} with center {data[cluster_centers_indices[predicition[1]]]}')
#
# # Plot result
# import matplotlib.pyplot as plt
# from itertools import cycle
#
# plt.close('all')
# plt.figure(1)
# plt.clf()
#
# colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
# for k, col in zip(range(n_clusters_), colors):
#     class_members = labels == k
#
#     cluster_center = data[cluster_centers_indices[k]]
#     print(f'Cluster center({k})={cluster_center}')
#     for i, obj in enumerate(data):
#     	if class_members[i]:
#     		print(obj)
#     print('\n')
#
#     plt.plot(data[class_members, 0], data[class_members, 1], col + '.')
#     plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=14)
#     for x in data[class_members]:
#         plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)
#
# plt.title('Estimated number of clusters: %d' % n_clusters_)
# plt.show()
