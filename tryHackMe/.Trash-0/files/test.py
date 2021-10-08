import pickle
fp = open("serverlocation.info", "rb")
print(pickle.load(fp))